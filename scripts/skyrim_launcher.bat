@echo off
REM Skyrim Launcher Batch File for Elden Ring x Skyrim Crossover Joke Mod

REM Set the path to the Skyrim executable
set SKYRIM_PATH="C:\Program Files (x86)\Steam\steamapps\common\Skyrim\SkyrimLauncher.exe"

REM Optional: Set the path to SKSE executable if using SKSE
set SKSE_PATH="C:\Program Files (x86)\Steam\steamapps\common\Skyrim\skse_loader.exe"

REM Check if SKSE is installed and launch Skyrim with SKSE
if exist %SKSE_PATH% (
    echo Launching Skyrim with SKSE...
    start "" %SKSE_PATH%
) else (
    echo SKSE not found. Launching Skyrim normally...
    start "" %SKYRIM_PATH%
)

pause
