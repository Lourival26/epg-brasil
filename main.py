import xml.etree.ElementTree as ET

def filtrar_grade_local():
    print("Iniciando limpeza e geração do EPG...")
    
    try:
        # Lendo o arquivo epg.xml que você tem no repositório
        tree = ET.parse('epg.xml')
        root = tree.getroot()
        
        # Criando a estrutura do novo arquivo
        novo_root = ET.Element("tv", {"generator-info-name": "Lourival26-Grade-Limpa"})
        
        ids_processados = set()
        nomes_processados = set()
        
        for canal in root.findall('channel'):
            canal_id = canal.attrib.get('id', '')
            display_name = canal.find('display-name')
            nome = display_name.text if display_name is not None else ""
            
            # Filtro de unicidade
            if canal_id not in ids_processados and nome not in nomes_processados:
                novo_root.append(canal)
                ids_processados.add(canal_id)
                nomes_processados.add(nome)
        
        # Salvando o arquivo final
        tree_final = ET.ElementTree(novo_root)
        tree_final.write("epg_completo.xml", encoding="utf-8", xml_declaration=True)
        print(f"Sucesso! {len(ids_processados)} canais únicos salvos em epg_completo.xml")
        
    except Exception as e:
        print(f"Erro ao processar: {e}")

if __name__ == "__main__":
    filtrar_grade_local()
