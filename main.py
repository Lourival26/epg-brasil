import requests
import xml.etree.ElementTree as ET

def diagnostico_epg():
    url_fonte = "https://raw.githubusercontent.com/limaalef/BrazilTVEPG/refs/heads/main/claro.xml"
    
    try:
        # Carrega o seu esqueleto
        meu_esqueleto = ET.parse('epg.xml')
        meus_ids = [canal.attrib.get('id') for canal in meu_esqueleto.findall('channel')]
        
        # Baixa a fonte
        response = requests.get(url_fonte)
        root_fonte = ET.fromstring(response.content)
        
        # Verifica quantos programas existem para os seus IDs
        contagem = 0
        for prog in root_fonte.findall('programme'):
            if prog.attrib.get('channel') in meus_ids:
                contagem += 1
        
        print(f"Diagnóstico: Encontrei {contagem} programas para os seus canais.")
        
        if contagem == 0:
            print("Alerta: Os IDs do seu epg.xml não batem com os da fonte. Verifique se não há espaços extras ou diferenças de maiúsculas.")
            print(f"Seus IDs: {meus_ids[:5]}...") # Mostra os primeiros para você comparar
            
    except Exception as e:
        print(f"Erro no diagnóstico: {e}")

if __name__ == "__main__":
    diagnostico_epg()
