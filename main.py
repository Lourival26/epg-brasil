import xml.etree.ElementTree as ET

def filtrar_grade_otimizado():
    print("Iniciando filtragem otimizada...")
    try:
        # Usamos iterparse para não carregar o arquivo gigante inteiro na memória
        context = ET.iterparse('epg.xml', events=('start', 'end'))
        novo_root = ET.Element("tv", {"generator-info-name": "Lourival26-Otimizado"})
        
        ids_validos = set()
        # Primeiro passo: encontrar apenas os canais
        for event, elem in context:
            if event == 'end' and elem.tag == 'channel':
                canal_id = elem.attrib.get('id', '')
                if '.br' in canal_id:
                    ids_validos.add(canal_id)
                    novo_root.append(elem)
            # Segundo passo: encontrar apenas os programas válidos
            elif event == 'end' and elem.tag == 'programme':
                canal_ref = elem.attrib.get('channel', '')
                if canal_ref in ids_validos:
                    novo_root.append(elem)
        
        ET.ElementTree(novo_root).write("epg_completo.xml", encoding="utf-8", xml_declaration=True)
        print("Arquivo gerado com sucesso!")
    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    filtrar_grade_otimizado()
