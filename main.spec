# -*- mode: python -*-

block_cipher = None


a = Analysis(['main.py'],
             pathex=[''],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)

a.datas += [('iconmonstr-clipboard-6-32.png','C:\\Users\\Dell\\iconmonstr-clipboard-6-32.png','DATA')]

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='Geometryczne',
          debug=False,
          strip=False,
          upx=True,
          console=False)