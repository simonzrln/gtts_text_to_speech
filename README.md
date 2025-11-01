# Text-to-Speech (TTS) Generator

Dieses Tool wandelt Text in Sprachausgabe um und speichert das Ergebnis als MP3-Audiodatei.

Das Skript liest automatisch die Datei `input.txt` und erzeugt daraus eine Audiodatei `output.mp3`.

---

## 📋 Was du brauchst

- **Python 3.8 oder neuer** (überprüfe mit `python --version` oder `python3 --version`)
- **Internetverbindung** (gTTS nutzt Googles Text-to-Speech-Service)

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

# Andere Sprache (z.B. Englisch)
python tts_cli.py -l en -t "Hello World"
```

**Alle Optionen im Überblick:**
- `-t`, `--text`: Der zu sprechende Text (ansonsten wird `input.txt` gelesen)
- `-o`, `--output`: Name der Ausgabedatei (Standard: `output.mp3`)
- `-l`, `--lang`: Sprachcode (z.B. `de` für Deutsch, `en` für Englisch)

---

## ❓ Problemlösung

### „ModuleNotFoundError" oder „Import Error"

- Stelle sicher, dass du die virtuelle Umgebung aktiviert hast:
  - **Windows**: `.\.venv\Scripts\Activate.ps1`
  - **macOS/Linux**: `source .venv/bin/activate`
- Installiere die Abhängigkeiten erneut: `pip install -r requirements.txt`

### Die Ausgabedatei ist leer oder sehr kurz

- Prüfe, ob `input.txt` Text enthält
- Stelle sicher, dass du eine Internetverbindung hast (gTTS benötigt Online-Zugriff)

---

## 📦 Projektstruktur

```
TTS/
├── tts_cli.py           # Hauptskript
├── input.txt            # Dein Text (hier reinschreiben!)
├── requirements.txt     # Python-Abhängigkeiten
├── run_windows.ps1      # Windows-Startskript (PowerShell)
├── run_windows.bat      # Windows-Startskript (cmd)
├── README.md            # Diese Anleitung
└── tests/               # Tests (optional)
```

---

## 💡 Tipps

- **Verschiedene Sprachen**: gTTS unterstützt viele Sprachen (z.B. `de`, `en`, `fr`, `es`, `it`, `ja`, `ko`)
- **Eigene Texte**: Bearbeite einfach `input.txt` und führe das Skript erneut aus
- **Längere Texte**: Das Skript funktioniert auch mit sehr langen Texten
- **Qualität**: Die Sprachausgabe verwendet Googles hochwertigen Text-to-Speech-Service

---

## 📄 Lizenz

Dieses Projekt nutzt die gTTS-Bibliothek (Google Text-to-Speech) und ist für den persönlichen und nicht-kommerziellen Gebrauch gedacht.
