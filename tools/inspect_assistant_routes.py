#!/usr/bin/env python3
"""Static read-only audit of three OEM Assistant Function routes.

No ADB, root, network operations, APK export or firmware modification.
Findings are reference/opcode signatures, NOT runtime proofs or a full CFG.
Run: python tools/inspect_assistant_routes.py /path/to/GlocalmeHome.apk
"""
import argparse
import json
import sys
import zipfile
from pathlib import Path

from inspect_2846 import Dex

ASSISTANT = 'Lcom/glocalme/minilauncher/assistant/AssistantActivity;'
PKG_UTIL = 'Lcom/glocalme/common/util/PackageUtil;'
ROUTES = {
    'MMI': ('startMMI', 'com.ukelink.dusk.mmi',
            'com.ukelink.dusk.mmi.MainActivity', 'MMI is not installed'),
    'Log Tools': ('startLogTools', 'com.ucloudlink.feedback',
                  'com.ucloudlink.feedback.LogSettingActivity', 'Log Tools is not installed'),
    'System Settings': ('startSystemSettings', 'com.android.settings',
                        'com.android.settings.Settings', 'System Settings not installed'),
}


def ordered_symbols(items, required):
    """Conservative ordered-subsequence match over the target method's DEX refs."""
    refs = [ref for _, ref in items if ref is not None]
    idx = 0
    for expected in required:
        while idx < len(refs) and refs[idx] != expected:
            idx += 1
        if idx >= len(refs):
            return False
        idx += 1
    return True


def audit_dex(dex):
    package_check = list(dex.instructions(PKG_UTIL, 'isAppInstall'))
    package_info = list(dex.instructions(PKG_UTIL, 'getPackageInfo'))
    guard_verified = ordered_symbols(package_check, [PKG_UTIL+'->getPackageInfo']) and ordered_symbols(
        package_info, ['Landroid/content/pm/PackageManager;->getPackageInfo'])
    output = {}
    for label, (method, package, activity, fallback) in ROUTES.items():
        items = list(dex.instructions(ASSISTANT, method))
        good = ordered_symbols(items, [
            package, PKG_UTIL+'->isAppInstall',
            'Landroid/content/Intent;-><init>', package, activity,
            'Landroid/content/Intent;->setClassName',
            ASSISTANT+'->startActivity', fallback,
        ])
        output[label] = {
            'package': package, 'activity': activity,
            'signature_matches': bool(good and guard_verified),
            'scope': 'ordered references in target method; not full control-flow proof',
        }
    return output


def inspect(apk):
    if apk.stat().st_size > 100 * 1024 * 1024:
        raise ValueError('APK exceeds 100 MiB cap')
    with zipfile.ZipFile(apk) as z:
        dex = Dex(z.read('classes.dex'))
    return audit_dex(dex)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('apk', type=Path, help='Private local copy of GlocalmeHome.apk')
    ap.add_argument('--json', action='store_true', help='Machine-readable non-sensitive summary')
    opts = ap.parse_args(argv)
    if not opts.apk.is_file():
        ap.error('APK not found')
    try:
        results = inspect(opts.apk)
    except (OSError, KeyError, IndexError, ValueError, zipfile.BadZipFile) as e:
        print('ERROR:', e, file=sys.stderr)
        return 2
    if opts.json:
        print(json.dumps(results, ensure_ascii=False, indent=2))
    else:
        for name, item in results.items():
            print(('PASS' if item['signature_matches'] else 'FAIL') + ': ' + name +
                  ' -> ' + item['package'] + '/' + item['activity'])
        print('Offline signature audit only; NOT a test that the target package can launch.')
    return 0 if all(i['signature_matches'] for i in results.values()) else 1


if __name__ == '__main__':
    sys.exit(main())
