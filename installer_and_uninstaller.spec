# installer_and_uninstaller.spec
# -*- mode: python ; coding: utf-8 -*-

import os

block_cipher = None

# Analysis for Installer
a_installer = Analysis(
    ['installer.py'],
    pathex=['.'],
    binaries=[],
    datas=[
        ('Data/scripts/EldenRingArrowInTheKnee.esp', 'Data/scripts'),
        ('Data/scripts/config.txt', 'Data/scripts'),
        ('audio/arrow_to_knee.mp3', 'audio'),
        ('scripts/elden_ring/Arrow_knee_detection.lua', 'scripts/elden_ring'),
        ('scripts/elden_ring/Arrow_knee_detection.luac', 'scripts/elden_ring'),
        ('scripts/elden_ring/Save_management.lua', 'scripts/elden_ring'),
        ('scripts/elden_ring/Save_management.luac', 'scripts/elden_ring'),
        ('scripts/elden_ring/Skyrim_transition.lua', 'scripts/elden_ring'),
        ('scripts/elden_ring/Skyrim_transition.luac', 'scripts/elden_ring'),
        ('scripts/skyrim_launcher.bat', 'scripts')
    ],
    hiddenimports=[],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
)
pyz_installer = PYZ(a_installer.pure, a_installer.zipped_data, cipher=block_cipher)
exe_installer = EXE(
    pyz_installer,
    a_installer.scripts,
    [],
    exclude_binaries=True,
    name='Arrow to the Knee (1.0) Installer',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    icon='icon.ico'  # Icon file for installer
)

# Analysis for Uninstaller
a_uninstaller = Analysis(
    ['uninstall.py'],
    pathex=['.'],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
)
pyz_uninstaller = PYZ(a_uninstaller.pure, a_uninstaller.zipped_data, cipher=block_cipher)
exe_uninstaller = EXE(
    pyz_uninstaller,
    a_uninstaller.scripts,
    [],
    exclude_binaries=True,
    name='Arrow to the Knee Uninstaller',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    icon='icon.ico'  # Icon file for uninstaller
)

coll = COLLECT(
    exe_installer,
    exe_uninstaller,
    a_installer.binaries,
    a_installer.zipfiles,
    a_installer.datas,
    a_uninstaller.binaries,
    a_uninstaller.zipfiles,
    a_uninstaller.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='Arrow to the Knee',
    distpath='dist',  # Output directory for the executables
    workpath='build',  # Build directory
    tempdir='temp'     # Temporary directory
)
