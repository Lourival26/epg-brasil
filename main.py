import requests
import xml.etree.ElementTree as ET

def diagnostico_ids():
    # Apenas as fontes públicas para teste
    links = [
        "https://raw.githubusercontent.com/iptv-org/epg/master/channels/br/telecine.xml"
    ]
    
    try:
        meu_esqueleto = ET.parse('epg.xml')
        meus_ids = {canal.attrib.get('id') for canal in meu_esqueleto.findall('channel')}
        
        print(f"IDs que você tem no epg.xml: {list(meus_ids)[:3]}...")
        
        for url in links:
            response = requests.get(url)
            root_fonte = ET.fromstring(response.content)
            
            # Conta quantos programas existem para os seus IDs
            encontrados = 0
            for prog in root_fonte.findall('programme'):
                if prog.attrib.get('channel') in meus_ids:
                    encontrados += 1
            
            print(f"Na fonte {url}, encontrei {encontrados} programas para os seus IDs.")
            
    except Exception as e:
        print(f"Erro no diagnóstico: {e}")

if __name__ == "__main__":
    diagnostico_ids()
