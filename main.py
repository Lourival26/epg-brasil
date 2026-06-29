import xml.etree.ElementTree as ET

def filtrar_grade_completa():
    print("Iniciando filtragem completa (Canais + Programação) para Lourival26...")
    
    try:
        tree = ET.parse('epg_origem.xml')
        root = tree.getroot()
        
        novo_root = ET.Element("tv", {"generator-info-name": "Lourival26-Grade-Completa"})
        
        # 1. Filtra os canais e guarda os IDs válidos
        ids_validos = set()
        for canal in root.findall('channel'):
            if '.br' in canal.attrib.get('id', ''):
                novo_root.append(canal)
                ids_validos.add(canal.attrib.get('id'))
        
        # 2. O QUE FALTAVA: Filtra apenas a programação dos canais que salvamos
        for programa in root.findall('programme'):
            canal_do_programa = programa.attrib.get('channel', '')
            if canal_do_programa in ids_validos:
                novo_root.append(programa)
                
        ET.ElementTree(novo_root).write("epg_completo.xml", encoding="utf-8", xml_declaration=True)
        print("Guia completo gerado com sucesso!")
        
    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    filtrar_grade_completa()
