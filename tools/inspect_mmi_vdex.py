#!/usr/bin/env python3
"""ZEUS H01 / MMI VDEX 010: inspect only its 2846 broadcast receiver.

Offline, read-only, no OEM code extraction, decompilation, or device access.
Outputs only selected symbolic references; never publishes extracted DEX.
Requires sibling inspect_2846.py for DEX metadata parsing.
"""
import argparse
import hashlib
from pathlib import Path
import struct
import sys

from inspect_2846 import Dex, u16, u32, opcode_width

RECEIVER = 'Lcom/ukelink/dusk/mmi/MySecretCodeReceiver;'
MMI_MAIN = 'Lcom/ukelink/dusk/mmi/MainActivity;'
SECRET_ACTION = 'android.provider.Telephony.SECRET_CODE'

class FormatError(ValueError):
    pass


def vdex_sections(data):
    if len(data) < 32 or data[:8] != b'vdex010\0':
        raise FormatError('Expected Android 8.1 VDEX 010')
    number, dex_size, deps_size, quick_size = struct.unpack_from('<IIII', data, 8)
    if number != 1:
        raise FormatError('This narrow tool supports exactly one embedded DEX')
    dex_start = 24 + number * 4
    end = dex_start + dex_size + deps_size + quick_size
    if end != len(data) or dex_size < 112 or quick_size < 12:
        raise FormatError('Inconsistent VDEX header sizes')
    dex = data[dex_start:dex_start+dex_size]
    if dex[:4] != b'dex\n' or u32(dex,32) != len(dex):
        raise FormatError('Invalid embedded DEX header/size')
    return dex, data[dex_start+dex_size+deps_size:end]


