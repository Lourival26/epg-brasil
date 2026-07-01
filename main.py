import xml.etree.ElementTree as ET

def filtrar_grade_local():
    print("Iniciando filtragem para Lourival26...")
    
    try:
        # Lê o arquivo que você criou no repositório
        tree = ET.parse('epg_origem.xml')
        root = tree.getroot()
        
        # Cria a nova estrutura com seu nome
        novo_root = ET.Element("tv", {"generator-info-name": "Lourival26-Grade-Claro"})
        
        # Filtra apenas os canais que possuem '.br' no id
        # Como o seu XML enviado só tem <channel>, o script vai filtrar esses
        for canal in root.findall('channel'):
            canal_id = canal.attrib.get('id', '')
            if '.br' in canal_id:
                novo_root.append(canal)
                
        # Salva o resultado
        ET.ElementTree(novo_root).write("epg_completo.xml", encoding="utf-8", xml_declaration=True)
        print("Arquivo epg_completo.xml gerado com sucesso para Lourival26!")
        
    except Exception as e:
        print(f"Erro ao processar arquivo: {e}")

if __name__ == "__main__":
    filtrar_grade_local()
