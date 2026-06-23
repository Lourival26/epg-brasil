# Definindo o conteúdo do seu XML
xml_header = '<?xml version="1.0" encoding="UTF-8"?>\n<tv generator-info-name="Lourival026">\n'
xml_footer = '</tv>'

# Lista de canais
canais = """
  <channel id="Globo.RJ"><display-name lang="pt">Globo RJ HD</display-name></channel>
  <channel id="Globo.SP"><display-name lang="pt">Globo SP HD</display-name></channel>
  <channel id="Globo.Nordeste"><display-name lang="pt">Globo Nordeste HD</display-name></channel>
  <channel id="Globo.MT"><display-name lang="pt">Globo MT HD</display-name></channel>
  <channel id="Globo.MG"><display-name lang="pt">Globo MG HD</display-name></channel>
  <channel id="Globo.MG2"><display-name lang="pt">Globo MG HD²</display-name></channel>
  <channel id="RPC.Curitiba"><display-name lang="pt">RPC Curitiba HD</display-name></channel>
  <channel id="RBS.POA"><display-name lang="pt">RBS TV Porto Alegre HD</display-name></channel>
  <channel id="RPC.Maringa"><display-name lang="pt">RPC Maringa FH</display-name></channel>
  <channel id="Globo.Goias"><display-name lang="pt">Globo Goiás HD</display-name></channel>
  <channel id="Globo.Manaus"><display-name lang="pt">Globo Manaus HD</display-name></channel>
  <channel id="Rede.Amazonica.PV"><display-name lang="pt">Rede Amazonica Porto Velho HD</display-name></channel>
  <channel id="Globo.Liberal"><display-name lang="pt">Globo TV Liberal Belém</display-name></channel>
"""

# Junta tudo e salva
with open("epg.xml", "w", encoding="utf-8") as f:
    f.write(xml_header + canais + xml_footer)

print("Arquivo epg.xml gerado com sucesso!")
