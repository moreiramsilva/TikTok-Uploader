#!/usr/bin/env python3
"""TikTok Uploader — versão com adaptador, logging em arquivo e watchmode.

Use --watch para observar a pasta `videos_para_upload/` e enviar novos arquivos automaticamente.
"""

import os
import shutil
import time
import logging
import argparse
from pathlib import Path

try:
    from dotenv import load_dotenv
except Exception:
    load_dotenv = None

from upload.provider import MockUploader, BaseUploader


def setup_logging(root: Path):
    logs = root / "logs"
    logs.mkdir(exist_ok=True)
    log_file = logs / "uploader.log"
    handler = logging.handlers.RotatingFileHandler(str(log_file), maxBytes=2_000_000, backupCount=5)
    formatter = logging.Formatter("%(asctime)s %(levelname)s: %(message)s")
    handler.setFormatter(formatter)
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)
    root_logger.addHandler(handler)
    # also console handler
    ch = logging.StreamHandler()
    ch.setFormatter(formatter)
    root_logger.addHandler(ch)


def pair_videos(upload_dir: Path):
    """Retorna lista de (video_path, caption) a serem enviados."""
    pairs = []
    for v in sorted(upload_dir.glob("*.mp4")):
        txt = v.with_suffix(".txt")
        caption = ""
        if txt.exists():
            try:
                caption = txt.read_text(encoding="utf-8").strip()
            except Exception as e:
                logging.warning("Erro ao ler %s: %s", txt.name, e)
        else:
            logging.warning("Legenda não encontrada para %s; legenda vazia será usada.", v.name)
        pairs.append((v, caption))
    return pairs


def process_all(uploader: BaseUploader, upload_dir: Path, published_dir: Path):
    summary = {"success": 0, "failed": 0}
    for v, caption in pair_videos(upload_dir):
        ok, remote_id = uploader.upload(v, caption)
        if ok:
            try:
                shutil.move(str(v), published_dir / v.name)
                txt = v.with_suffix(".txt")
                if txt.exists():
                    shutil.move(str(txt), published_dir / txt.name)
                logging.info("Upload bem-sucedido: %s -> %s", v.name, remote_id)
                summary["success"] += 1
            except Exception as e:
                logging.exception("Erro ao mover arquivos de %s: %s", v.name, e)
                summary["failed"] += 1
        else:
            logging.error("Falha no upload para %s", v.name)
            summary["failed"] += 1
    logging.info("Resumo: sucesso=%d falha=%d", summary["success"], summary["failed"])


def watch_and_process(uploader: BaseUploader, upload_dir: Path, published_dir: Path):
    try:
        from watchdog.observers import Observer
        from watchdog.events import FileSystemEventHandler
    except Exception:
        logging.error("watchdog não instalado; instale com pip install watchdog")
        return

    class Handler(FileSystemEventHandler):
        def on_created(self, event):
            p = Path(event.src_path)
            if p.suffix.lower() == ".mp4":
                logging.info("Novo arquivo detectado: %s", p.name)
                time.sleep(0.5)  # esperar completar escrita
                process_all(uploader, upload_dir, published_dir)

    observer = Observer()
    observer.schedule(Handler(), str(upload_dir), recursive=False)
    observer.start()
    logging.info("Watchmode ativo em %s (pressione Ctrl+C para sair)", upload_dir)
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        logging.info("Encerrando watchmode...")
        observer.stop()
    observer.join()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--watch", action="store_true", help="Observa a pasta e envia novos vídeos automaticamente")
    parser.add_argument("--provider", choices=["mock", "tiktok"], default="mock", help="Escolhe o provider de upload")
    parser.add_argument("--dry-run", action="store_true", help="Executa em modo dry-run (não faz uploads reais)")
    args = parser.parse_args()

    root = Path(__file__).parent
    upload_dir = root / "videos_para_upload"
    published_dir = root / "videos_publicados"
    upload_dir.mkdir(exist_ok=True)
    published_dir.mkdir(exist_ok=True)

    setup_logging(root)

    if load_dotenv:
        load_dotenv(root / ".env")

    # Escolhe provider
    if args.provider == "mock":
        uploader = MockUploader()
    else:
        # import local para evitar erro se requests não estiver configurado
        from upload.tiktok_uploader import TikTokUploader
        uploader = TikTokUploader(sessionid=os.getenv("TIKTOK_SESSION_ID"), dry_run=args.dry_run)

    if args.watch:
        watch_and_process(uploader, upload_dir, published_dir)
    else:
        process_all(uploader, upload_dir, published_dir)


if __name__ == "__main__":
    main()
