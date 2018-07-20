# -*- mode: python -*-

block_cipher = None


a = Analysis(['zerojudge-cli.py'],
             pathex=['Z:\\home\\neptune\\GitHub\\zerojudge-cli','~/.wine/drive_c/Python27/Lib/site-packages','Z:\\usr\\lib\\python3.6\\site-packages'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='zerojudge-cli',
          debug=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='zerojudge-cli')
