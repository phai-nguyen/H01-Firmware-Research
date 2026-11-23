#!/usr/bin/env python3
"""Compare the observed GlocalmeHome 2846 path across two privately held APKs.

Read-only: no ADB, root, network, APK modifications or OEM bytecode export.
Run beside inspect_2846.py, Python >=3.8.
"""
import argparse
import hashlib
import json
import sys
import zipfile
from pathlib import Path

from inspect_2846 import Dex

TARGETS = (
    ('MiniAboutActivity.startAssistantFunction',
     'Lcom/glocalme/minilauncher/about/MiniAboutActivity;', 'startAssistantFunction'),
    ('MiniAboutActivity$5.onClick',
     'Lcom/glocalme/minilauncher/about/MiniAboutActivity$5;', 'onClick'),
    ('AssistantActivity.startMMI',
     'Lcom/glocalme/minilauncher/assistant/AssistantActivity;', 'startMMI'),
    ('AssistantActivity.startLogTools',
     'Lcom/glocalme/minilauncher/assistant/AssistantActivity;', 'startLogTools'),
    ('AssistantActivity.startSystemSettings',
     'Lcom/glocalme/minilauncher/assistant/AssistantActivity;', 'startSystemSettings'),
)
LAYOUTS = ('res/layout/about_settings_activity.xml', 'res/layout/assistant_activity.xml')
DEX_NAMES = ('classes.dex', 'classes2.dex', 'classes3.dex')
MAX_APK_BYTES = 100 * 1024 * 1024
MAX_UNCOMPRESSED_DEX_BYTES = 32 * 1024 * 1024


def sha256_bytes(data):
    return hashlib.sha256(data).hexdigest()


def normalized_method_signature(instructions):
    """Digest opcode order + decoded string/method refs, not an identical bytecode claim."""
    normalized = [[op, ref] for op, ref in instructions]
    encoded = json.dumps(normalized, ensure_ascii=False, separators=(',', ':')).encode('utf-8')
    return {'instruction_count': len(normalized), 'digest': sha256_bytes(encoded)}


def get_binary(z, name):
    info = z.getinfo(name)
    if info.file_size > MAX_UNCOMPRESSED_DEX_BYTES:
        raise ValueError(f'APK entry too large: {name}')
    return z.read(info)


def inspect(path):
    if not path.is_file() or path.stat().st_size > MAX_APK_BYTES:
        raise ValueError(f'Input must be an APK file smaller than 100 MiB: {path}')
    result = {'file_name': path.name, 'apk_sha256': sha256_bytes(path.read_bytes()),
              'dex_sha256': {}, 'layout_sha256': {}, 'methods': {}}
    with zipfile.ZipFile(path) as z:
        for n in DEX_NAMES:
            if n in z.namelist():
                result['dex_sha256'][n] = sha256_bytes(get_binary(z, n))
        if 'classes.dex' not in result['dex_sha256']:
            raise ValueError(f'No classes.dex in {path.name}')
        dex = Dex(get_binary(z, 'classes.dex'))
        for name, owner, method in TARGETS:
            result['methods'][name] = normalized_method_signature(list(dex.instructions(owner, method)))
        for n in LAYOUTS:
            result['layout_sha256'][n] = sha256_bytes(get_binary(z, n))
    return result


def compare_results(a, b):
    method_names = sorted(set(a['methods']) | set(b['methods']))
    methods = {n: a['methods'].get(n) == b['methods'].get(n) for n in method_names}
    dex_names = sorted(set(a['dex_sha256']) | set(b['dex_sha256']))
    dex = {n: a['dex_sha256'].get(n) == b['dex_sha256'].get(n) for n in dex_names}
    layouts = {n: a['layout_sha256'].get(n) == b['layout_sha256'].get(n)
               for n in sorted(set(a['layout_sha256']) | set(b['layout_sha256']))}
    return {'identical_apk': a['apk_sha256'] == b['apk_sha256'],
            'methods_semantically_matching': methods,
            'dex_byte_identical': dex, 'layout_byte_identical': layouts}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('apk_a', type=Path)
    parser.add_argument('apk_b', type=Path)
    parser.add_argument('--json', action='store_true', help='Output bounded metadata as JSON, not OEM content')
    args = parser.parse_args(argv)
    try:
        first, second = inspect(args.apk_a), inspect(args.apk_b)
        report = compare_results(first, second)
    except (OSError, ValueError, KeyError, IndexError, zipfile.BadZipFile) as exc:
        print('ERROR:', str(exc), file=sys.stderr)
        return 2
    if args.json:
        print(json.dumps({'a': first, 'b': second, 'comparison': report}, indent=2))
    else:
        print(f'APK A: {first["file_name"]} ({first["apk_sha256"][:16]}...)')
        print(f'APK B: {second["file_name"]} ({second["apk_sha256"][:16]}...)')
        print('APK byte-identical:', 'YES' if report['identical_apk'] else 'NO')
        for n, equal in report['dex_byte_identical'].items():
            print('DEX', n, ':', 'SAME' if equal else 'DIFFERENT')
        for n, equal in report['layout_byte_identical'].items():
            print('Layout', n, ':', 'SAME' if equal else 'DIFFERENT')
        for n, equal in report['methods_semantically_matching'].items():
            print('2846-method', n, ':', 'MATCH' if equal else 'DIFFERENT')
        print('Note: MATCH compares selected opcode/reference signatures, not complete control flow.')
        print('A modified/repackaged APK is NOT proof of a different OEM firmware build.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
