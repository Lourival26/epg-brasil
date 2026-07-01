import xml.etree.ElementTree as ET
import requests

def processar_epg_claro():
    url = "https://raw.githubusercontent.com/limaalef/BrazilTVEPG/refs/heads/main/claro.xml"
    print(f"Baixando EPG de: {url}")
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        # Faz o parse
        root = ET.fromstring(response.content)
        
        # FORÇANDO A ALTERAÇÃO DO NOME DO GERADOR
        root.set("generator-info-name", "Lourival26-Completo")
        
        # Cria a estrutura nova para filtrar
        novo_root = ET.Element("tv", {"generator-info-name": "Lourival26-Completo"})
        
        # Filtra canais .br
        ids_validos = set()
        for canal in root.findall('channel'):
            canal_id = canal.attrib.get('id', '')
            if '.br' in canal_id:
                ids_validos.add(canal_id)
                novo_root.append(canal)
        
        # Filtra programas
        encontrou_programas = 0
        for programa in root.findall('programme'):
            canal_ref = programa.attrib.get('channel', '')
            if canal_ref in ids_validos:
                novo_root.append(programa)
                encontrou_programas += 1
        
        print(f"Programas encontrados e adicionados: {encontrou_programas}")
        
        # Salva
        tree = ET.ElementTree(novo_root)
        tree.write("epg_completo.xml", encoding="utf-8", xml_declaration=True)
        
    except Exception as e:
        print(f"Erro ao processar: {e}")

if __name__ == "__main__":
    processar_epg_claro()
