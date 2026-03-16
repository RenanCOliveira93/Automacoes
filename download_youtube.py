"""Script para baixar vídeos do YouTube usando yt-dlp.

Uso:
    python download_youtube.py "https://www.youtube.com/watch?v=..."

Pré-requisito (uma das opções):
    pip install yt-dlp
    # ou
    # instalar binário yt-dlp no sistema
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path


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
    parser.add_argument(
        "-d",
        "--diretorio",
        default=".",
        help="Diretório de saída dos arquivos (padrão: diretório atual)",
    )
    return parser.parse_args()


def download_com_modulo(url: str, output: str, qualidade: str) -> int:
    try:
        from yt_dlp import DownloadError, YoutubeDL
    except ImportError:
        return 2

    options = {
        "format": qualidade,
        "outtmpl": output,
        "noplaylist": True,
    }

    try:
        with YoutubeDL(options) as ydl:
            ydl.download([url])
    except DownloadError as exc:
        print(f"Erro no download: {exc}", file=sys.stderr)
        return 1

    return 0


def download_com_binario(url: str, output: str, qualidade: str) -> int:
    if shutil.which("yt-dlp") is None:
        return 2

    command = [
        "yt-dlp",
        "--no-playlist",
        "-f",
        qualidade,
        "-o",
        output,
        url,
    ]

    result = subprocess.run(command, check=False)
    return result.returncode


def main() -> int:
    args = parse_args()

    diretorio = Path(args.diretorio).expanduser().resolve()
    diretorio.mkdir(parents=True, exist_ok=True)

    output_template = str(diretorio / args.output)

    status = download_com_modulo(args.url, output_template, args.qualidade)
    if status == 0:
        print("Download concluído com sucesso.")
        return 0

    if status == 2:
        status_binario = download_com_binario(args.url, output_template, args.qualidade)
        if status_binario == 0:
            print("Download concluído com sucesso.")
            return 0

    print(
        "Erro: não foi possível baixar o vídeo. Instale o yt-dlp com: pip install yt-dlp "
        "ou instale o binário 'yt-dlp' no sistema.",
        file=sys.stderr,
    )
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
