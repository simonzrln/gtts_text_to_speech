<#
run_windows.ps1

Erstellt eine virtuelle Umgebung (.venv) falls nötig, installiert Abhängigkeiten
und führt `tts_cli.py` aus mit der lokalen Python-Interpreter der venv.
#>
param(
    [string[]]$Args
)

Set-StrictMode -Version Latest
Push-Location -ErrorAction Stop
try {
    $venvDir = Join-Path -Path $PWD -ChildPath ".venv"
    $python = Join-Path $venvDir "Scripts\python.exe"

    if (-not (Test-Path $python)) {
        Write-Host "Erstelle virtuelle Umgebung .venv..."
        python -m venv .venv
    }

    Write-Host "Installiere Abhängigkeiten (requirements.txt)..."
    & $python -m pip install --upgrade pip
    & $python -m pip install -r requirements.txt

    Write-Host "Starte tts_cli.py..."
    & $python tts_cli.py @Args
}
finally {
    Pop-Location
}
