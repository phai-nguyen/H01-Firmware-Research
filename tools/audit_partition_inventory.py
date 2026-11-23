#!/usr/bin/env python3
"""Metadata-only inventory of H01 GPT partition IMG backups (read-only)."""
import argparse
import csv
from dataclasses import dataclass, field
from pathlib import Path, PurePosixPath
import re
import sys
from zipfile import ZipFile, BadZipFile

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_GPT = ROOT / "docs/firmware/partition-layout-sanitized.csv"
COLUMNS = ["index", "name", "start_lba", "end_lba", "sectors", "size_bytes"]
IMG_NAME = re.compile(r"^H01-([A-Za-z0-9]+)-([0-9]{8})\.img$")


@dataclass
class Coverage:
    expected: int = 0
    found: set = field(default_factory=set)
    missing: set = field(default_factory=set)
    size_disagreement: set = field(default_factory=set)
    variants: int = 0
    ignored: int = 0
    errors: int = 0

    def exit_code(self):
        return 2 if self.errors else (1 if self.missing else 0)


def load_gpt(path):
    if path.is_symlink() or not path.is_file():
        raise ValueError("CSV source missing/symlink")
    with path.open(encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames != COLUMNS:
            raise ValueError("unexpected CSV columns")
        rows = list(reader)
    if not rows:
        raise ValueError("empty GPT table")
    result = {}
    previous_end = -1
    for i, row in enumerate(rows, 1):
        try:
            index, start, end, sectors, size = (
                int(row[k]) for k in ("index", "start_lba", "end_lba", "sectors", "size_bytes")
            )
        except (TypeError, ValueError) as exc:
            raise ValueError("non-integer GPT data") from exc
        name = row["name"]
        if (index != i or not name or name in result or start <= previous_end
                or end < start or sectors != end - start + 1
                or size != sectors * 512):
            raise ValueError("inconsistent GPT row")
        result[name] = size
        previous_end = end
    return result


def audit(folder, gpt):
    report = Coverage(expected=len(gpt))
    if folder.is_symlink() or not folder.is_dir():
        report.errors += 1
        return report
    candidates = {}
    try:
        entries = list(folder.iterdir())
    except OSError:
        report.errors += 1
        return report
    for path in entries:
        if path.suffix.lower() == ".img":
            if path.is_symlink() or not path.is_file():
                report.errors += 1
                continue
            candidates[path.name] = (path.stat().st_size, "file")
        elif path.suffix.lower() == ".zip":
            if path.is_symlink() or not path.is_file():
                report.errors += 1
                continue
            try:
                with ZipFile(path) as z:
                    for member in z.infolist():
                        if member.is_dir():
                            continue
                        if (".." in member.filename.split("/") or
                                member.filename.startswith("/") or "\\" in member.filename):
                            report.errors += 1
                            continue
                        name = PurePosixPath(member.filename).name
                        if IMG_NAME.fullmatch(name):
                            # ZIP header length is metadata: NOT a verified IMG read.
                            candidates[(path.name, member.filename)] = (member.file_size, "zip")
            except (BadZipFile, OSError):
                report.errors += 1
    seen = set()
    for entry, (size, origin) in candidates.items():
        basename = entry if isinstance(entry, str) else PurePosixPath(entry[1]).name
        match = IMG_NAME.fullmatch(basename)
        if not match or match.group(1) not in gpt:
            report.ignored += 1
            continue
        part = match.group(1)
        report.variants += 1
        seen.add(part)
        if size == gpt[part]:
            report.found.add(part)
        else:
            report.size_disagreement.add(part)
    report.missing = set(gpt) - report.found
    return report


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Check partition-name and size coverage from IMG/ZIP metadata only"
    )
    parser.add_argument("folder", type=Path, help="One directory of ZIP/IMG backups")
    parser.add_argument("--gpt", type=Path, default=DEFAULT_GPT, help="Sanitized GPT CSV")
    parser.add_argument("--details", action="store_true", help="Print partition names only")
    args = parser.parse_args(argv)
    try:
        gpt = load_gpt(args.gpt)
    except (OSError, ValueError) as exc:
        print("ERROR: invalid GPT CSV ({})".format(type(exc).__name__))
        return 2
    r = audit(args.folder, gpt)
    print("Partition candidates of expected {}: {}".format(r.expected, len(r.found)))
    print("Missing/size-unverified: {} | Size disagreement: {} | Variants: {} | Ignored: {} | Errors: {}".format(
        len(r.missing), len(r.size_disagreement), r.variants, r.ignored, r.errors))
    if args.details:
        print("Missing/size-unverified names: {}".format(", ".join(sorted(r.missing)) or "(none)"))
        print("Size disagreement names: {}".format(", ".join(sorted(r.size_disagreement)) or "(none)"))
    print("ZIP lengths are header metadata, not verified IMG bytes. NOT a restore audit.")
    return r.exit_code()


if __name__ == "__main__":
    sys.exit(main())
