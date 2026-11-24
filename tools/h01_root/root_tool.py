#!/usr/bin/env python3
"""H01 Magisk 30.7 host-side assistant (ADB/Fastboot, Python 3.8+).

Adapted from the H01-Root-Co-Dinh v1.1 Notion-tested workflow. No boot
images, serials, private hashes, OEM binaries or Magisk APK are bundled.
This generalized script itself has NOT been tested on a physical H01.
"""
import argparse
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

BOOT_SIZE = 33554432
BOOT_PARTITION = "/dev/block/bootdevice/by-name/boot"
ROOT_CONFIRM = "I-CONFIRM-ROOT-FLASH-ON-MY-H01"
RESTORE_CONFIRM = "I-CONFIRM-STOCK-RESTORE-ON-MY-H01"


def digest_file(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for piece in iter(lambda: stream.read(1048576), b""):
            h.update(piece)
    return h.hexdigest()


def checked_digest(s):
    if not isinstance(s, str) or not re.fullmatch(r"[a-fA-F0-9]{64}", s):
        raise ValueError("Expected SHA-256 must be a 64-character hexadecimal string")
    return s.lower()


def load_config(filename):
    path = Path(filename).resolve()
    d = json.loads(path.read_text(encoding="utf-8"))
    serial = d["serial"]
    if not isinstance(serial, str) or not re.fullmatch(r"[A-Za-z0-9_-]{4,80}", serial):
        raise ValueError("Invalid serial in private config")
    for key in ("stock_sha256", "patched_sha256"):
        d[key] = checked_digest(d[key])
    if d["stock_sha256"] == d["patched_sha256"]:
        raise ValueError("Stock/patched hashes must differ")
    d["stock_image"] = path.parent / d["stock_image"]
    d["patched_image"] = path.parent / d["patched_image"]
    d["backup_image"] = path.parent / "private-backup" / "boot-before.img"
    return d


def verify_images(d):
    for filename, expected in ((d["stock_image"], d["stock_sha256"]),
                               (d["patched_image"], d["patched_sha256"])):
        if not filename.is_file() or filename.stat().st_size != BOOT_SIZE:
            raise ValueError("Missing image or unexpected boot size: %s" % filename)
        if digest_file(filename) != expected:
            raise ValueError("SHA-256 mismatch: %s" % filename)
    return True


def command(args, check=True):
    r = subprocess.run(args, stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE, universal_newlines=True)
    output = (r.stdout + "\n" + r.stderr).strip()
    if check and r.returncode:
        raise RuntimeError("Command failed: %s\n%s" % (" ".join(args[:3]), output[:1600]))
    return output


def adb(d, *args):
    return command(["adb", "-s", d["serial"]] + list(args))


def fastboot(d, *args):
    return command(["fastboot", "-s", d["serial"]] + list(args))


def device_check(d):
    props = {k: adb(d, "shell", "getprop", k).strip() for k in (
        "ro.product.model", "ro.board.platform", "ro.build.version.sdk",
        "ro.boot.flash.locked", "ro.boot.slot_suffix")}
    if props["ro.product.model"] not in ("K1", "H01"):
        raise ValueError("Unexpected device model")
    if props["ro.board.platform"] != "msm8909":
        raise ValueError("Unexpected SoC")
    if props["ro.build.version.sdk"] != "27":
        raise ValueError("Not Android 8.1 / SDK27")
    if props["ro.boot.flash.locked"] != "0" or props["ro.boot.slot_suffix"]:
        raise ValueError("Bootloader not confirmed unlocked or device is A/B")
    return props


def root_check(d):
    device_check(d)
    result = adb(d, "shell", "su", "-c", "id")
    if not re.search(r"\buid=0\(root\)", result):
        raise ValueError("Magisk Shell root is not granted")
    m = adb(d, "shell", "su", "-c", "magisk -V").strip()
    if m != "30700":
        raise ValueError("Expected Magisk 30.7 (version code 30700), got %r" % m)
    boot = adb(d, "shell", "su", "-c",
               "sha256sum " + BOOT_PARTITION).split()[0].lower()
    checked_digest(boot)
    if boot not in (d["stock_sha256"], d["patched_sha256"]):
        raise ValueError("Physical boot partition differs from known images")
    print("ROOT PASS: uid=0, Magisk 30.7, read-only partition hash matches")
    print("CURRENT BOOT: " + ("stock" if boot == d["stock_sha256"] else "patched"))
    return boot


def fastboot_check(d):
    devices = command(["fastboot", "devices"]).splitlines()
    found = [line.split()[0] for line in devices if len(line.split()) >= 2]
    if len(found) != 1 or found[0] != d["serial"]:
        raise ValueError("Exactly one matching Fastboot device required")
    info = fastboot(d, "oem", "device-info")
    gv = fastboot(d, "getvar", "unlocked")
    if re.search(r"\bDevice unlocked:\s*false\b", info, re.I) or re.search(
            r"\bunlocked:\s*(no|false)\b", gv, re.I):
        raise ValueError("Bootloader reports locked")
    if not (re.search(r"\bDevice unlocked:\s*true\b", info, re.I) or
            re.search(r"\bunlocked:\s*(yes|true)\b", gv, re.I)):
        raise ValueError("Could not positively verify main bootloader unlocked")


def backup_partition(d, expected):
    out = d["backup_image"]
    if out.exists():
        if out.stat().st_size != BOOT_SIZE or digest_file(out) != expected:
            raise ValueError("Existing backup mismatch; never overwrite it")
        print("Existing local backup verified")
        return out
    out.parent.mkdir(parents=True, exist_ok=True)
    tmp = out.with_suffix(".tmp")
    if tmp.exists():
        raise ValueError("Temporary backup exists; inspect it before retry")
    with tmp.open("xb") as f:
        r = subprocess.run(["adb", "-s", d["serial"], "exec-out", "su", "-c",
                            "dd if=%s bs=1048576" % BOOT_PARTITION],
                           stdout=f, stderr=subprocess.PIPE)
    if r.returncode or tmp.stat().st_size != BOOT_SIZE or digest_file(tmp) != expected:
        raise ValueError("Backup failed/incomplete; inspect %s and STOP" % tmp)
    tmp.rename(out)
    print("BOOT BACKUP PASS: stored privately at %s" % out)
    return out


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("action", choices=["check", "root-status", "boot-ram",
                                      "backup", "flash-root", "restore-stock"])
    p.add_argument("--config", required=True, help="Private JSON config.local.json")
    p.add_argument("--confirm", default="", help="Explicit phrase required for flash")
    args = p.parse_args(argv)
    d = load_config(args.config)
    verify_images(d)
    if args.action == "check":
        print("LOCAL IMAGES PASS: matched 32 MiB + both expected SHA-256 values")
    elif args.action == "root-status":
        root_check(d)
    elif args.action == "boot-ram":
        fastboot_check(d)
        print("Starting RAM-only boot (does not flash boot partition)")
        print(fastboot(d, "boot", str(d["patched_image"])))
        print("After Android boots, explicitly run root-status and grant Magisk Shell access")
    elif args.action == "backup":
        current = root_check(d)
        backup_partition(d, current)
    elif args.action == "flash-root":
        if args.confirm != ROOT_CONFIRM:
            raise ValueError("Explicit --confirm %s required" % ROOT_CONFIRM)
        current = root_check(d)
        if current != d["stock_sha256"]:
            raise ValueError("Refusing to overwrite a boot partition not matching STOCK")
        backup_partition(d, current)
        print("Rebooting to Fastboot. If verification fails, device remains untouched.")
        adb(d, "reboot", "bootloader")
        fastboot_check(d)
        print(fastboot(d, "flash", "boot", str(d["patched_image"])))
        print("Flash command returned success. MANUALLY reboot and verify root-status.")
    elif args.action == "restore-stock":
        if args.confirm != RESTORE_CONFIRM:
            raise ValueError("Explicit --confirm %s required" % RESTORE_CONFIRM)
        fastboot_check(d)
        print(fastboot(d, "flash", "boot", str(d["stock_image"])))
        print("Stock restore command returned success. MANUALLY reboot/check startup.")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (OSError, ValueError, RuntimeError, KeyError, json.JSONDecodeError) as exc:
        sys.exit("STOP: %s" % exc)
