import requests
import xml.etree.ElementTree as ET
import gzip
import io
import os

URL_SHARE = "https://epgshare01.online/epgshare01/epg_ripper_ALL_SOURCES1.xml.gz"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

def gerar_epg():
    print("Iniciando download...")
    try:
        resp = requests.get(URL_SHARE, headers=HEADERS, timeout=60)
        print(f"Status da resposta: {resp.status_code}")
        
        if resp.status_code == 200:
            print("Download concluído. Descompactando...")
            buffer = io.BytesIO(resp.content)
            with gzip.GzipFile(fileobj=buffer) as f:
                conteudo = f.read()
                
            print("Processando XML...")
            with open("epg_completo.xml", "wb") as f:
                f.write(conteudo)
            print("Arquivo epg_completo.xml salvo com sucesso!")
        else:
            print(f"Falha no download. Status: {resp.status_code}")
    except Exception as e:
        print(f"Erro crítico: {e}")

if __name__ == "__main__":
    gerar_epg()
