import requests
import xml.etree.ElementTree as ET

# Adicionamos a fonte do Brazuca Play aqui
fontes = {
    "iptv_org": "https://iptv-org.github.io/epg/guides/br/brazil.xml",
    "pluto_tv": "https://i.mjh.nz/PlutoTV/br.xml",
    "brazuca_play": "LINK_DA_FONTE_BRAZUCA" # Substitua pelo link correto do XML
}

def gerar_epg_unificado():
    root = ET.Element("tv", {"generator-info-name": "Lourival026-EPG"})
    canais_adicionados = set()

    for nome, url in fontes.items():
        print(f"Processando: {nome}...")
        try:
            resp = requests.get(url, timeout=45)
            if resp.status_code == 200:
                temp_root = ET.fromstring(resp.content)
                
                # Adiciona canais
                for canal in temp_root.findall('channel'):
                    canal_id = canal.get('id')
                    if canal_id not in canais_adicionados:
                        root.append(canal)
                        canais_adicionados.add(canal_id)
                
                # Adiciona programas
                for programa in temp_root.findall('programme'):
                    root.append(programa)
                    
        except Exception as e:
            print(f"Erro ao processar {nome}: {e}")

    tree = ET.ElementTree(root)
    tree.write("epg_completo.xml", encoding="utf-8", xml_declaration=True)
    print("Sucesso: epg_completo.xml gerado com a nova fonte Brazuca Play!")

if __name__ == "__main__":
    gerar_epg_unificado()
