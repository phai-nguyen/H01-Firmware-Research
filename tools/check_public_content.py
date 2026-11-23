#!/usr/bin/env python3
"""Basic, deliberately conservative pre-publication scan.

This is not a secret scanner and does not establish redistribution rights.
Run from repository root: python tools/check_public_content.py
"""
from pathlib import Path
import re, subprocess, sys

ROOT = Path(__file__).resolve().parents[1]
DENIED_SUFFIXES = {'.img','.bin','.mbn','.elf','.apk','.apks','.odex','.vdex','.dex','.so','.ko',
                   '.jar','.zip','.rar','.7z','.gz','.xz','.tar','.pdf','.jpg','.jpeg','.png',
                   '.mp4','.mov','.log','.pcap','.pcapng','.key','.pem','.p12','.pfx','.jks',
                   '.bks','.db','.sqlite','.sqlite3'}
MAX_BYTES = 1024 * 1024
PATTERNS = [
    ('private key', re.compile(r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----')),
    ('credential assignment', re.compile(r'(?i)\b(?:deviceSecret|api[_-]?key|access[_-]?token|password)\s*[:=]\s*["\']?[A-Za-z0-9_+/.-]{12,}')),
    ('possibly unredacted IMEI/IMSI', re.compile(r'(?<![A-Za-z0-9])\d{15}(?![A-Za-z0-9])')),
]

def list_files():
    try:
        result = subprocess.run(['git', '-C', str(ROOT), 'ls-files', '-z'],
                                capture_output=True, check=True)
        if result.stdout:
            return [ROOT / p.decode('utf-8') for p in result.stdout.split(b'\0') if p]
    except (OSError, subprocess.CalledProcessError):
        pass
    return [p for p in ROOT.rglob('*') if p.is_file() and '.git' not in p.parts]

def main():
    errors = []
    items = list_files()
    for p in items:
        rel = p.relative_to(ROOT).as_posix()
        if not p.exists():
            continue
        if p.suffix.lower() in DENIED_SUFFIXES or p.name.startswith('.env'):
            errors.append(f'{rel}: blocked file type')
            continue
        if p.stat().st_size > MAX_BYTES:
            errors.append(f'{rel}: exceeds 1 MiB (manual review needed)')
            continue
        try:
            data = p.read_text(encoding='utf-8')
        except (UnicodeError, OSError):
            errors.append(f'{rel}: not readable UTF-8 text')
            continue
        for name, rx in PATTERNS:
            if rx.search(data):
                errors.append(f'{rel}: {name} pattern (manual review needed)')
    if errors:
        for err in errors:
            print('BLOCK:', err)
        return 1
    print(f'Basic file scan passed: {len(items)} text files. MANUAL REVIEW STILL REQUIRED.')
    return 0

if __name__ == '__main__':
    sys.exit(main())
