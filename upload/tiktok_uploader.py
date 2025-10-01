from pathlib import Path
from typing import Optional, Tuple
import logging
import requests

from .provider import BaseUploader


class TikTokUploader(BaseUploader):
    """Esqueleto de uploader para TikTok usando requests + sessionid cookie.

    ATENÇÃO: Este é um scaffold. Não implementa o fluxo real de upload porque
    a integração com o TikTok envolve endpoints privados e riscos ao violar TOS.
    Use este adaptador apenas como ponto de partida.
    """

    def __init__(self, sessionid: Optional[str] = None, *, dry_run: bool = True):
        self.session = requests.Session()
        self.dry_run = dry_run
        if sessionid:
            # define cookie sessionid para domínio .tiktok.com
            self.session.cookies.set("sessionid", sessionid, domain=".tiktok.com")

    def upload(self, video_path: Path, caption: str) -> Tuple[bool, Optional[str]]:
        logging.info("[TikTokUploader] upload called for %s (dry_run=%s)", video_path.name, self.dry_run)
        if self.dry_run:
            return True, f"tiktok_stub://{video_path.stem}"

        # Implement real upload here using TikTok private endpoints or an unofficial library.
        # This often requires multipart upload, media initialization, chunk upload, and publish call.
        raise NotImplementedError("TikTokUploader.upload is not implemented for non-dry-run mode")
