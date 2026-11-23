# ZEUS H01 Open Firmware Research

An independent, community-oriented research project documenting the **ZEUS H01 / GlocalMe K1** hardware and its Android 8.1 firmware, boot chain, EDL/Fastboot, OTA, SIM architecture, hidden services and companion applications.

**Release v0.2.0 adds a sanitized GPT layout and host-side read-only tools**, not an official firmware image, recovery ROM or guaranteed flashing procedure. Observations refer to particular hardware/firmware snapshots.

## Highlights

- Qualcomm MSM8909 / ARMv7, Android 8.1 (API 27).
- A lab report dated 2026-11-18 records an unlocked bootloader and Magisk root on a test unit.
- A report dated 2026-11-22 documents a verified **incremental OTA, build 81 → 87**, 44,118,207 bytes; it is **not** a full factory image.
- DSDS property and two logical radio channels observed; simultaneous two physical SIM operation is **not** yet verified.
- AutoHotspot v0.4 reportedly passed after reboot; audio output recovery remains **unresolved and paused**.

Browse the Vietnamese [main README](README.md), [research status](docs/research/status.md), [source provenance](docs/research/provenance.md), and [publication policy](docs/security/publication-policy.md).

## v0.2.0 tools

- [Sanitized 42-partition GPT map](docs/firmware/gpt-layout.md) (no per-device GUIDs, not a flashing recipe).
- [ADB read-only survey guide](docs/tools/read-only-report.md) for Windows 7 and Linux/antiX.
- [Offline SHA-256 verifier](docs/tools/backup-hashes.md) for independently held backups.
- Basic checks: `python3 -m unittest discover -s tests -v`. These tools were unit-tested with synthetic data, not validated as a recovery workflow.

## License & contributions

Original scripts/code: MIT ([LICENSE](LICENSE)); independently authored documentation: CC BY 4.0 ([LICENSE-DOCS.md](LICENSE-DOCS.md)). Vendor firmware, apps, copyrighted logos, keys and device data are **not redistributed or relicensed**. Contributions welcome via issues and pull requests under [CONTRIBUTING.md](CONTRIBUTING.md). This project is not affiliated with the vendors.
