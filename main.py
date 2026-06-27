import requests
import xml.etree.ElementTree as ET
import gzip
import io

# Agora o script foca apenas na fonte da Share
fontes = {
    "epgshare": "https://epgshare01.online/epgshare01/epg_ripper_ALL_SOURCES1.xml.gz"
}

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}

def baixar_xml(url):
    try:
        resp = requests.get(url, headers=HEADERS, timeout=60)
        if resp.status_code == 200:
            if url.endswith('.gz') or 'gzip' in resp.headers.get('Content-Encoding', ''):
                buffer = io.BytesIO(resp.content)
                with gzip.GzipFile(fileobj=buffer) as f:
                    return f.read()
            return resp.content
        else:
            print(f"Erro {resp.status_code} ao acessar {url}")
            return None
    except Exception as e:
        print(f"Erro na conexão com {url}: {e}")
        return None

def gerar_epg_unificado():
    root = ET.Element("tv", {"generator-info-name": "Lourival26-EPG"})
    
    # Processa apenas a fonte única configurada
    for nome, url in fontes.items():
        print(f"Baixando e processando: {nome}...")
        conteudo = baixar_xml(url)
        
        if conteudo:
            try:
                temp_root = ET.fromstring(conteudo)
                
                # Adiciona todos os canais
                for canal in temp_root.findall('channel'):
                    root.append(canal)
                
                # Adiciona todos os programas
                for programa in temp_root.findall('programme'):
                    root.append(programa)
                    
            except Exception as e:
                print(f"Erro ao processar XML de {nome}: {e}")
    
    tree = ET.ElementTree(root)
    tree.write("epg_completo.xml", encoding="utf-8", xml_declaration=True)
    print("Sucesso: epg_completo.xml (apenas Share) gerado com sucesso!")

if __name__ == "__main__":
    gerar_epg_unificado()
