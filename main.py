import xml.etree.ElementTree as ET
import gzip
import io
import requests

def gerar_epg_claro():
    url = "https://epgshare01.online/epgshare01/epg_ripper_ALL_SOURCES1.xml.gz"
    print("Baixando e filtrando canais Claro/Brasil...")
    resp = requests.get(url, timeout=120)
    
    with gzip.GzipFile(fileobj=io.BytesIO(resp.content)) as f:
        tree = ET.parse(f)
        root = tree.getroot()
        
        # Aqui inserimos o seu nome na identificação do arquivo
        novo_root = ET.Element("tv", {"generator-info-name": "Lourival26-EPG-Custom"})
        
        # Filtra apenas canais que contêm '.br' no ID
        canais_validos = set()
        for canal in root.findall('channel'):
            canal_id = canal.attrib.get('id', '')
            if '.br' in canal_id: 
                novo_root.append(canal)
                canais_validos.add(canal_id)
                
        # Filtra programas apenas para esses canais
        for prog in root.findall('programme'):
            if prog.attrib.get('channel') in canais_validos:
                novo_root.append(prog)
        
        # Salva o arquivo final
        ET.ElementTree(novo_root).write("epg_completo.xml", encoding="utf-8", xml_declaration=True)
        print("Arquivo filtrado para Lourival26 gerado com sucesso!")

if __name__ == "__main__":
    gerar_epg_claro()
