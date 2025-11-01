"""Kleines Hilfs-Skript: prüft, ob ffmpeg/ffprobe verfügbar sind und gibt Hinweise."""
import shutil
import sys


def find_bin(name):
    path = shutil.which(name)
    return path


def main():
    ffmpeg = find_bin("ffmpeg")
    ffprobe = find_bin("ffprobe")

    if ffmpeg:
        print(f"ffmpeg gefunden: {ffmpeg}")
    else:
        print("ffmpeg nicht gefunden. Installationshinweise:")
        print("  - Windows: choco install ffmpeg  oder scoop install ffmpeg")
        print("  - macOS: brew install ffmpeg")
        print("  - Linux: apt/snap/your-distro packages")

    if ffprobe:
        print(f"ffprobe gefunden: {ffprobe}")
    else:
        print("ffprobe nicht gefunden (wird von pydub benötigt).")

    if not ffmpeg or not ffprobe:
        sys.exit(2)


if __name__ == "__main__":
    main()
