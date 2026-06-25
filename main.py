import requests
import xml.etree.ElementTree as ET

# Fontes que entregam arquivos .xml diretos e possuem grade completa no Brasil
fontes = {
    "iptv_org": "https://iptv-org.github.io/epg/guides/br/brazil.xml",
    "pluto_tv": "https://i.mjh.nz/PlutoTV/br.xml"
}

# URL do EPG da Claro - TROCA AQUI pela URL correta
URL_CLARO = "https://iptv-org.github.io/epg/guides/br/claro.xml"

def gerar_epg_unificado():
    # Cria a estrutura raiz do XML
    root = ET.Element("tv", {"generator-info-name": "Lourival026-EPG"})
    
    # Conjuntos para evitar duplicatas de canais
    canais_adicionados = set()

    for nome, url in fontes.items():
        print(f"Baixando e processando: {nome}...")
        try:
            # Baixa o XML da fonte
            resp = requests.get(url, timeout=60)
            if resp.status_code == 200:
                temp_root = ET.fromstring(resp.content)
                
                # Adiciona canais se ainda não existirem
                for canal in temp_root.findall('channel'):
                    canal_id = canal.get('id')
                    if canal_id not in canais_adicionados:
                        root.append(canal)
                        canais_adicionados.add(canal_id)
                
                # Adiciona todos os programas encontrados
                for programa in temp_root.findall('programme'):
                    root.append(programa)
                    
            else:
                print(f"Erro ao baixar {nome}: Status {resp.status_code}")
        except Exception as e:
            print(f"Erro ao processar {nome}: {e}")

    # Salva o arquivo final
    tree = ET.ElementTree(root)
    tree.write("epg_completo.xml", encoding="utf-8", xml_declaration=True)
    print("Sucesso: epg_completo.xml gerado com sucesso!")

def gerar_epg_claro():
    print("Baixando e gerando: claro...")
    try:
        resp = requests.get(URL_CLARO, timeout=60)
        if resp.status_code == 200:
            with open("claro.xml", "wb") as f:
                f.write(resp.content)
            print("Sucesso: claro.xml gerado com sucesso!")
        else:
            print(f"Erro ao baixar Claro: Status {resp.status_code}")
    except Exception as e:
        print(f"Erro ao processar Claro: {e}")

if __name__ == "__main__":
    gerar_epg_unificado()  # gera epg_completo.xml com iptv_org + pluto_tv
    gerar_epg_claro()      # gera claro.xml separado
