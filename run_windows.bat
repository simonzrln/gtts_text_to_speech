@echo off
REM run_windows.bat - creates venv, installs requirements and runs the script

IF NOT EXIST .venv\Scripts\python.exe (
    echo Creating virtual environment .venv...
    python -m venv .venv
)

echo Installing requirements...
.venv\Scripts\python.exe -m pip install --upgrade pip
.venv\Scripts\python.exe -m pip install -r requirements.txt

where ffmpeg >nul 2>&1
IF ERRORLEVEL 1 (
    echo WARNING: ffmpeg not found in PATH. WAV/OGG conversion may fail.
    echo Install options: choco install ffmpeg  OR  scoop install ffmpeg
)

echo Running tts_cli.py ...
.venv\Scripts\python.exe tts_cli.py %*
