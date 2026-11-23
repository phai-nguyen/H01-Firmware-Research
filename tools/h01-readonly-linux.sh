#!/bin/sh
# ZEUS H01: host-side allowlisted ADB queries. No flash/root/write to device.
set -u
ADB=${ADB:-adb}
if ! command -v "$ADB" >/dev/null 2>&1; then
    echo 'ERROR: adb not found in PATH' >&2
    exit 2
fi
if ! "$ADB" get-state >/dev/null 2>&1; then
    echo 'ERROR: connect one authorized H01 ADB device' >&2
    exit 2
fi
OUTDIR=${1:-./H01-READONLY-RESULTS}
if ! mkdir -p "$OUTDIR"; then
    echo 'ERROR: unable to create output directory' >&2
    exit 2
fi
REPORT=$OUTDIR/report.txt
{
    printf 'ZEUS H01 READ-ONLY SURVEY\nScope: allowlisted host-side ADB reads. Manually redact before sharing.\n\n'
    printf '==== ANDROID BUILD ====\n'
    "$ADB" shell getprop ro.build.version.release
    "$ADB" shell getprop ro.build.version.sdk
    "$ADB" shell getprop ro.product.device
    "$ADB" shell getprop ro.board.platform
    "$ADB" shell getprop ro.product.cpu.abi
    "$ADB" shell getprop ro.fota.version
    printf '\n==== BOOT STATUS ====\n'
    "$ADB" shell getprop ro.boot.flash.locked
    "$ADB" shell getprop ro.boot.verifiedbootstate
    "$ADB" shell id
    printf '\n==== STORAGE NAMES AND SIZES - NOT A DUMP ====\n'
    "$ADB" shell cat /proc/partitions
    printf '\n==== RADIO STATE - NO IDENTIFIERS ====\n'
    "$ADB" shell getprop persist.radio.multisim.config
    "$ADB" shell getprop gsm.sim.state
    "$ADB" shell getprop init.svc.ril-daemon
    "$ADB" shell getprop init.svc.ril-daemon2
    printf '\n==== DISPLAY READ-ONLY ====\n'
    "$ADB" shell wm size
    "$ADB" shell wm density
    printf '\n==== AUDIO READ-ONLY ====\n'
    "$ADB" shell cat /proc/asound/cards
    "$ADB" shell ls -l /dev/snd
} > "$REPORT" 2>&1
printf 'Saved: %s\nReview and redact before publication.\n' "$REPORT"
