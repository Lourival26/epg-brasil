import xml.etree.ElementTree as ET
import re

def limpar_nome(nome):
    """Remove sufixos comuns para que 'Globo HD' e 'Globo' virem a mesma coisa."""
    nome = nome.upper()
    # Remove sufixos como HD, FHD, SD, etc.
    nome = re.sub(r'\s+(HD|FHD|SD|BR|TV|FHD²|HD²|FHD2)\s*$', '', nome)
    return nome.strip()

def filtrar_grade_local():
    print("Iniciando filtragem inteligente para Lourival26...")
    try:
        tree = ET.parse('epg.xml')
        root = tree.getroot()
        
        # Mantendo seu nome na estrutura do arquivo
        novo_root = ET.Element("tv", {"generator-info-name": "Lourival26"})
        
        canais_adicionados = {} 
        
        for canal in root.findall('channel'):
            display_name = canal.find('display-name')
            if display_name is not None:
                nome_bruto = display_name.text
                nome_limpo = limpar_nome(nome_bruto)
                
                if nome_limpo not in canais_adicionados:
                    novo_root.append(canal)
                    canais_adicionados[nome_limpo] = canal.attrib.get('id')
        
        ids_validos = set(canais_adicionados.values())
        for elemento in root.findall('programme'):
            if elemento.attrib.get('channel') in ids_validos:
                novo_root.append(elemento)
        
        ET.ElementTree(novo_root).write("epg_completo.xml", encoding="utf-8", xml_declaration=True)
        print("Sucesso! Arquivo epg_completo.xml gerado por Lourival26.")
        
    except Exception as e:
        print(f"Erro ao processar: {e}")

if __name__ == "__main__":
    filtrar_grade_local()
