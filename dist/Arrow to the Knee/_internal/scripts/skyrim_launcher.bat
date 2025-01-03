@echo off
set SKYRIM_PATH="C:\Program Files (x86)\Steam\steamapps\common\Skyrim\SkyrimLauncher.exe"
set SKSE_PATH="C:\Program Files (x86)\Steam\steamapps\common\Skyrim\skse_loader.exe"

if exist %SKSE_PATH% (
    echo Launching Skyrim with SKSE...
    start "" %SKSE_PATH%
) else (
    echo SKSE not found. Launching Skyrim normally...
    start "" %SKYRIM_PATH%
)

pause
