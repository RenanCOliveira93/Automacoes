"""Script para baixar vídeos do YouTube usando yt-dlp.

Uso:
    python download_youtube.py "https://www.youtube.com/watch?v=..."

Pré-requisito:
    pip install yt-dlp
"""

from __future__ import annotations

import argparse
import shutil
import sys


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Recebe um link do YouTube e faz o download do vídeo."
    )
    parser.add_argument("url", help="Link do vídeo do YouTube")
    parser.add_argument(
        "-o",
        "--output",
        default="%(title)s.%(ext)s",
        help="Template de nome do arquivo de saída (padrão: %%(title)s.%%(ext)s)",
    )
    parser.add_argument(
        "-q",
        "--qualidade",
        default="bestvideo+bestaudio/best",
        help=(
            "Formato/qualidade do download no padrão do yt-dlp "
            "(padrão: bestvideo+bestaudio/best)"
        ),
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    if shutil.which("yt-dlp") is None:
        print(
            "Erro: 'yt-dlp' não encontrado no sistema. "
            "Instale com: pip install yt-dlp",
            file=sys.stderr,
        )
        return 1

    try:
        from yt_dlp import YoutubeDL
    except ImportError:
        print(
            "Erro: módulo Python 'yt_dlp' não encontrado. "
            "Instale com: pip install yt-dlp",
            file=sys.stderr,
        )
        return 1

    options = {
        "format": args.qualidade,
        "outtmpl": args.output,
        "noplaylist": True,
    }

    with YoutubeDL(options) as ydl:
        ydl.download([args.url])

    print("Download concluído com sucesso.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
