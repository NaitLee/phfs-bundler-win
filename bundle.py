#!/usr/bin/python3

import os, sys, zipfile, datetime, re

def wildcard2re(e: str):
    return e.replace('*', '.*').replace('?', '.?').replace(';', '|')

phfs_path = ''

if len(sys.argv) < 2:
    phfs_path = input(' * Input path of PHFS workdir: ')
else:
    phfs_path = sys.argv[1]

print(' * Delete previously generated version...')
os.system('rm -rf phfs-win')

print(' * Create directory phfs-win...')
os.makedirs('phfs-win')

print(' * Create directory phfs-win/phfs...')
os.makedirs('phfs-win/phfs')

print(' * Copy Python3.7 32bit embeddable version...')
os.system('cp python3/* phfs-win/phfs')

print(' * Copy VC++ runtime...')
os.system('cp api-ms/* phfs-win/phfs')

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
        os.system('cp -r %s/%s phfs-win/phfs' % (phfs_path, i))

print(' * Copy template...')
os.system('cp hfs.tpl phfs-win/phfs')

print(' * Copy Werkzeug...')
os.system('cp -r werkzeug phfs-win/phfs')

print(' * Copy start.bat...')
os.system('cp start.bat phfs-win')

print(' * Create ZIP file...')
z = zipfile.ZipFile('phfs-win.zip', 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9)
for dirpath, dirnames, filenames in os.walk('phfs-win'):
    for i in filenames:
        z.write(os.path.join(dirpath, i))
z.comment = ('PHFS ~ Python HTTP File Server bundle for win32 platform at %s' % str(datetime.datetime.now())).encode('utf-8')
z.close()

print('================\n * Done!')
