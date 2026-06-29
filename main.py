import xml.etree.ElementTree as ET

def filtrar_grade_local():
    print("Iniciando filtragem e geração do EPG...")
    
    try:
        # Lê o arquivo fonte
        tree = ET.parse('epg.xml')
        root = tree.getroot()
        
        # Cria a estrutura do novo arquivo
        novo_root = ET.Element("tv", {"generator-info-name": "Lourival26-Grade-Completa"})
        
        ids_processados = set()
        nomes_processados = set()
        
        # Primeiro, filtra e adiciona os canais
        canais_validos = []
        for canal in root.findall('channel'):
            canal_id = canal.attrib.get('id', '')
            display_name = canal.find('display-name')
            nome = display_name.text if display_name is not None else ""
            
            # Filtro: precisa ter .br E não ser duplicado
            if '.br' in canal_id and canal_id not in ids_processados and nome not in nomes_processados:
                novo_root.append(canal)
                ids_processados.add(canal_id)
                nomes_processados.add(nome)
                canais_validos.append(canal_id)
        
        # Segundo, adiciona a grade de programação (o que está passando) apenas dos canais filtrados
        for programa in root.findall('programme'):
            if programa.attrib.get('channel') in ids_processados:
                novo_root.append(programa)
        
        # Salva o resultado final
        tree_final = ET.ElementTree(novo_root)
        tree_final.write("epg_completo.xml", encoding="utf-8", xml_declaration=True)
        print(f"Sucesso! {len(ids_processados)} canais brasileiros processados com a programação.")
        
    except Exception as e:
        print(f"Erro ao processar: {e}")

if __name__ == "__main__":
    filtrar_grade_local()
