# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['learnt_SQLlite.py'],
    pathex=[],
    binaries=[],
    datas=[('C:\\Users\\sersa\\AppData\\Local\\Programs\\Python\\Python313\\tcl\\tcl8.6', 'tcl\\tcl8.6'), ('C:\\Users\\sersa\\AppData\\Local\\Programs\\Python\\Python313\\tcl\\tk8.6', 'tcl\\tk8.6')],
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
    name='learnt_SQLlite',
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
    icon=['C:\\Users\\sersa\\OneDrive\\Рабочий стол\\learnt\\icon\\favicon.ico'],
)
