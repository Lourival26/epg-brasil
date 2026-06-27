import requests
import xml.etree.ElementTree as ET
import gzip
import io
import time

URL = "https://epgshare01.online/epgshare01/epg_ripper_ALL_SOURCES1.xml.gz"
HEADERS = {"User-Agent": "Mozilla/5.0"}

def gerar_epg():
    print("Iniciando download da Share...")
    try:
        # Aumentamos o timeout para garantir que o download tenha tempo de concluir
        response = requests.get(URL, headers=HEADERS, timeout=120)
        response.raise_for_status() # Lança erro se a resposta não for 200
        
        print("Download bem-sucedido. Descompactando...")
        buffer = io.BytesIO(response.content)
        with gzip.GzipFile(fileobj=buffer) as f:
            # Lendo todo o conteúdo para a memória
            conteudo = f.read()
            
        print("Salvando arquivo final...")
        with open("epg_completo.xml", "wb") as f:
            f.write(conteudo)
            
        print("Sucesso total!")
    except Exception as e:
        print(f"Erro ocorrido: {e}")

if __name__ == "__main__":
    gerar_epg()
