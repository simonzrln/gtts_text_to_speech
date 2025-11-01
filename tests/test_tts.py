import tempfile
from pathlib import Path

from tts_cli import synthesize


def test_synthesize_mp3_creates_file(tmp_path):
    out = tmp_path / "test_out.mp3"
    synthesize("Dies ist ein Test.", str(out), fmt="mp3", lang="de")
    assert out.exists()
    assert out.stat().st_size > 0
