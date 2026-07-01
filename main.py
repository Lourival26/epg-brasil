import xml.etree.ElementTree as ET

def filtrar_grade_definitivo():
    print("Iniciando filtragem completa...")
    try:
        # Carrega o XML original
        tree = ET.parse('epg.xml')
        root = tree.getroot()
        
        # Cria o novo arquivo XML
        novo_root = ET.Element("tv", {"generator-info-name": "Lourival26-Completo"})
        
        # 1. Adiciona apenas os canais que terminam com .br
        ids_validos = set()
        for canal in root.findall('channel'):
            canal_id = canal.attrib.get('id', '')
            if '.br' in canal_id:
                ids_validos.add(canal_id)
                novo_root.append(canal)
        
        # 2. Adiciona APENAS os programas que pertencem a esses canais
        for programa in root.findall('programme'):
            canal_ref = programa.attrib.get('channel', '')
            if canal_ref in ids_validos:
                novo_root.append(programa)
        
        # Salva o arquivo final
        ET.ElementTree(novo_root).write("epg_completo.xml", encoding="utf-8", xml_declaration=True)
        print("Arquivo gerado com sucesso com canais E programas!")
    except Exception as e:
        print(f"Erro ao processar: {e}")

if __name__ == "__main__":
    filtrar_grade_definitivo()
