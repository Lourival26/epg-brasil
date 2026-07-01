import requests
import xml.etree.ElementTree as ET

def gerar_epg():
    # Fonte da grade completa da Claro
    url_fonte = "https://raw.githubusercontent.com/limaalef/BrazilTVEPG/refs/heads/main/claro.xml"
    print("Baixando grade da Claro TV...")
    
    try:
        response = requests.get(url_fonte)
        root = ET.fromstring(response.content)
        
        # Cria a estrutura com o seu nome personalizado
        novo_root = ET.Element("tv", {"generator-info-name": "Lourival26-Grade-Claro"})
        
        print("Filtrando canais e programas...")
        
        # Filtra os canais que terminam com .br
        for canal in root.findall('channel'):
            canal_id = canal.attrib.get('id', '')
            if '.br' in canal_id:
                novo_root.append(canal)
        
        # Filtra os programas que pertencem a esses canais
        for prog in root.findall('programme'):
            prog_channel = prog.attrib.get('channel', '')
            if '.br' in prog_channel:
                novo_root.append(prog)
                
        # Salva o arquivo epg.xml na raiz do seu repositório
        tree = ET.ElementTree(novo_root)
        tree.write("epg.xml", encoding="utf-8", xml_declaration=True)
        print("EPG gerado com sucesso!")
        
    except Exception as e:
        print(f"Erro ao processar: {e}")

if __name__ == "__main__":
    gerar_epg()
