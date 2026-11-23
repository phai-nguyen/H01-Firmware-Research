#!/usr/bin/env python3
"""Read-only ZIP/IMG backup audit. Transport integrity != restorable firmware."""
import argparse
from dataclasses import dataclass
import hashlib
from pathlib import Path, PurePosixPath
import re
import sys
from zipfile import ZipFile, BadZipFile, LargeZipFile

CHUNK = 1024 * 1024
MAX_MEMBERS = 4096
MAX_ZIP_UNCOMPRESSED = 24 * 1024**3
MAX_SIDECAR = 4096
SIDECAR = re.compile(rb"([0-9a-fA-F]{64}) [ *]([^\r\n]+)")


@dataclass
class Result:
    archives: int = 0
    crc_pass: int = 0
    images: int = 0
    match: int = 0
    review: int = 0
    mismatch: int = 0
    error: int = 0

    def exit_code(self):
        if self.error or self.mismatch or not self.images:
            return 2
        return 1 if self.review else 0


def valid_name(name):
    """Reject paths with traversal or platform-specific separators."""
    return (bool(name) and not name.startswith("/") and "\\" not in name
            and ":" not in name and "\0" not in name
            and all(x not in ("", ".", "..") for x in name.split("/")))


def parse_sidecar(data, basename):
    if len(data) > MAX_SIDECAR:
        raise ValueError("large sidecar")
    match = SIDECAR.fullmatch(data.strip(b"\r\n"))
    if match is None:
        raise ValueError("malformed sha256sum record")
    digest, filename = match.groups()
    try:
        name = filename.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise ValueError("invalid filename encoding") from exc
    if name != basename or not valid_name(name) or "/" in name:
        raise ValueError("sha256sum filename mismatch")
    return digest.decode("ascii").lower()


def digest_stream(stream):
    h = hashlib.sha256()
    while True:
        data = stream.read(CHUNK)
        if not data:
            return h.hexdigest()
        h.update(data)


def note(enabled, msg):
    if enabled:
        print(msg)


def audit_zip(path, result, verbose=False):
    result.archives += 1
    if path.is_symlink() or not path.is_file():
        result.error += 1
        return
    try:
        with ZipFile(path, "r") as archive:
            infos = archive.infolist()
            if len(infos) > MAX_MEMBERS:
                raise ValueError("too many entries")
            members, total = {}, 0
            for info in infos:
                if info.is_dir():
                    continue
                name = info.filename
                if not valid_name(name) or name in members or info.flag_bits & 1:
                    raise ValueError("unsafe, duplicate or encrypted member")
                total += info.file_size
                if total > MAX_ZIP_UNCOMPRESSED:
                    raise ValueError("oversized archive")
                if name.lower().endswith(".sha256") and info.file_size > MAX_SIDECAR:
                    raise ValueError("oversized sidecar")
                members[name] = info
            img_names = [name for name in members if name.lower().endswith(".img")]
            result.images += len(img_names)
            hashes, sidecars = {}, {}
            for name, info in members.items():
                with archive.open(info) as stream:
                    if name in img_names:
                        hashes[name] = digest_stream(stream)
                    elif name.lower().endswith(".sha256"):
                        sidecars[name] = stream.read(MAX_SIDECAR + 1)
                        if len(sidecars[name]) > MAX_SIDECAR:
                            raise ValueError("oversized sidecar")
                    else:
                        while stream.read(CHUNK):
                            pass
            # Every ZIP member was read to EOF, so zipfile checked its CRC.
            result.crc_pass += 1
            for name in img_names:
                sidecar = sidecars.get(name + ".sha256")
                if sidecar is None:
                    result.review += 1
                    note(verbose, "REVIEW: ZIP image has no paired sidecar")
                    continue
                try:
                    expected = parse_sidecar(sidecar, PurePosixPath(name).name)
                except ValueError:
                    result.error += 1
                    note(verbose, "ERROR: invalid ZIP sidecar")
                    continue
                if expected == hashes[name]:
                    result.match += 1
                    note(verbose, "MATCH: ZIP image checksum")
                else:
                    result.mismatch += 1
                    note(verbose, "MISMATCH: ZIP image checksum")
    except (OSError, ValueError, RuntimeError, EOFError, BadZipFile, LargeZipFile) as exc:
        result.error += 1
        note(verbose, "ERROR: ZIP structure/read/CRC failed ({})".format(type(exc).__name__))


def audit_image(path, result, verbose=False):
    result.images += 1
    if path.is_symlink() or not path.is_file():
        result.error += 1
        return
    sidecar = path.with_name(path.name + ".sha256")
    if not sidecar.exists():
        result.review += 1
        note(verbose, "REVIEW: standalone image has no sidecar")
        return
    if sidecar.is_symlink() or not sidecar.is_file():
        result.error += 1
        return
    try:
        if sidecar.stat().st_size > MAX_SIDECAR:
            raise ValueError("oversized sidecar")
        expected = parse_sidecar(sidecar.read_bytes(), path.name)
        with path.open("rb") as stream:
            actual = digest_stream(stream)
        if expected == actual:
            result.match += 1
            note(verbose, "MATCH: standalone image checksum")
        else:
            result.mismatch += 1
            note(verbose, "MISMATCH: standalone image checksum")
    except (OSError, ValueError):
        result.error += 1
        note(verbose, "ERROR: image or sidecar unreadable/invalid")


def audit_folder(root, verbose=False):
    report = Result()
    if root.is_symlink() or not root.is_dir():
        report.error += 1
        return report
    try:
        entries = sorted(root.iterdir(), key=lambda item: item.name.lower())
    except OSError:
        report.error += 1
        return report
    for entry in entries:
        if entry.suffix.lower() == ".zip":
            audit_zip(entry, report, verbose)
        elif entry.suffix.lower() == ".img":
            audit_image(entry, report, verbose)
    return report


def main(argv=None):
    parser = argparse.ArgumentParser(description="Offline ZIP/IMG integrity audit, no extraction")
    parser.add_argument("folder", type=Path)
    parser.add_argument("--details", action="store_true",
                        help="Show status categories, never raw hashes or data")
    args = parser.parse_args(argv)
    r = audit_folder(args.folder, args.details)
    print("ZIP: {} (CRC OK: {})".format(r.archives, r.crc_pass))
    print("IMG: {} | MATCH: {} | REVIEW: {} | MISMATCH: {} | ERROR: {}".format(
        r.images, r.match, r.review, r.mismatch, r.error))
    print("No OEM signature, GPT coverage, physical LBA or restore safety is verified.")
    return r.exit_code()


if __name__ == "__main__":
    sys.exit(main())
