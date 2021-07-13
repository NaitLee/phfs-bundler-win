@echo off
color f0
cd "%~dp0\phfs"
echo PHFS ~ Python HTTP File Server
echo ==============================
echo  * Please read README.txt or ./phfs/README.md for instructions

python.exe run.py %*
