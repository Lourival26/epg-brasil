import requests
import xml.etree.ElementTree as ET

def gerar_epg_completo():
    try:
        # 1. Carrega o seu esqueleto fixo (o epg.xml que você já tem)
        esqueleto = ET.parse('epg.xml')
        root_esqueleto = esqueleto.getroot()
        
        # 2. Baixa a grade completa da internet
        url = "https://raw.githubusercontent.com/limaalef/BrazilTVEPG/refs/heads/main/claro.xml"
        response = requests.get(url)
        root_fonte = ET.fromstring(response.content)
        
        # 3. Cria a estrutura do arquivo completo
        # Mantemos o nome original do seu gerador
        novo_root = ET.Element("tv", {"generator-info-name": "Lourival26"})
        
        # Copia todos os canais do seu esqueleto para o novo arquivo
        for canal in root_esqueleto.findall('channel'):
            novo_root.append(canal)
            
        # Pega a lista de IDs dos seus canais
        ids_meus_canais = [canal.attrib['id'] for canal in root_esqueleto.findall('channel')]
        
        # 4. Só copia o programa se o ID do canal estiver na sua lista
        for prog in root_fonte.findall('programme'):
            if prog.attrib.get('channel') in ids_meus_canais:
                novo_root.append(prog)
        
        # 5. Salva como epg_completo.xml
        tree = ET.ElementTree(novo_root)
        tree.write("epg_completo.xml", encoding="utf-8", xml_declaration=True)
        print("Arquivo epg_completo.xml gerado com sucesso!")
        
    except Exception as e:
        print(f"Erro ao gerar o EPG: {e}")

if __name__ == "__main__":
    gerar_epg_completo()
