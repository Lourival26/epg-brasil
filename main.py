import xml.etree.ElementTree as ET

def filtrar_grade_local():
    print("Iniciando filtragem para Lourival26...")
    
    try:
        # Lê o arquivo de origem
        tree = ET.parse('epg_origem.xml')
        root = tree.getroot()
        
        # Cria a nova estrutura
        novo_root = ET.Element("tv", {"generator-info-name": "Lourival26-Grade-Claro"})
        
        # --- NOVIDADE: Conjunto para guardar IDs já adicionados ---
        canais_adicionados = set()
        
        for canal in root.findall('channel'):
            canal_id = canal.attrib.get('id', '')
            
            # Filtra pelo '.br' E verifica se o ID ainda não foi adicionado
            if '.br' in canal_id and canal_id not in canais_adicionados:
                novo_root.append(canal)
                canais_adicionados.add(canal_id) # Marca este ID como processado
        
        # Salva o resultado
        ET.ElementTree(novo_root).write("epg_completo.xml", encoding="utf-8", xml_declaration=True)
        print(f"Arquivo epg_completo.xml gerado com sucesso! {len(canais_adicionados)} canais únicos processados.")
        
    except Exception as e:
        print(f"Erro ao processar arquivo: {e}")

if __name__ == "__main__":
    filtrar_grade_local()
