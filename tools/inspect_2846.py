#!/usr/bin/env python3
"""Read-only offline 2846 feature audit for a locally owned GlocalmeHome.apk.

Pure Python 3 (no ADB, no root, no decompilation dependency).
This tool extracts only narrowly scoped facts from DEX and binary AXML.
It never extracts APK members to disk or publishes OEM bytecode.
"""

import argparse
import hashlib
import struct
import sys
import zipfile
from pathlib import Path

LAB_SHA256 = "c0c047bd6ad91e888becf9142fef0f09eb08fc1743a6e23781033507044a981c"


def u16(data, at):
    return struct.unpack_from("<H", data, at)[0]


def u32(data, at):
    return struct.unpack_from("<I", data, at)[0]


def uleb128(data, at):
    value = 0
    for shift in (0, 7, 14, 21, 28):
        octet = data[at]
        at += 1
        value |= (octet & 0x7f) << shift
        if not octet & 0x80:
            return value, at
    raise ValueError("invalid ULEB128")


class Dex:
    def __init__(self, data):
        self.data = data
        if data[:4] != b"dex\n" or data[7] != 0:
            raise ValueError("expected standard DEX input")
        (string_count, string_off, type_count, type_off, proto_count, proto_off,
         _field_count, _field_off, method_count, method_off,
         class_count, class_off) = struct.unpack_from("<12I", data, 0x38)
        if not (0 < string_count < 500000 and 0 < class_count < 50000):
            raise ValueError("unexpected DEX table counts")

        self.strings = []
        for i in range(string_count):
            at = u32(data, string_off + 4*i)
            _, at = uleb128(data, at)
            stop = data.find(b"\0", at)
            if stop < 0:
                raise ValueError("unterminated DEX string")
            self.strings.append(data[at:stop].decode("utf-8", errors="replace"))
        self.types = [self.strings[u32(data, type_off + 4*i)] for i in range(type_count)]
        protos = []
        for i in range(proto_count):
            _, ret, params_off = struct.unpack_from("<III", data, proto_off + 12*i)
            n = u32(data, params_off) if params_off else 0
            params = tuple(self.types[u16(data, params_off + 4 + 2*j)] for j in range(n))
            protos.append((self.types[ret], params))
        self.methods = []
        for i in range(method_count):
            owner, proto, name = struct.unpack_from("<HHI", data, method_off + 8*i)
            self.methods.append((self.types[owner], self.strings[name], protos[proto]))
        self.codes = {}
        for i in range(class_count):
            class_index, _, _, _, _, _, off, _ = struct.unpack_from("<8I", data, class_off + 32*i)
            if not off:
                continue
            counts = []
            for _ in range(4):
                n, off = uleb128(data, off)
                counts.append(n)
            for count in counts[:2]:
                for _ in range(count):
                    _, off = uleb128(data, off)
                    _, off = uleb128(data, off)
            for count in counts[2:]:
                index = 0
                for _ in range(count):
                    diff, off = uleb128(data, off)
                    _, off = uleb128(data, off)
                    code_off, off = uleb128(data, off)
                    index += diff
                    if code_off:
                        self.codes[index] = code_off

    def method_index(self, class_name, method_name):
        for i, (owner, name, proto) in enumerate(self.methods):
            if owner == class_name and name == method_name and i in self.codes:
                return i
        raise ValueError("method not found: {}->{}".format(class_name, method_name))

    def instructions(self, class_name, method_name):
        """Yield selected metadata with conservative instruction boundaries.

        This is not a general DEX disassembler; unsupported opcodes fail closed.
        """
        off = self.codes[self.method_index(class_name, method_name)]
        size = u32(self.data, off + 12)
        inst = [u16(self.data, off + 16 + 2*i) for i in range(size)]
        i = 0
        while i < size:
            first = inst[i]
            op = first & 0xff
            width = opcode_width(op)
            if width is None or i + width > size:
                raise ValueError("unsupported or malformed DEX opcode {}".format(hex(op)))
            words = inst[i:i+width]
            ref = None
            if op == 0x1a:  # const-string
                ref = self.strings[words[1]]
            elif op == 0x1b:  # const-string/jumbo
                ref = self.strings[words[1] | (words[2] << 16)]
            elif op in range(0x6e, 0x79) and op != 0x73:  # invoke-* (index in second word)
                owner, name, _ = self.methods[words[1]]
                ref = owner + "->" + name
            elif op == 0x12:  # const/4, sign-extended literal
                n = (first >> 12) & 0xf
                ref = str(n if n < 8 else n-16)
            yield (op, ref)
            i += width


