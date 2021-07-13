#!/usr/bin/python3

import os, shutil, zipfile, datetime

def smartcopy(src, dst):
    if os.path.isfile(src):
        shutil.copy(src, dst + '/' + os.path.basename(src) if os.path.exists(dst) else dst)
    else:
        shutil.copytree(src, dst + '/' + os.path.basename(src) if os.path.exists(dst) else dst)

files = """
docs
werkzeug
_test_macro.py
alias.txt
cfgLib.py
classesLib.py
filelist.tpl
hash.py
hashLib.py
helpersLib.py
hfs.ini
hfs.tpl
i18n.ini
i18nLib.py
LICENSE
LICENSE.txt
mime.ini
mimeLib.py
README-zh-CN.md
README.md
requirements.txt
run.py
scriptLib.py
SECURITY.md
serverLib.py
sha256.js
test.py
tplLib.py
wsgiserver.py
"""

if not os.path.exists('phfs-win'):
    print(' * Needs generate phfs-win first. Exiting.')
    exit(1)

if os.path.exists('phfs-unix'):
    print(' * Delete previously generated version...')
    shutil.rmtree('phfs-unix')

print(' * Create directory phfs-unix...')
os.makedirs('phfs-unix')

print(' * Copy files...')
for i in files.split('\n'):
    if os.path.exists('phfs-win/phfs/%s' % i) and i != '':
        smartcopy('phfs-win/phfs/%s' % i, 'phfs-unix')

print(' * Create ZIP file...')
z = zipfile.ZipFile('phfs-unix.zip', 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9)
for dirpath, dirnames, filenames in os.walk('phfs-unix'):
    for i in filenames:
        z.write(os.path.join(dirpath, i))
z.comment = ('PHFS ~ Python HTTP File Server bundle for unix-like platform at %s' % str(datetime.datetime.now())).encode('utf-8')
z.close()
