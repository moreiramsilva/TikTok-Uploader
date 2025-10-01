from pathlib import Path

from upload.provider import MockUploader


def test_mock_uploader_returns_success(tmp_path):
    v = tmp_path / "video.mp4"
    v.write_bytes(b"x")
    uploader = MockUploader()
    ok, remote = uploader.upload(v, "caption")
    assert ok is True
    assert remote.startswith("mock://")
