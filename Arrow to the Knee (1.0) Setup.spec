# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['installer.py'],
    pathex=[],
    binaries=[],
    datas=[('Data', 'Data'), ('audio', 'audio'), ('scripts/elden_ring', 'scripts/elden_ring'), ('scripts/skyrim_LE', 'scripts/skyrim_LE')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='Arrow to the Knee (1.0) Setup',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['E:\\Files\\elden ring - arrow to the knee mod\\Arrow_to_the_Knee\\icon.ico'],
)
