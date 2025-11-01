#!/usr/bin/env python3
"""tts_cli.py

CLI, die gTTS verwendet, um eingegebenen Text in Audio zu konvertieren.
Standardmäßig liest das Skript `input.txt` aus dem aktuellen Verzeichnis, wenn kein `--text`
Argument gegeben wurde. Der Prozess teilt längere Texte in Chunks und zeigt eine
Fortschrittsleiste (tqdm) für die einzelnen Synthese-Schritte.

Für WAV/OGG wird `pydub` + ffmpeg verwendet. Wenn `pydub` fehlt, fällt das Skript
auf eine einfache, einzeldatei-basierte Synthese zurück.
"""
from pathlib import Path
import argparse
import sys
import tempfile
import re
import shutil
from typing import List

from gtts import gTTS

try:
    from tqdm import tqdm
except Exception:
    # fallback: einfache Ersatzklasse
    class tqdm:
        def __init__(self, iterable=None, total=None, desc=None):
            self.iterable = iterable or []

        def __iter__(self):
            return iter(self.iterable)

        def update(self, n=1):
            pass


def split_text_into_chunks(text: str, max_chars: int = 250) -> List[str]:
    """Split text into chunks by sentences, grouping until max_chars reached."""
    # einfache Satztrennung (preserve punctuation)
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())
    chunks = []
    current = []
    cur_len = 0
    for s in sentences:
        if not s:
            continue
        if cur_len + len(s) + 1 > max_chars and current:
            chunks.append(" ".join(current))
            current = [s]
            cur_len = len(s)
        else:
            current.append(s)
            cur_len += len(s) + 1
    if current:
        chunks.append(" ".join(current))
    return chunks


def synthesize_chunks_to_file(chunks: List[str], out_path: str, fmt: str = "mp3", lang: str = "de") -> Path:
    """Synthesize multiple text chunks and combine them into a single audio file.

    - Für jeden Chunk wird eine temporäre MP3 mit gTTS erzeugt.
    - Anschließend werden die Fragmente mit pydub zusammengefügt (falls vorhanden).
    - Unterstützte Formate: mp3, wav, ogg
    """
    out = Path(out_path)
    fmt = fmt.lower()
    if fmt not in ("mp3", "wav", "ogg"):
        raise ValueError(f"Unsupported format: {fmt}")

    tmp_dir = Path(tempfile.mkdtemp(prefix="tts_tmp_"))
    tmp_files = []

    try:
        # Schritt 1: pro Chunk ein mp3 erzeugen und Fortschritt anzeigen
        for i, chunk in enumerate(tqdm(chunks, desc="Synthesizing", total=len(chunks))):
            tmp_file = tmp_dir / f"part_{i}.mp3"
            tts = gTTS(text=chunk, lang=lang)
            tts.save(str(tmp_file))
            tmp_files.append(str(tmp_file))

        # Schritt 2: Falls pydub verfügbar, zusammenfügen und exportieren
        try:
            from pydub import AudioSegment
        except Exception:
            # Kein pydub: wenn nur mp3 gewünscht, nenne die erste Datei um und fertig
            if fmt == "mp3":
                # einfache naive Zusammenführung durch Byte-Konkatenation ist nicht zuverlässig
                # daher speichern wir stattdessen die erste Datei und warnen
                shutil.copy(tmp_files[0], out)
                print("Hinweis: pydub fehlt — nur der erste Chunk wurde als Ausgabe verwendet.")
                return out
            else:
                raise RuntimeError("Für WAV/OGG-Konvertierung wird `pydub` und ffmpeg benötigt.")

        # pydub vorhanden: lade alle Teile und hänge an
        combined = None
        for tmp in tmp_files:
            seg = AudioSegment.from_file(tmp, format="mp3")
            if combined is None:
                combined = seg
            else:
                combined += seg

        # export
        if fmt == "mp3":
            combined.export(str(out), format="mp3")
        elif fmt == "wav":
            combined.export(str(out), format="wav")
        elif fmt == "ogg":
            combined.export(str(out), format="ogg")

        return out
    finally:
        # aufräumen
        try:
            shutil.rmtree(tmp_dir)
        except Exception:
            pass


def synthesize_text(text: str, out_path: str, fmt: str = "mp3", lang: str = "de") -> Path:
    """High-level: wähle chunked oder single-shot je nach Länge und sorge für Fortschritt."""
    # Wenn Text kurz ist, gTTS in einem Rutsch
    if len(text) <= 200:
        out = Path(out_path)
        if fmt == "mp3":
            tts = gTTS(text=text, lang=lang)
            tts.save(str(out))
            return out
        else:
            # Erzeuge mp3 temporär und konvertiere mit pydub
            with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as tmp:
                tmp_name = tmp.name
            tts = gTTS(text=text, lang=lang)
            tts.save(tmp_name)
            try:
                from pydub import AudioSegment
            except Exception as e:
                raise RuntimeError("Konvertierung erfordert pydub + ffmpeg.") from e
            audio = AudioSegment.from_mp3(tmp_name)
            audio.export(str(out), format=fmt)
            return out

    # Sonst chunked mit Fortschrittsanzeige
    chunks = split_text_into_chunks(text)
    return synthesize_chunks_to_file(chunks, out_path, fmt=fmt, lang=lang)


def _read_stdin_text() -> str:
    data = sys.stdin.read()
    return data.strip()


def main():
    parser = argparse.ArgumentParser(description="Text-to-speech mit gTTS. Liest standardmäßig `input.txt` wenn vorhanden.")
    parser.add_argument("-t", "--text", help="Text (wenn nicht gesetzt, wird stdin oder `input.txt` gelesen)")
    parser.add_argument("-o", "--output", default="output.mp3", help="Output-Dateiname (Default: output.mp3)")
    parser.add_argument("-f", "--format", default="mp3", choices=["mp3", "wav", "ogg"], help="Ziel-Audioformat")
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
        result = synthesize_text(text=text, out_path=out_path, fmt=args.format, lang=args.lang)
        print(f"Erstellt: {result}")
    except Exception as e:
        print("Fehler beim Erzeugen der Audio-Datei:", e, file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