def quickening_for_method(quick_blob, code_offset):
    """VDEX010: tail pointer -> (code_item_off, quick_data_off) pairs."""
    if len(quick_blob) < 12:
        raise FormatError('Quickening section is too small')
    index_start = u32(quick_blob, len(quick_blob) - 4)
    end = len(quick_blob) - 4
    if index_start >= end or (end - index_start) % 8:
        raise FormatError('Malformed quickening index table')
    offsets = []
    for pos in range(index_start, end, 8):
        off, value = struct.unpack_from('<II', quick_blob, pos)
        if off == code_offset:
            offsets.append(value)
    if len(offsets) != 1:
        raise FormatError('Expected exactly one quickening entry for code item')
    offset = offsets[0]
    if offset + 4 > index_start:
        raise FormatError('Quickening payload pointer out of range')
    nbytes = u32(quick_blob, offset)
    if nbytes & 1 or offset + 4 + nbytes > index_start:
        raise FormatError('Invalid quickening payload length')
    return [u16(quick_blob, offset+4+2*i) for i in range(nbytes//2)]


def field_ids(dex):
    data = dex.data
    count, offset = u32(data, 0x50), u32(data, 0x54)
    if offset + count * 8 > len(data):
        raise FormatError('Field table out of DEX range')
    fields = []
    for i in range(count):
        cls, typ, name = struct.unpack_from('<HHI', data, offset+i*8)
        fields.append((dex.types[cls], dex.strings[name], dex.types[typ]))
    return fields


def method_insns(dex, quick_blob, cls, method, fields):
    index = dex.method_index(cls, method)
    code_off = dex.codes[index]
    quick = quickening_for_method(quick_blob, code_off)
    size = u32(dex.data, code_off + 12)
    if size > 10000 or code_off + 16 + size * 2 > len(dex.data):
        raise FormatError('Unreasonably large or truncated method')
    words = [u16(dex.data, code_off+16+2*i) for i in range(size)]
    pos = 0
    used = 0
    events = []
    while pos < size:
        op = words[pos] & 0xff
        if op in (0xe3,0xe4,0xe5,0xe6,0xe7,0xe8,0xef,0xf0,0xf1,0xf2,0xf3,0xf4,0xf5,0xf6,0xf7,0xf8):
            width = 2
        elif op in (0xe9,0xea):
            width = 3
        elif op == 0x73:  # return-void-no-barrier
            width = 1
        else:
            width = opcode_width(op)
        if width is None or pos + width > size:
            raise FormatError(f'Unsupported/invalid DEX opcode 0x{op:02x} at unit {pos}')
        ins = words[pos:pos+width]
        ref = None
        if op in (0xe3,0xe4,0xe5,0xe6,0xe7,0xe8,0xef,0xf0,0xf1,0xf2,0xf3,0xf4,0xf5,0xf6,0xf7,0xf8,0xe9,0xea):
            if used >= len(quick):
                raise FormatError('Not enough quickening indices')
            idx = quick[used]
            used += 1
            if op in (0xe9,0xea):
                owner, name, proto = dex.methods[idx]
                ref = f'{owner}->{name}'
            else:
                owner, name, typ = fields[idx]
                ref = f'{owner}->{name}'
        elif op in (0x1a,0x1b):
            idx = ins[1] if op == 0x1a else ins[1] | ins[2] << 16
            ref = dex.strings[idx]
        elif op in (0x6e,0x6f,0x70,0x71,0x72,0x74,0x75,0x76,0x77,0x78):
            owner, name, proto = dex.methods[ins[1]]
            ref = f'{owner}->{name}'
        elif op in (0x1c,0x22):
            ref = dex.types[ins[1]]
        elif op == 0x15:
            ref = ins[1] << 16
        events.append((pos, op, ref))
        pos += width
    if used != len(quick):
        raise FormatError('Not all quickening indices were consumed')
    return events, used


def analyze(vdex_path):
    raw = Path(vdex_path).read_bytes()
    print('VDEX SHA-256:', hashlib.sha256(raw).hexdigest())
    dex_bytes, quick_blob = vdex_sections(raw)
    dex = Dex(dex_bytes)
    fields = field_ids(dex)
    ctor, n_ctor = method_insns(dex, quick_blob, RECEIVER, '<init>', fields)
    recv, n_recv = method_insns(dex, quick_blob, RECEIVER, 'onReceive', fields)
    constructor = [ref for _,_,ref in ctor]
    references = [ref for _,_,ref in recv]
    calls = [ref for _,op,ref in recv if op in (0xe9,0xea,0x6e,0x6f,0x70,0x71,0x72,0x74,0x75,0x76,0x77,0x78)]
    expected_calls = [
        'Landroid/content/Intent;->getAction',
        'Ljava/lang/String;->equals',
        'Landroid/content/Intent;->getData',
        'Landroid/net/Uri;->getHost',
        'Ljava/lang/String;->equals',
        'Landroid/content/Intent;-><init>',
        'Landroid/content/Intent;->setClass',
        'Landroid/content/Intent;->setFlags',
        'Landroid/content/Context;->startActivity',
    ]
    checks = {
        'constructor initializes SECRETCODE with 2846': '2846' in constructor and RECEIVER+'->SECRETCODE' in constructor,
        'onReceive invokes expected APIs in order': calls == expected_calls,
        'action constant matches Telephony secret code': SECRET_ACTION in references,
        'checks SECRETCODE instance field': RECEIVER+'->SECRETCODE' in references,
        'targets MMI MainActivity': MMI_MAIN in references,
        'sets FLAG_ACTIVITY_NEW_TASK': 0x10000000 in references,
        'receiver has 2 conditional exits': sum(1 for _,op,_ in recv if op==0x38)==2,
        'quickening indices consumed (constructor + onReceive)': (n_ctor,n_recv)==(1,9),
    }
    for label, ok in checks.items():
        print(('PASS' if ok else 'FAIL')+': '+label)
    print(f'Quickening refs: constructor={n_ctor}/1; onReceive={n_recv}/9')
    print(f'Result: {sum(checks.values())}/{len(checks)} checks passed')
    print('Interpretation: MMI secret-code BroadcastReceiver checks action and host')
    print('  then opens MainActivity when both match. This is separate from')
    print('  the GlocalmeHome About-password -> AssistantActivity route.')
    print('No OEM code or extracted DEX saved.')
    return 0 if all(checks.values()) else 1


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('vdex', type=Path, help='Privately held MMI.vdex, version 010')
    args = parser.parse_args()
    if not args.vdex.is_file():
        parser.error('VDEX file not found')
    if args.vdex.stat().st_size > 100 * 1024 * 1024:
        parser.error('VDEX over 100 MiB not supported')
    try:
        return analyze(args.vdex)
    except (ValueError, IndexError, struct.error, OSError) as exc:
        print('ERROR:', exc, file=sys.stderr)
        return 2

if __name__ == '__main__':
    sys.exit(main())
