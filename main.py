import requests
import xml.etree.ElementTree as ET

def processar_epg():
    url = "https://raw.githubusercontent.com/Lourival26/epg-brasil/refs/heads/main/epg.xml"
    response = requests.get(url)
    root = ET.fromstring(response.content)
    
    novo_root = ET.Element("tv", {"generator-info-name": "Lourival26-Final"})
    
    # Dicionário para garantir que cada canal seja adicionado apenas UMA vez
    canais_adicionados = {}
    
    # 1. Filtra canais únicos
    for canal in root.findall('channel'):
        c_id = canal.get('id')
        if c_id not in canais_adicionados:
            novo_root.append(canal)
            canais_adicionados[c_id] = True
            
    # 2. Filtra programas apenas para os canais que foram aceitos
    for programa in root.findall('programme'):
        if programa.get('channel') in canais_adicionados:
            novo_root.append(programa)
    
    ET.ElementTree(novo_root).write("epg_completo.xml", encoding="utf-8", xml_declaration=True)

if __name__ == "__main__":
    processar_epg()
