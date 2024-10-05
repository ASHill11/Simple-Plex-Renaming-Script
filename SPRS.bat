@echo off

REM Check if a file path argument was passed
if "%~1"=="" (
    REM No argument passed, run main.py
    "C:\Users\ASHil\AppData\Local\Microsoft\WindowsApps\python3.12.exe" "C:\Users\ASHil\Documents\VSCode Projects\Simple-Plex-Renaming-Script\main.py"
) else (
    REM Argument passed, run SPRS-bat.py with the file path as an argument
    "C:\Users\ASHil\AppData\Local\Microsoft\WindowsApps\python3.12.exe" "C:\Users\ASHil\Documents\VSCode Projects\Simple-Plex-Renaming-Script\SPRS-bat.py" "%~1"
)