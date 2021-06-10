@echo off
color f0
cd phfs
echo PHFS ~ Python HTTP File Server
echo ==============================
echo  * You can configure PHFS at ./phfs/hfs.ini.
echo  * Starting server...
python.exe _run_simple.py
