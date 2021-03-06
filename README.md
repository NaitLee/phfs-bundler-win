# phfs-bundler-win

*Bundler script for PHFS for Windows platform*

*Now also does this for unix-like platforms*

## What's special?

There are some batch scripts prepared here for PHFS to act like original HFS -- simply drag-drop then files are shared.

Though PHFS (currently) have no GUI, you can drag-drop your file/folder(s) to `start.bat` inside the bundle, then they are shared to `http://localhost:8090/`.

For your LAN/WAN IP address, check online tutorials for getting it.

Exact things happened when drag-drop:

- If what being dropped is a folder, its content will be shared.
  - That means changes to files inside will be reflected at server side.
- If it's a file, or many items, they will be copied to a temporary folder and shared.
  - That means changes to original files will not be reflected at server side.

## Steps

1. Download newer version of embeddable python from [here](https://www.python.org/downloads/), extract to folder `python3`.
2. Download Werkzeug from [here](https://pypi.org/project/Werkzeug/#files), extract the folder `Werkzeug-(version)/src/werkzeug` as `werkzeug`.
3. Download WSGIserver from [here](https://pypi.org/project/WSGIserver/#files), extract the file `WSGIserver-(version)/wsgiserver.py` as `wsgiserver.py`.
4. Get sha256.js from [here](https://github.com/AndersLindman/SHA256), create folder `other`, put `sha256.js` inside.
5. Pick a template for HFS 2.4, rename it as `hfs.tpl`, place into this folder.
6. Create new folder `api-ms`, copy these files from `C:\Windows\System32` (32 bit) or `C:\Windows\SysWOW64` (64 bit) to that folder:
```
api-ms-win-core-console-l1-1-0.dll
api-ms-win-core-datetime-l1-1-0.dll
api-ms-win-core-debug-l1-1-0.dll
api-ms-win-core-delayload-l1-1-0.dll
api-ms-win-core-errorhandling-l1-1-0.dll
api-ms-win-core-fibers-l1-1-0.dll
api-ms-win-core-file-l1-1-0.dll
api-ms-win-core-file-l1-2-0.dll
api-ms-win-core-file-l2-1-0.dll
api-ms-win-core-handle-l1-1-0.dll
api-ms-win-core-heap-l1-1-0.dll
api-ms-win-core-interlocked-l1-1-0.dll
api-ms-win-core-io-l1-1-0.dll
api-ms-win-core-libraryloader-l1-1-0.dll
api-ms-win-core-localization-l1-1-0.dll
api-ms-win-core-localization-l1-2-0.dll
api-ms-win-core-localregistry-l1-1-0.dll
api-ms-win-core-memory-l1-1-0.dll
api-ms-win-core-misc-l1-1-0.dll
api-ms-win-core-namedpipe-l1-1-0.dll
api-ms-win-core-processenvironment-l1-1-0.dll
api-ms-win-core-processthreads-l1-1-0.dll
api-ms-win-core-processthreads-l1-1-1.dll
api-ms-win-core-profile-l1-1-0.dll
api-ms-win-core-rtlsupport-l1-1-0.dll
api-ms-win-core-string-l1-1-0.dll
api-ms-win-core-synch-l1-1-0.dll
api-ms-win-core-synch-l1-2-0.dll
api-ms-win-core-sysinfo-l1-1-0.dll
api-ms-win-core-threadpool-l1-1-0.dll
api-ms-win-core-timezone-l1-1-0.dll
api-ms-win-core-util-l1-1-0.dll
api-ms-win-core-xstate-l1-1-0.dll
api-ms-win-core-xstate-l2-1-0.dll
api-ms-win-crt-conio-l1-1-0.dll
api-ms-win-crt-convert-l1-1-0.dll
api-ms-win-crt-environment-l1-1-0.dll
api-ms-win-crt-filesystem-l1-1-0.dll
api-ms-win-crt-heap-l1-1-0.dll
api-ms-win-crt-locale-l1-1-0.dll
api-ms-win-crt-math-l1-1-0.dll
api-ms-win-crt-multibyte-l1-1-0.dll
api-ms-win-crt-private-l1-1-0.dll
api-ms-win-crt-process-l1-1-0.dll
api-ms-win-crt-runtime-l1-1-0.dll
api-ms-win-crt-stdio-l1-1-0.dll
api-ms-win-crt-string-l1-1-0.dll
api-ms-win-crt-time-l1-1-0.dll
api-ms-win-crt-utility-l1-1-0.dll
api-ms-win-downlevel-advapi32-l1-1-0.dll
api-ms-win-downlevel-advapi32-l2-1-0.dll
api-ms-win-downlevel-normaliz-l1-1-0.dll
api-ms-win-downlevel-ole32-l1-1-0.dll
api-ms-win-downlevel-shell32-l1-1-0.dll
api-ms-win-downlevel-shlwapi-l1-1-0.dll
api-ms-win-downlevel-shlwapi-l2-1-0.dll
api-ms-win-downlevel-user32-l1-1-0.dll
api-ms-win-downlevel-version-l1-1-0.dll
api-ms-win-security-base-l1-1-0.dll
api-ms-win-security-lsalookup-l1-1-0.dll
api-ms-win-security-sddl-l1-1-0.dll
api-ms-win-service-core-l1-1-0.dll
api-ms-win-service-management-l1-1-0.dll
api-ms-win-service-management-l2-1-0.dll
api-ms-win-service-winsvc-l1-1-0.dll
ucrtbase.dll
```
7. Run `bundle.py` with Python3, input path to cloned [PHFS repo](https://github.com/NaitLee/PHFS) folder, wait for a while, then done ????
8. You can run PHFS with `phfs-win\start.bat`, redistribute with `phfs-win.zip`.

## For unix

For historical reason, needs to generate phfs-win first to continue.

If you dislike Windows things, simply leave related folders empty to generate phfs-win.

After generating phfs-win, run `get-unix.py` then done ????

You can run PHFS with `phfs-unix\run.py`, redistribute with `phfs-unix.zip`.
