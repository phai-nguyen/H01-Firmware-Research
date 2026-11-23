@echo off
setlocal EnableExtensions DisableDelayedExpansion
rem ZEUS H01 Assistant Function: READ ONLY. No pm enable, root, logcat, flash or launch.
set "ADB=adb"
if exist "%~dp0adb.exe" set "ADB=%~dp0adb.exe"
where "%ADB%" >nul 2>&1
if errorlevel 1 (
 echo ERROR: adb.exe not found. Place this file next to adb.exe or add it to PATH.
 exit /b 2
)
"%ADB%" get-state >nul 2>&1
if errorlevel 1 (
 echo ERROR: Connect one authorized H01 via ADB.
 exit /b 2
)
set "OUTDIR=%~dp0H01-ASSISTANT-RESULTS"
if not exist "%OUTDIR%" mkdir "%OUTDIR%"
(
 echo ZEUS H01 - Assistant Function package status - read only
 echo NOTE: pm package visibility can vary by user/profile.
 echo.
 echo === GlocalmeHome ===
 "%ADB%" shell pm path com.glocalme.g4home
 echo === MMI ===
 "%ADB%" shell pm path com.ukelink.dusk.mmi
 echo === Feedback Log Tools ===
 "%ADB%" shell pm path com.ucloudlink.feedback
 echo === Android Settings ===
 "%ADB%" shell pm path com.android.settings
 echo.
 echo === Disabled Feedback package match ===
 "%ADB%" shell pm list packages -d com.ucloudlink.feedback
 echo === Available Feedback package match ===
 "%ADB%" shell pm list packages com.ucloudlink.feedback
) > "%OUTDIR%\01-package-status.txt" 2>&1
(
 echo === Feedback: allowlisted diagnostic lines ===
 "%ADB%" shell dumpsys package com.ucloudlink.feedback ^| findstr /I /C:"LogSettingActivity" /C:"enabled=" /C:"hidden=" /C:"User 0:"
) > "%OUTDIR%\02-feedback-state.txt" 2>&1
(
 echo === Foreground Activity, only selected lines ===
 "%ADB%" shell dumpsys activity activities ^| findstr /I /C:"mResumedActivity" /C:"mLastPausedActivity"
) > "%OUTDIR%\03-foreground.txt" 2>&1
echo Files in "%OUTDIR%"
echo No packages were enabled or changed; no modem logs were started.
echo Review output and redact device details before publication.
endlocal
