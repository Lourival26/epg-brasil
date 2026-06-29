import xml.etree.ElementTree as ET

def filtrar_grade_claro():
    print("Iniciando filtro de canais para Lourival26...")
    
    try:
        # Lê o seu arquivo original (ajuste o nome para 'epg.xml' se for esse o seu arquivo)
        tree = ET.parse('epg.xml')
        root = tree.getroot()
        
        # Cria a nova estrutura mantendo seu identificador
        novo_root = ET.Element("tv", {"generator-info-name": "Lourival26"})
        
        # Filtra apenas os canais que possuem '.br' no id
        # E já adiciona a programação correspondente a eles
        ids_validos = set()
        
        # Primeiro, identifica os canais
        for canal in root.findall('channel'):
            canal_id = canal.attrib.get('id', '')
            if '.br' in canal_id:
                novo_root.append(canal)
                ids_validos.add(canal_id)
        
        # Segundo, adiciona a programação apenas para esses canais
        for programa in root.findall('programme'):
            if programa.attrib.get('channel') in ids_validos:
                novo_root.append(programa)
                
        # Salva o arquivo final que o seu app vai ler
        ET.ElementTree(novo_root).write("epg_completo.xml", encoding="utf-8", xml_declaration=True)
        print("Arquivo epg_completo.xml gerado com sucesso!")
        
    except Exception as e:
        print(f"Erro ao processar arquivo: {e}")

if __name__ == "__main__":
    filtrar_grade_claro()
