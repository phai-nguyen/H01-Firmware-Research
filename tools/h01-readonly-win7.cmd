@echo off
setlocal EnableExtensions DisableDelayedExpansion
rem ZEUS H01: no flash, no install, no root, no full getprop dump.
set "ADB=adb"
if exist "%~dp0adb.exe" set "ADB=%~dp0adb.exe"
where "%ADB%" >nul 2>&1
if errorlevel 1 (
  echo ERROR: adb.exe not found. Put this script beside adb.exe or add adb to PATH.
  exit /b 2
)
"%ADB%" get-state >nul 2>&1
if errorlevel 1 (
  echo ERROR: ADB device not ready. Connect one authorized H01.
  exit /b 2
)
set "OUTDIR=%~dp0H01-READONLY-RESULTS"
if not "%~1"=="" set "OUTDIR=%~f1"
if not exist "%OUTDIR%" mkdir "%OUTDIR%"
if errorlevel 1 (
  echo ERROR: Cannot create output directory.
  exit /b 2
)
set "REPORT=%OUTDIR%\report.txt"
(
 echo ZEUS H01 READ-ONLY SURVEY
 echo Scope: allowlisted host-side ADB reads only. Manually redact before sharing.
 echo.
 echo ==== ANDROID BUILD ====
 "%ADB%" shell getprop ro.build.version.release
 "%ADB%" shell getprop ro.build.version.sdk
 "%ADB%" shell getprop ro.product.device
 "%ADB%" shell getprop ro.board.platform
 "%ADB%" shell getprop ro.product.cpu.abi
 "%ADB%" shell getprop ro.fota.version
 echo.
 echo ==== BOOT STATUS ====
 "%ADB%" shell getprop ro.boot.flash.locked
 "%ADB%" shell getprop ro.boot.verifiedbootstate
 "%ADB%" shell id
 echo.
 echo ==== STORAGE NAMES AND SIZES - NOT A DUMP ====
 "%ADB%" shell cat /proc/partitions
 echo.
 echo ==== RADIO STATE - NO IDENTIFIERS ====
 "%ADB%" shell getprop persist.radio.multisim.config
 "%ADB%" shell getprop gsm.sim.state
 "%ADB%" shell getprop init.svc.ril-daemon
 "%ADB%" shell getprop init.svc.ril-daemon2
 echo.
 echo ==== DISPLAY READ-ONLY ====
 "%ADB%" shell wm size
 "%ADB%" shell wm density
 echo.
 echo ==== AUDIO READ-ONLY ====
 "%ADB%" shell cat /proc/asound/cards
 "%ADB%" shell ls -l /dev/snd
) > "%REPORT%" 2>&1
if errorlevel 1 (
  echo NOTICE: Some properties or paths may be unavailable. Review the report.
)
echo Report saved: "%REPORT%"
echo WARNING: Review and redact report before publishing.
exit /b 0
