#!/usr/bin/env python3
"""tts_cli.py

CLI, die gTTS verwendet, um eingegebenen Text in MP3-Audio zu konvertieren.
Standardmäßig liest das Skript `input.txt` aus dem aktuellen Verzeichnis, wenn kein `--text`
Argument gegeben wurde. Der Prozess zeigt eine Fortschrittsleiste (tqdm) für die Synthese.
"""
from pathlib import Path
import argparse
import sys

from gtts import gTTS

try:
    from tqdm import tqdm
except Exception:
    # fallback: einfache Ersatzklasse falls tqdm nicht installiert
    class tqdm:
        def __init__(self, iterable=None, total=None, desc=None):
            self.iterable = iterable or []

        def __iter__(self):
            return iter(self.iterable)

        def update(self, n=1):
            pass


def synthesize_text(text: str, out_path: str, lang: str = "de") -> Path:
    """Synthesize text to MP3 audio file using gTTS.
    
    Args:
        text: Der zu sprechende Text
        out_path: Zieldateipfad für die MP3
        lang: Sprachcode für gTTS (z.B. 'de' für Deutsch)
    
    Returns:
        Path zur erstellten MP3-Datei
    """
    out = Path(out_path)
    
    print("Erzeuge Sprachausgabe...")
    tts = gTTS(text=text, lang=lang)
    tts.save(str(out))
    
    return out


def _read_stdin_text() -> str:
    data = sys.stdin.read()
    return data.strip()


def main():
    parser = argparse.ArgumentParser(description="Text-to-speech mit gTTS. Liest standardmäßig `input.txt` und erzeugt MP3.")
    parser.add_argument("-t", "--text", help="Text (wenn nicht gesetzt, wird stdin oder `input.txt` gelesen)")
    parser.add_argument("-o", "--output", default="output.mp3", help="Output-Dateiname (Default: output.mp3)")
    parser.add_argument("-l", "--lang", default="de", help="Sprachcode für gTTS (z.B. 'de' oder 'en')")

    args = parser.parse_args()

    text = args.text
    # Reihenfolge: --text > stdin > input.txt > interaktiv
    if not text:
        try:
            if not sys.stdin.isatty():
                piped = _read_stdin_text()
                if piped:
                    text = piped
        except Exception:
            pass

    if not text:
        input_file = Path("input.txt")
        if input_file.exists():
            text = input_file.read_text(encoding="utf-8")

    if not text:
        text = input("Bitte den zu sprechenden Text eingeben: ")

    out_path = args.output
    try:
        result = synthesize_text(text=text, out_path=out_path, lang=args.lang)
        print(f"✓ Erstellt: {result}")
    except Exception as e:
        print("Fehler beim Erzeugen der Audio-Datei:", e, file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
