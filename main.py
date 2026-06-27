import requests
import xml.etree.ElementTree as ET
import gzip
import io

# URL da fonte
URL_SHARE = "https://epgshare01.online/epgshare01/epg_ripper_ALL_SOURCES1.xml.gz"

# LISTA DE IDs QUE VOCÊ QUER MANTER (Exemplos, ajuste com os IDs dos seus canais)
canais_desejados = {"canal1.id", "canal2.id"} 

def processar_epg():
    print("Baixando arquivo...")
    resp = requests.get(URL_SHARE, timeout=60)
    
    if resp.status_code == 200:
        buffer = io.BytesIO(resp.content)
        with gzip.GzipFile(fileobj=buffer) as f:
            tree = ET.parse(f)
            root = tree.getroot()
            
            # Novo XML enxuto
            novo_root = ET.Element("tv")
            
            # Filtra apenas os canais e programas da lista
            for canal in root.findall('channel'):
                if canal.attrib.get('id') in canais_desejados:
                    novo_root.append(canal)
            
            for prog in root.findall('programme'):
                if prog.attrib.get('channel') in canais_desejados:
                    novo_root.append(prog)
            
            # Salva o arquivo pequeno
            tree_final = ET.ElementTree(novo_root)
            tree_final.write("epg_completo.xml", encoding="utf-8", xml_declaration=True)
            print("Arquivo filtrado e salvo com sucesso!")

if __name__ == "__main__":
    processar_epg()
