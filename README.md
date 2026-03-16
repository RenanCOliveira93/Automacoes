# Automacoes
Repositório voltado a trabalhos/projetos que envolvam automação, como WebScrapping, PyAutogui, entre outras ferramentas. 

## Download de vídeo do YouTube
Script `download_youtube.py` para receber um link do YouTube e baixar o vídeo.

### Exemplo de uso
```bash
python download_youtube.py "https://www.youtube.com/watch?v=SEU_ID"
```

### Opções úteis
```bash
# definir pasta de saída
python download_youtube.py "https://www.youtube.com/watch?v=SEU_ID" --diretorio downloads

# definir nome/template do arquivo
python download_youtube.py "https://www.youtube.com/watch?v=SEU_ID" --output "%(title)s.%(ext)s"

# escolher qualidade/formato
python download_youtube.py "https://www.youtube.com/watch?v=SEU_ID" --qualidade "best"
```

### Dependência
Instale uma das opções abaixo:
```bash
pip install yt-dlp
```
ou tenha o binário `yt-dlp` disponível no sistema.
