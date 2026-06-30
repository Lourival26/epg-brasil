import requests
import xml.etree.ElementTree as ET

def processar_epg():
    url = "https://raw.githubusercontent.com/Lourival26/epg-brasil/refs/heads/main/epg.xml"
    print(f"Baixando EPG de: {url}")
    
    # 1. Baixar o arquivo
    response = requests.get(url)
    if response.status_code != 200:
        print("Erro ao baixar o arquivo!")
        return
    
    root = ET.fromstring(response.content)
    
    # 2. Criar estrutura do arquivo limpo
    novo_root = ET.Element("tv", {"generator-info-name": "Lourival26-Final"})
    
    canais_processados = set()
    
    # 3. Filtrar canais (mantém apenas o primeiro que encontrar)
    for canal in root.findall('channel'):
        canal_id = canal.get('id')
        if canal_id not in canais_processados:
            novo_root.append(canal)
            canais_processados.add(canal_id)
            
    # 4. Filtrar programas (apenas para canais que foram mantidos)
    for programa in root.findall('programme'):
        if programa.get('channel') in canais_processados:
            novo_root.append(programa)
    
    # 5. Salvar o resultado
    ET.ElementTree(novo_root).write("epg_completo.xml", encoding="utf-8", xml_declaration=True)
    print("epg_completo.xml gerado com sucesso sem duplicatas.")

if __name__ == "__main__":
    processar_epg()
