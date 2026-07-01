import xml.etree.ElementTree as ET

def filtrar_grade_com_programacao():
    print("Iniciando filtragem completa (canais e programas)...")
    
    try:
        # Lê o arquivo de origem completo
        tree = ET.parse('epg_origem.xml')
        root = tree.getroot()
        
        # Cria a nova estrutura
        novo_root = ET.Element("tv", {"generator-info-name": "Lourival26-Grade-Claro-Completa"})
        
        # Identifica IDs de canais que terminam com .br
        ids_validos = set()
        for canal in root.findall('channel'):
            canal_id = canal.attrib.get('id', '')
            if '.br' in canal_id:
                ids_validos.add(canal_id)
                novo_root.append(canal)
        
        # Filtra apenas os programas dos canais que foram selecionados
        for programa in root.findall('programme'):
            canal_ref = programa.attrib.get('channel', '')
            if canal_ref in ids_validos:
                novo_root.append(programa)
                
        # Salva o arquivo final
        ET.ElementTree(novo_root).write("epg_completo.xml", encoding="utf-8", xml_declaration=True)
        print("Arquivo epg_completo.xml gerado com sucesso com grade e canais!")
        
    except Exception as e:
        print(f"Erro ao processar arquivo: {e}")

if __name__ == "__main__":
    filtrar_grade_com_programacao()
