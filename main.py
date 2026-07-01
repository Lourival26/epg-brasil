import requests
import xml.etree.ElementTree as ET

def gerar_epg():
    url = "https://raw.githubusercontent.com/limaalef/BrazilTVEPG/refs/heads/main/claro.xml"
    
    try:
        # Baixa a grade
        response = requests.get(url)
        if response.status_code == 200:
            root = ET.fromstring(response.content)
            
            # Cria a estrutura raiz do XML
            novo_root = ET.Element("tv", {"generator-info-name": "Lourival26-Grade-Claro"})
            
            # Adiciona canais e programas com filtro .br
            count = 0
            for canal in root.findall('channel'):
                if '.br' in canal.attrib.get('id', ''):
                    novo_root.append(canal)
                    count += 1
            
            for prog in root.findall('programme'):
                if '.br' in prog.attrib.get('channel', ''):
                    novo_root.append(prog)
            
            # Salva o arquivo
            tree = ET.ElementTree(novo_root)
            tree.write("epg.xml", encoding="utf-8", xml_declaration=True)
            print(f"Sucesso! {count} canais processados.")
        else:
            print("Erro ao baixar o arquivo.")
    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    gerar_epg()
