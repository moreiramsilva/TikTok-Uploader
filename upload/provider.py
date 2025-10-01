from pathlib import Path
from typing import Optional, Tuple
import logging


class BaseUploader:
    """Interface para uploaders."""

    def upload(self, video_path: Path, caption: str) -> Tuple[bool, Optional[str]]:
        raise NotImplementedError()


class MockUploader(BaseUploader):
    """Uploader de mock para testes e desenvolvimento local."""

    def upload(self, video_path: Path, caption: str) -> Tuple[bool, Optional[str]]:
        logging.info("[MockUploader] Uploading %s (caption len=%d)", video_path.name, len(caption))
        # Simula algum processamento
        return True, f"mock://{video_path.stem}"
