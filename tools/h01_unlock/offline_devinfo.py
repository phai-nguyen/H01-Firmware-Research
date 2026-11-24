#!/usr/bin/env python3
"""Offline H01 DEVINFO candidate preparation/verification.

Derived from the November 2026 Notion H01 experiments. This tool NEVER
communicates with a phone, invokes EDL or writes any device partition.
It is NOT a universal OEM unlocker.
"""
import argparse
import hashlib
import json
import re
import struct
from pathlib import Path

SIZE = 1048576
OLD_MAGIC = b"ANDROID-BOOT!"
NEW_MAGIC = b"GLOCALME-BOOT"
EXPECTED_DIFFERENCES = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12)


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def valid_digest(value):
    if not re.fullmatch(r"[0-9a-fA-F]{64}", value):
        raise ValueError("An expected SHA-256 must contain 64 hexadecimal characters")
    return value.lower()


def checked_file(path, expected=None):
    data = Path(path).read_bytes()
    if len(data) != SIZE:
        raise ValueError("%s: expected 1048576 bytes" % path)
    digest = sha256(data)
    if expected is not None and digest != valid_digest(expected):
        raise ValueError("%s: SHA-256 does not match expected value" % path)
    return data


def prepare_candidate(original):
    """Patch only the OEM label, preserving all other bytes."""
    if len(original) != SIZE:
        raise ValueError("DEVINFO must be exactly 1048576 bytes")
    if original[:16] != OLD_MAGIC + b"\0\0\0":
        raise ValueError("DEVINFO header differs from the Notion H01 baseline")
    if struct.unpack_from("<I", original, 0x10)[0] != 0:
        raise ValueError("Unexpected initial unlocked field; refusing candidate")
    result = bytearray(original)
    result[:13] = NEW_MAGIC
    result = bytes(result)
    differences = tuple(i for i, pair in enumerate(zip(original, result))
                        if pair[0] != pair[1])
    if differences != EXPECTED_DIFFERENCES or result[13:] != original[13:]:
        raise ValueError("Unexpected changed bytes; refusing candidate")
    return result


def inspect(original, candidate):
    expected = prepare_candidate(original)
    if candidate != expected:
        raise ValueError("Candidate is not the 12-byte-only change documented in Notion")
    return {
        "size_bytes": SIZE,
        "changed_byte_count": 12,
        "original_sha256": sha256(original),
        "candidate_sha256": sha256(candidate),
        "offline_verified": True,
        "device_unlocked": False,
    }


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("mode", choices=["verify", "prepare"])
    p.add_argument("--devinfo", required=True, type=Path,
                   help="Original DEVINFO image read from THIS device")
    p.add_argument("--expected-devinfo", required=True,
                   help="Independent SHA-256 of original image")
    p.add_argument("--aboot", required=True, type=Path,
                   help="Matching ABOOT from the same device")
    p.add_argument("--expected-aboot", required=True,
                   help="Independently verified SHA-256 for ABOOT")
    p.add_argument("--candidate", required=True, type=Path,
                   help="Candidate file to check or offline output to create")
    p.add_argument("--confirm", default="",
                   help="For prepare only: enter PREPARE-MY-OWN-H01")
    args = p.parse_args(argv)

    original = checked_file(args.devinfo, args.expected_devinfo)
    aboot = checked_file(args.aboot, args.expected_aboot)
    # Matching a caller-supplied hash proves integrity against that reference,
    # NOT that the ABOOT implementation supports the GlocalMe metadata branch.
    if not aboot.startswith(b"\x7fELF"):
        raise ValueError("ABOOT is not ELF; firmware implementation not verified")

    if args.mode == "prepare":
        if args.confirm != "PREPARE-MY-OWN-H01":
            raise ValueError("Explicit confirmation required for candidate generation")
        if args.candidate.exists():
            raise ValueError("Refusing to overwrite a candidate file")
        result = prepare_candidate(original)
        args.candidate.parent.mkdir(parents=True, exist_ok=True)
        with args.candidate.open("xb") as out:
            out.write(result)
    candidate = checked_file(args.candidate)
    report = inspect(original, candidate)
    report["aboot_sha256"] = sha256(aboot)
    print(json.dumps(report, indent=2))
    print("NO DEVICE WRITE. Candidate is not an authorization to flash.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError) as e:
        raise SystemExit("FAIL: " + str(e))
