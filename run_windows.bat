@echo off
REM run_windows.bat - creates venv, installs requirements and runs the script

IF NOT EXIST .venv\Scripts\python.exe (
    echo Creating virtual environment .venv...
    python -m venv .venv
)

echo Installing requirements...
.venv\Scripts\python.exe -m pip install --upgrade pip
.venv\Scripts\python.exe -m pip install -r requirements.txt

echo Running tts_cli.py ...
.venv\Scripts\python.exe tts_cli.py %*
