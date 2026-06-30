import xml.etree.ElementTree as ET

def gerar_grade_unica():
    tree = ET.parse('epg.xml')
    root = tree.getroot()
    
    novo_root = ET.Element("tv", {"generator-info-name": "Lourival26-Limpo"})
    
    canais_processados = set()
    
    # Filtra canais garantindo que cada ID apareça apenas uma vez
    for canal in root.findall('channel'):
        canal_id = canal.get('id')
        if canal_id not in canais_processados:
            novo_root.append(canal)
            canais_processados.add(canal_id)
            
    # Filtra programas apenas para os canais que foram mantidos
    for programa in root.findall('programme'):
        if programa.get('channel') in canais_processados:
            novo_root.append(programa)
                
    ET.ElementTree(novo_root).write("epg_completo.xml", encoding="utf-8", xml_declaration=True)

if __name__ == "__main__":
    gerar_grade_unica()
