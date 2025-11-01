# Text-to-Speech (TTS) Generator

Dieses Tool wandelt Text in Sprachausgabe um und speichert das Ergebnis als Audiodatei (MP3, WAV oder OGG).

Das Skript liest automatisch die Datei `input.txt` und erzeugt daraus eine Audiodatei `output.mp3`.

---

## 📋 Was du brauchst

- **Python 3.8 oder neuer** (überprüfe mit `python --version` oder `python3 --version`)
- **ffmpeg** (nur wenn du WAV- oder OGG-Dateien erzeugen willst; für MP3 optional aber empfohlen)

---

## 🚀 Schnellstart

### Windows

1. **Projekt herunterladen/klonen**
   ```powershell
   git clone <dein-repo-url>
   cd TTS
   ```

2. **Einfach starten** (automatische Einrichtung)
   - Doppelklick auf `run_windows.bat` ODER
   - In PowerShell:
     ```powershell
     .\run_windows.ps1
     ```
   
   Das Skript richtet automatisch alles ein (virtuelle Umgebung, Abhängigkeiten) und startet die Sprachausgabe.

3. **Deine Audiodatei ist fertig!**
   - Die Datei `output.mp3` findest du im Projektordner
   - Du kannst `input.txt` bearbeiten und das Skript erneut ausführen

### macOS / Linux

1. **Projekt herunterladen/klonen**
   ```bash
   git clone <dein-repo-url>
   cd TTS
   ```

2. **Einrichtung (nur beim ersten Mal)**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Skript ausführen**
   ```bash
   python tts_cli.py
   ```

4. **Deine Audiodatei ist fertig!**
   - Die Datei `output.mp3` findest du im Projektordner

---

## 📝 So benutzt du das Tool

### Einfache Nutzung (empfohlen)

1. **Öffne `input.txt`** und schreibe oder füge deinen Text ein
2. **Führe das Skript aus** (siehe oben)
3. **Fertig!** Die Audiodatei `output.mp3` wird erstellt

### Erweiterte Optionen

Du kannst das Skript auch direkt mit verschiedenen Optionen aufrufen:

```bash
# Text direkt angeben
python tts_cli.py -t "Hallo Welt"

# Anderer Dateiname
python tts_cli.py -o meine_ausgabe.mp3

# Anderes Format (WAV oder OGG - erfordert ffmpeg!)
python tts_cli.py -f wav -o ausgabe.wav

# Andere Sprache (z.B. Englisch)
python tts_cli.py -l en -t "Hello World"
```

**Alle Optionen im Überblick:**
- `-t`, `--text`: Der zu sprechende Text (ansonsten wird `input.txt` gelesen)
- `-o`, `--output`: Name der Ausgabedatei (Standard: `output.mp3`)
- `-f`, `--format`: Format der Audiodatei: `mp3`, `wav` oder `ogg` (Standard: `mp3`)
- `-l`, `--lang`: Sprachcode (z.B. `de` für Deutsch, `en` für Englisch)

---

## 🔧 ffmpeg installieren (optional, aber empfohlen)

**Wofür wird ffmpeg gebraucht?**
- Für WAV- oder OGG-Ausgabe: **unbedingt erforderlich**
- Für MP3: verbessert die Qualität bei längeren Texten (mehrere Teile werden sauber zusammengefügt)

### Windows

**Option 1: Chocolatey** (als Administrator)
```powershell
choco install ffmpeg
```

**Option 2: Scoop** (ohne Administrator, empfohlen)
```powershell
# Falls Scoop noch nicht installiert ist:
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
irm get.scoop.sh | iex

# ffmpeg installieren:
scoop install ffmpeg
```

**Option 3: Manuell**
1. Lade ffmpeg herunter: https://www.gyan.dev/ffmpeg/builds/
2. Entpacke die Datei
3. Füge den `bin`-Ordner zu deinen Umgebungsvariablen hinzu (PATH)

**Prüfen, ob ffmpeg funktioniert:**
```powershell
ffmpeg -version
```

### macOS

```bash
brew install ffmpeg
```

**Prüfen, ob ffmpeg funktioniert:**
```bash
ffmpeg -version
```

### Linux

```bash
# Ubuntu/Debian
sudo apt install ffmpeg

# Fedora
sudo dnf install ffmpeg

# Arch
sudo pacman -S ffmpeg
```

---

## ❓ Problemlösung

### „ffmpeg nicht gefunden" oder ähnliche Warnung

- **MP3-Ausgabe**: Das Skript funktioniert trotzdem, aber bei längeren Texten wird nur der erste Teil verwendet
- **WAV/OGG-Ausgabe**: Installiere ffmpeg (siehe oben)
- **Prüfe die Installation**: führe `check_ffmpeg.py` aus
  ```bash
  python check_ffmpeg.py
  ```

### „ModuleNotFoundError" oder „Import Error"

- Stelle sicher, dass du die virtuelle Umgebung aktiviert hast:
  - **Windows**: `.\.venv\Scripts\Activate.ps1`
  - **macOS/Linux**: `source .venv/bin/activate`
- Installiere die Abhängigkeiten erneut: `pip install -r requirements.txt`

### Die Ausgabedatei ist leer oder sehr kurz

- Prüfe, ob `input.txt` Text enthält
- Bei längeren Texten: installiere ffmpeg für bessere Zusammenführung

---

## 📦 Projektstruktur

```
TTS/
├── tts_cli.py           # Hauptskript
├── input.txt            # Dein Text (hier reinschreiben!)
├── requirements.txt     # Python-Abhängigkeiten
├── run_windows.ps1      # Windows-Startskript (PowerShell)
├── run_windows.bat      # Windows-Startskript (cmd)
├── check_ffmpeg.py      # Hilfsskript: ffmpeg-Check
├── README.md            # Diese Anleitung
└── tests/               # Tests (optional)
```

---

## 💡 Tipps

- **Längere Texte**: Das Skript teilt automatisch lange Texte in Abschnitte auf und zeigt eine Fortschrittsanzeige
- **Verschiedene Sprachen**: gTTS unterstützt viele Sprachen (z.B. `de`, `en`, `fr`, `es`, `it`, `ja`, `ko`)
- **Keine Internetverbindung?**: gTTS benötigt Internet, da es Googles Text-to-Speech-Service nutzt
- **Eigene Texte**: Bearbeite einfach `input.txt` und führe das Skript erneut aus

---

## 📄 Lizenz

Dieses Projekt nutzt die gTTS-Bibliothek (Google Text-to-Speech) und ist für den persönlichen und nicht-kommerziellen Gebrauch gedacht.
