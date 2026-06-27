import xml.etree.ElementTree as ET
import gzip
import io
import requests

# Defina aqui os IDs dos canais que você quer (coloque os IDs exatos da sua lista)
# Exemplo: canais_importantes = {"canal.exemplo1", "canal.exemplo2"}
canais_importantes = {"id_do_seu_canal_1", "id_do_seu_canal_2"} 

def filtrar_epg():
    url = "https://epgshare01.online/epgshare01/epg_ripper_ALL_SOURCES1.xml.gz"
    print("Baixando...")
    resp = requests.get(url, timeout=120)
    
    with gzip.GzipFile(fileobj=io.BytesIO(resp.content)) as f:
        tree = ET.parse(f)
        root = tree.getroot()
        
        # Cria um novo XML vazio
        novo_root = ET.Element("tv", {"generator-info-name": "Lourival26-EPG"})
        
        # Filtra Canais
        for canal in root.findall('channel'):
            if canal.attrib.get('id') in canais_importantes:
                novo_root.append(canal)
                
        # Filtra Programas
        for prog in root.findall('programme'):
            if prog.attrib.get('channel') in canais_importantes:
                novo_root.append(prog)
        
        # Salva o XML filtrado
        ET.ElementTree(novo_root).write("epg_completo.xml", encoding="utf-8", xml_declaration=True)
        print("Arquivo filtrado gerado com sucesso!")

if __name__ == "__main__":
    filtrar_epg()
