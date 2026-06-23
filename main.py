import requests
import xml.etree.ElementTree as ET

# Fontes que possuem a grade de programação completa
fontes = {
    "iptv_org": "https://iptv-org.github.io/epg/guides/br/brazil.xml",
    "pluto_tv": "https://i.mjh.nz/PlutoTV/br.xml"
}

def gerar_epg_unificado():
    # Cria a estrutura base do XML
    root = ET.Element("tv", {"generator-info-name": "Lourival026-EPG"})
    
    for nome, url in fontes.items():
        print(f"Baixando grade de: {nome}...")
        try:
            resp = requests.get(url, timeout=45)
            if resp.status_code == 200:
                # Carrega o XML da fonte
                temp_root = ET.fromstring(resp.content)
                # Adiciona todos os canais e programas ao nosso arquivo principal
                for elemento in temp_root:
                    root.append(elemento)
        except Exception as e:
            print(f"Erro ao baixar {nome}: {e}")

    # Salva tudo em um único arquivo chamado epg_completo.xml
    tree = ET.ElementTree(root)
    tree.write("epg_completo.xml", encoding="utf-8", xml_declaration=True)
    print("Sucesso: epg_completo.xml gerado com todos os canais e grades!")

if __name__ == "__main__":
    gerar_epg_unificado()
