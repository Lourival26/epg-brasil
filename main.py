import requests
import xml.etree.ElementTree as ET

def filtrar_grade_local():
    print("Iniciando filtragem para Lourival26...")
    
    try:
        # AQUI FOI A MUDANÇA: O robô baixa a grade completa da Claro primeiro
        url = "https://raw.githubusercontent.com/limaalef/BrazilTVEPG/refs/heads/main/claro.xml"
        response = requests.get(url)
        root = ET.fromstring(response.content)
        
        # Cria a nova estrutura com seu nome
        novo_root = ET.Element("tv", {"generator-info-name": "Lourival26-Grade-Claro"})
        
        # Filtra apenas os canais que possuem '.br' no id
        for canal in root.findall('channel'):
            canal_id = canal.attrib.get('id', '')
            if '.br' in canal_id:
                novo_root.append(canal)
                
        # Filtra os programas (para não esquecer os horários e nomes)
        for prog in root.findall('programme'):
            if '.br' in prog.attrib.get('channel', ''):
                novo_root.append(prog)
                
        # Salva o resultado como epg.xml (o nome que você usa no player)
        ET.ElementTree(novo_root).write("epg.xml", encoding="utf-8", xml_declaration=True)
        print("Arquivo epg.xml gerado com sucesso para Lourival26!")
        
    except Exception as e:
        print(f"Erro ao processar: {e}")

if __name__ == "__main__":
    filtrar_grade_local()
