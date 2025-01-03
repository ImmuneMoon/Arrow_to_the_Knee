# installer.spec
# -*- mode: python ; coding: utf-8 -*-

import os
from pathlib import Path

# Define the base path of your project directory
project_base = Path("E:/Files/elden ring - arrow to the knee mod/Arrow_to_the_Knee").resolve()

block_cipher = None

a = Analysis(
    [str(project_base / 'installer.py')],
    pathex=[str(project_base)],
    binaries=[],
    datas=[
        (str(project_base / 'Data/scripts/EldenRingArrowInTheKnee.esp'), 'Data/scripts'),
        (str(project_base / 'Data/scripts/config.txt'), 'Data/scripts'),
        (str(project_base / 'audio/arrow_to_knee.mp3'), 'audio'),
        (str(project_base / 'scripts/elden_ring/Arrow_knee_detection.lua'), 'scripts/elden_ring'),
        (str(project_base / 'scripts/elden_ring/Arrow_knee_detection.luac'), 'scripts/elden_ring'),
        (str(project_base / 'scripts/elden_ring/Save_management.lua'), 'scripts/elden_ring'),
        (str(project_base / 'scripts/elden_ring/Save_management.luac'), 'scripts/elden_ring'),
        (str(project_base / 'scripts/elden_ring/Skyrim_transition.lua'), 'scripts/elden_ring'),
        (str(project_base / 'scripts/elden_ring/Skyrim_transition.luac'), 'scripts/elden_ring'),
        (str(project_base / 'scripts/skyrim_launcher.bat'), 'scripts')
    ],
    hiddenimports=[],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='installer',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='installer'
)
