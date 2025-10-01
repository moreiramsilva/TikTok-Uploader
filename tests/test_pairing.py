from pathlib import Path
import tempfile
import shutil

from main import pair_videos


def test_pairing_creates_pairs(tmp_path):
    upload_dir = tmp_path / "upload"
    upload_dir.mkdir()
    # criar um vídeo e legenda
    v = upload_dir / "video1.mp4"
    t = upload_dir / "video1.txt"
    v.write_bytes(b"dummy")
    t.write_text("caption here")

    pairs = pair_videos(upload_dir)
    assert len(pairs) == 1
    p, caption = pairs[0]
    assert p.name == "video1.mp4"
    assert caption == "caption here"
