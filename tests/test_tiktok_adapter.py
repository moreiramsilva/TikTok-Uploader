from pathlib import Path

from upload.tiktok_uploader import TikTokUploader


def test_tiktok_adapter_dry_run(tmp_path):
    v = tmp_path / "video.mp4"
    v.write_bytes(b"x")
    uploader = TikTokUploader(dry_run=True)
    ok, remote = uploader.upload(v, "caption")
    assert ok is True
    assert remote.startswith("tiktok_stub://")
