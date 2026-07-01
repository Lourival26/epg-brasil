import requests
import xml.etree.ElementTree as ET

def processar():
    url = "https://raw.githubusercontent.com/limaalef/BrazilTVEPG/refs/heads/main/claro.xml"
    print("Baixando...")
    response = requests.get(url)
    
    # Faz o parse do XML
    root = ET.fromstring(response.content)
    
    # Muda o nome
    root.set("generator-info-name", "Lourival26-Completo")
    
    # Salva o arquivo sem filtros, apenas para testar se aparece o conteúdo
    tree = ET.ElementTree(root)
    tree.write("epg_completo.xml", encoding="utf-8", xml_declaration=True)
    print("Arquivo gerado.")

if __name__ == "__main__":
    processar()
