#!/usr/bin/env python3
"""Offline H01 backup sidecar verifier. Does not write to device or source files."""
import argparse
import hashlib
from pathlib import Path
import re
import sys

LINE = re.compile(r"^([0-9a-fA-F]{64}) [ *]([^\r\n]+)$")
CHUNK_SIZE = 1024 * 1024


def verify(sidecar):
    """Return (ok, result). Reject paths/symlinks in user-supplied sidecars."""
    sidecar = Path(sidecar)
    if sidecar.is_symlink() or not sidecar.is_file() or sidecar.suffix.lower() != ".sha256":
        return False, "ERROR: invalid sidecar: {}".format(sidecar.name)
    try:
        content = sidecar.read_text(encoding="ascii").strip("\r\n")
    except (OSError, UnicodeError):
        return False, "ERROR: unreadable sidecar: {}".format(sidecar.name)
    match = LINE.fullmatch(content)
    if not match:
        return False, "ERROR: malformed sidecar: {}".format(sidecar.name)
    expected, filename = match.groups()
    if (filename in ("", ".", "..") or filename != Path(filename).name
            or "/" in filename or "\\" in filename or ":" in filename):
        return False, "ERROR: unsafe filename in sidecar: {}".format(sidecar.name)
    image = sidecar.parent / filename
    if image.is_symlink() or not image.is_file():
        return False, "ERROR: missing or symlinked source: {}".format(filename)
    digest = hashlib.sha256()
    try:
        with image.open("rb") as stream:
            while True:
                chunk = stream.read(CHUNK_SIZE)
                if not chunk:
                    break
                digest.update(chunk)
    except OSError:
        return False, "ERROR: unable to read: {}".format(filename)
    if digest.hexdigest().lower() != expected.lower():
        return False, "MISMATCH: {}".format(filename)
    return True, "PASS: {}".format(filename)


def main(argv=None):
    parser = argparse.ArgumentParser(description="Verify H01 backups offline using SHA256sum sidecar files")
    parser.add_argument("sidecars", nargs="+", help="One or more .sha256 files beside their original files")
    args = parser.parse_args(argv)
    failures = 0
    for name in args.sidecars:
        ok, status = verify(name)
        print(status)
        failures += not ok
    return 0 if not failures else 1


if __name__ == "__main__":
    sys.exit(main())
