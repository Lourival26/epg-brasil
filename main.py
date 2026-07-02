import requests
import xml.etree.ElementTree as ET

def gerar_epg_combinado():
    # Fontes configuradas: Share + Pluto TV + IPTV-ORG (Telecine/Geral)
    links = [
        "COLE_SEU_LINK_SHARE_AQUI",
        "https://raw.githubusercontent.com/iptv-org/epg/master/channels/br/pluto.tv.xml",
        "https://raw.githubusercontent.com/iptv-org/epg/master/channels/br/telecine.xml"
    ]
    
    try:
        # 1. Carrega seu esqueleto (epg.xml)
        meu_esqueleto = ET.parse('epg.xml')
        root_meu = meu_esqueleto.getroot()
        root_meu.set("generator-info-name", "Lourival26")
        
        # Cria uma lista de IDs para busca rápida
        meus_ids = {canal.attrib.get('id') for canal in root_meu.findall('channel')}
        
        # 2. Processa cada fonte
        total_progs = 0
        for url in links:
            print(f"Baixando: {url}")
            try:
                response = requests.get(url, timeout=30)
                if response.status_code == 200:
                    root_fonte = ET.fromstring(response.content)
                    for prog in root_fonte.findall('programme'):
                        # Verifica se o programa pertence a um dos seus canais
                        if prog.attrib.get('channel') in meus_ids:
                            root_meu.append(prog)
                            total_progs += 1
            except Exception as sub_e:
                print(f"Erro ao processar a fonte {url}: {sub_e}")
        
        # 3. Salva o resultado final
        meu_esqueleto.write("epg_completo.xml", encoding="utf-8", xml_declaration=True)
        print(f"Sucesso! {total_progs} programas combinados para Lourival26.")
        
    except Exception as e:
        print(f"Erro ao combinar: {e}")

if __name__ == "__main__":
    gerar_epg_combinado()