def opcode_width(op):
    if op in (0x00, 0x01, 0x04, 0x07) or 0x0a <= op <= 0x12 or op in (0x1d, 0x1e, 0x21, 0x27, 0x28):
        return 1
    if op in (0x02, 0x05, 0x08, 0x13, 0x15, 0x16, 0x19, 0x1a, 0x1c, 0x1f, 0x20, 0x22, 0x23, 0x29) or 0x2d <= op <= 0x3d or 0x44 <= op <= 0x6d or 0xd0 <= op <= 0xe2:
        return 2
    if op in (0x03, 0x06, 0x09, 0x14, 0x17, 0x1b, 0x24, 0x25, 0x26, 0x2a, 0x2b, 0x2c) or 0x6e <= op <= 0x78:
        return 3
    if op == 0x18:
        return 5
    if 0x7b <= op <= 0x8f or 0xb0 <= op <= 0xcf:
        return 1
    if 0x90 <= op <= 0xaf:
        return 2
    return None


def check_rule(items, required):
    actual = {ref for _, ref in items if ref is not None}
    return all(needle in actual for needle in required)


def inspect(apk):
    digest = hashlib.sha256(apk.read_bytes()).hexdigest()
    with zipfile.ZipFile(apk) as z:
        dex = Dex(z.read("classes.dex"))
        about_xml = z.read("res/layout/about_settings_activity.xml")
        assistant_xml = z.read("res/layout/assistant_activity.xml")

    about = "Lcom/glocalme/minilauncher/about/MiniAboutActivity;"
    confirm = "Lcom/glocalme/minilauncher/about/MiniAboutActivity$5;"
    assistant = "Lcom/glocalme/minilauncher/assistant/AssistantActivity;"
    rules = [
        ("About: five taps", about, "startAssistantFunction",
         ["5", about+"->createPasswordDialog"]),
        ("Password: compare 2846 + navigate via ARouter", confirm, "onClick",
         ["2846", "Ljava/lang/String;->contentEquals", "/minilauncher/assistant",
          "Lcom/alibaba/android/arouter/launcher/ARouter;->getInstance",
          "Lcom/alibaba/android/arouter/facade/Postcard;->navigation"]),
        ("Assistant: MMI explicit intent", assistant, "startMMI",
         ["com.ukelink.dusk.mmi", "com.ukelink.dusk.mmi.MainActivity",
          "Landroid/content/Intent;->setClassName"]),
        ("Assistant: feedback logging intent", assistant, "startLogTools",
         ["com.ucloudlink.feedback", "com.ucloudlink.feedback.LogSettingActivity",
          "Landroid/content/Intent;->setClassName"]),
        ("Assistant: Android Settings intent", assistant, "startSystemSettings",
         ["com.android.settings", "com.android.settings.Settings",
          "Landroid/content/Intent;->setClassName"]),
    ]
    print("APK SHA256:", digest)
    print("Reference sample:", "MATCH" if digest == LAB_SHA256 else "DIFFERENT BUILD")
    passed = 0
    for label, cls, method, patterns in rules:
        items = list(dex.instructions(cls, method))
        ok = check_rule(items, patterns)
        print("{}: {}".format("PASS" if ok else "FAIL", label))
        if not ok:
            print("  Missing:", ", ".join(s for s in patterns if s not in {ref for _, ref in items}))
        passed += bool(ok)
    # Resource XML has a binary string pool; detect callback symbols only.
    layout_ok = b"startAssistantFunction" in about_xml and all(
        key.encode("utf-8") in assistant_xml
        for key in ("startMMI", "startLogTools", "startSystemSettings")
    )
    print("{}: layout callback strings".format("PASS" if layout_ok else "FAIL"))
    passed += bool(layout_ok)
    print("Result: {}/6 checks passed".format(passed))
    print("This is offline static evidence, not proof of runtime execution on other firmware.")
    return 0 if passed == 6 else 1


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("apk", type=Path, help="Locally held OEM GlocalmeHome APK")
    args = parser.parse_args(argv)
    if not args.apk.is_file():
        parser.error("APK file does not exist")
    if args.apk.stat().st_size > 100 * 1024 * 1024:
        parser.error("APK over 100 MiB not supported")
    try:
        return inspect(args.apk)
    except (OSError, KeyError, IndexError, ValueError, struct.error, zipfile.BadZipFile) as exc:
        print("ERROR:", exc, file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
