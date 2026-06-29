import xml.etree.ElementTree as ET

def filtrar_grade_local():
    print("Iniciando filtragem inteligente por nome...")
    try:
        tree = ET.parse('epg.xml')
        root = tree.getroot()
        
        novo_root = ET.Element("tv", {"generator-info-name": "Lourival26-Grade-Unificada"})
        
        # Agora vamos rastrear apenas pelo NOME do canal
        nomes_ja_adicionados = set()
        
        # 1. Filtra canais únicos pelo nome
        for canal in root.findall('channel'):
            display_name = canal.find('display-name')
            nome = display_name.text if display_name is not None else ""
            
            # Filtro: tem .br E o nome ainda não apareceu
            if '.br' in canal.attrib.get('id', '') and nome not in nomes_ja_adicionados:
                novo_root.append(canal)
                nomes_ja_adicionados.add(nome)
        
        # 2. Adiciona a programação, mas usamos uma lista de nomes válidos para filtrar
        # Isso garante que só entre a grade de canais que realmente salvamos
        for elemento in root:
            if elemento.tag == 'programme':
                canal_id = elemento.attrib.get('channel', '')
                
                # Procura o nome correspondente ao ID para saber se devemos manter
                canal_origem = root.find(f".//channel[@id='{canal_id}']")
                if canal_origem is not None:
                    nome_canal = canal_origem.find('display-name')
                    if nome_canal is not None and nome_canal.text in nomes_ja_adicionados:
                        novo_root.append(elemento)
        
        ET.ElementTree(novo_root).write("epg_completo.xml", encoding="utf-8", xml_declaration=True)
        print("Sucesso! Canais agrupados por nome e duplicatas removidas.")
        
    except Exception as e:
        print(f"Erro ao processar: {e}")

if __name__ == "__main__":
    filtrar_grade_local()
