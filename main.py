#!/usr/bin/env python3
"""TikTok Uploader — esqueleto mínimo.

Este script escaneia `videos_para_upload/` em busca de arquivos `.mp4`, busca o `.txt` correspondente
para legenda e simula o upload para o TikTok.

Substitua a função `mock_upload` por uma implementação real de upload usando a API/biblioteca de sua escolha.
"""

import os
import shutil
import time
import logging
from pathlib import Path

try:
    from dotenv import load_dotenv
except Exception:
    load_dotenv = None


def mock_upload(video_path: Path, caption: str, sessionid: str):
    """Simula um upload. Retorna (success: bool, remote_id: str|None)."""
    logging.info("Simulando upload: %s (caption len=%d)", video_path.name, len(caption))
    time.sleep(0.5)
    return True, "mock_video_id_123"


def main():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s: %(message)s")
    root = Path(__file__).parent
    upload_dir = root / "videos_para_upload"
    published_dir = root / "videos_publicados"
    upload_dir.mkdir(exist_ok=True)
    published_dir.mkdir(exist_ok=True)

    if load_dotenv:
        # Carrega variáveis do arquivo .env na raiz do projeto, se existir
        load_dotenv(root / ".env")

    sessionid = os.getenv("TIKTOK_SESSION_ID")
    if not sessionid:
        logging.warning("TIKTOK_SESSION_ID não definido. Rodando em modo dry-run (sem enviar realmente).")

    videos = sorted(upload_dir.glob("*.mp4"))
    if not videos:
        logging.info("Nenhum vídeo encontrado em %s", upload_dir)
        return

    summary = {"success": 0, "failed": 0}

    for v in videos:
        txt = v.with_suffix(".txt")
        caption = ""
        if txt.exists():
            try:
                caption = txt.read_text(encoding="utf-8").strip()
            except Exception as e:
                logging.warning("Erro ao ler %s: %s", txt.name, e)
        else:
            logging.warning("Arquivo de legenda não encontrado para %s; legenda vazia será usada.", v.name)

        ok, remote_id = mock_upload(v, caption, sessionid)
        if ok:
            try:
                shutil.move(str(v), published_dir / v.name)
                if txt.exists():
                    shutil.move(str(txt), published_dir / txt.name)
                logging.info("Upload simulado com sucesso e arquivos movidos: %s", v.name)
                summary["success"] += 1
            except Exception as e:
                logging.error("Erro ao mover arquivos de %s: %s", v.name, e)
                summary["failed"] += 1
        else:
            logging.error("Falha no upload simulado para %s", v.name)
            summary["failed"] += 1

    logging.info("Resumo: sucesso=%d falha=%d", summary["success"], summary["failed"])


if __name__ == "__main__":
    main()
