#!/usr/bin/python3

import os, sys, zipfile, datetime, re, shutil

def wildcard2re(e):
    return e.replace('*', '.*').replace('?', '.?').replace(';', '|')

def smartcopy(src, dst):
    if os.path.isfile(src):
        shutil.copy(src, dst + '/' + os.path.basename(src) if os.path.exists(dst) else dst)
    else:
        shutil.copytree(src, dst + '/' + os.path.basename(src) if os.path.exists(dst) else dst)

phfs_path = ''

if len(sys.argv) < 2:
    phfs_path = input(' * Input path of PHFS workdir: ')
else:
    phfs_path = sys.argv[1]

print(' * Delete previously generated version...')
shutil.rmtree('phfs-win')

print(' * Create directory phfs-win...')
os.makedirs('phfs-win')

print(' * Create directory phfs-win/phfs...')
os.makedirs('phfs-win/phfs')

print(' * Copy Python3.7 32bit embeddable version...')
for i in os.listdir('python3'):
    smartcopy('python3/%s' % i, 'phfs-win/phfs')

print(' * Copy VC++ runtime...')
for i in os.listdir('api-ms'):
    smartcopy('api-ms/%s' % i, 'phfs-win/phfs')

print(' * Read .gitignore file...')
f = open('%s/.gitignore' % phfs_path, 'r', encoding='utf-8')
ignored_files = f.read().split('\n') + ['.git', '.gitignore', '.github']
f.close()

print(' * Copy PHFS files...')
for i in os.listdir(phfs_path):
    # Currently this ignore detect not work to sub-directories
    if True in [bool(re.fullmatch(wildcard2re(x), i)) for x in ignored_files]:
        print('   * Ignored: %s' % i)
    else:
        smartcopy('%s/%s' % (phfs_path, i), 'phfs-win/phfs')

print(' * Copy template...')
smartcopy('hfs.tpl', 'phfs-win/phfs')

print(' * Copy Werkzeug...')
smartcopy('werkzeug', 'phfs-win/phfs')

print(' * Copy WSGIserver...')
smartcopy('wsgiserver.py', 'phfs-win/phfs')

print(' * Copy start.bat...')
smartcopy('start.bat', 'phfs-win')

print(' * Create ZIP file...')
z = zipfile.ZipFile('phfs-win.zip', 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9)
for dirpath, dirnames, filenames in os.walk('phfs-win'):
    for i in filenames:
        z.write(os.path.join(dirpath, i))
z.comment = ('PHFS ~ Python HTTP File Server bundle for win32 platform at %s' % str(datetime.datetime.now())).encode('utf-8')
z.close()

print('================\n * Done!')
