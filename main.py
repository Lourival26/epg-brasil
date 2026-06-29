import xml.etree.ElementTree as ET

def filtrar_grade_local():
    print("Iniciando filtragem ultra-rápida...")
    try:
        # Lendo o 'epg.xml' que está na pasta do seu GitHub
        tree = ET.parse('epg.xml')
        root = tree.getroot()
        
        # Cria a nova estrutura limpa
        novo_root = ET.Element("tv", {"generator-info-name": "Lourival26-Grade-Claro-Otimizada"})
        
        ids_br = set()
        nomes_processados = set()
        
        # 1. Filtra e adiciona apenas os canais .br sem duplicados
        for canal in root.findall('channel'):
            canal_id = canal.attrib.get('id', '')
            display_name = canal.find('display-name')
            nome = display_name.text if display_name is not None else ""
            
            if '.br' in canal_id and canal_id not in ids_br and nome not in nomes_processados:
                novo_root.append(canal)
                ids_br.add(canal_id)
                nomes_processados.add(nome)
        
        # 2. Adiciona a programação de forma super leve e rápida
        # Passando direto pelos elementos para não consumir a memória do GitHub e não travar
        for elemento in root:
            if elemento.tag == 'programme':
                canal_id = elemento.attrib.get('channel', '')
                if canal_id in ids_br:
                    novo_root.append(elemento)
        
        # Salva o arquivo final limpo e completo
        ET.ElementTree(novo_root).write("epg_completo.xml", encoding="utf-8", xml_declaration=True)
        print("Sucesso! O arquivo epg_completo.xml foi gerado com a programação de forma super rápida.")
        
    except Exception as e:
        print(f"Erro ao processar: {e}")

if __name__ == "__main__":
    filtrar_grade_local()
