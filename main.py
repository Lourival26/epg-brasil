import requests

# --- SUA LISTA ATUAL ---
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
  <channel id="SBT.News"><display-name lang="pt">SBT NEWS</display-name></channel>
  <channel id="Mais.SBT"><display-name lang="pt">+SBT HD</display-name></channel>
  <channel id="SBT.SP"><display-name lang="pt">SBT SP SD</display-name></channel>
  <channel id="SBT.Interior.SP"><display-name lang="pt">SBT Interior SP HD</display-name></channel>
  <channel id="TV.Difusora.SL"><display-name lang="pt">TV Difusora (SBT São Luís)</display-name></channel>
  <channel id="TV.Difusora.Leste"><display-name lang="pt">TV Difusora Leste</display-name></channel>
  <channel id="TV.Rio.Parnaiba"><display-name lang="pt">TV Rio Parnaíba Maranhão</display-name></channel>
  <channel id="SBT.Guajara"><display-name lang="pt">SBT Guajará</display-name></channel>
  <channel id="TV.Aratu"><display-name lang="pt">TV ARATU HD</display-name></channel>
  <channel id="SBT.Cidade.Verde"><display-name lang="pt">SBT CIDADE VERDE FHD</display-name></channel>
  <channel id="TVE.RS"><display-name lang="pt">TVE FHD</display-name></channel>
  <channel id="TV.Sonata"><display-name lang="pt">TV Sonata</display-name></channel>
  <channel id="Guia.TV"><display-name lang="pt">Guia TV</display-name></channel>
  <channel id="Rede.Brasil"><display-name lang="pt">Rede Brasil HD</display-name></channel>
  <channel id="TV.Brasil"><display-name lang="pt">TV BRASIL</display-name></channel>
  <channel id="TV.Brasil.ES"><display-name lang="pt">TV BRASIL ES</display-name></channel>
  <channel id="Rede.TV"><display-name lang="pt">Rede TV HD</display-name></channel>
  <channel id="Cultura.HD"><display-name lang="pt">Cultura HD</display-name></channel>
  <channel id="TV.Cultura.Brasil"><display-name lang="pt">TV Cultura Brasil</display-name></channel>
  <channel id="TV.Cultura.PA"><display-name lang="pt">TV Cultura Pará</display-name></channel>
  <channel id="Rede.Familia"><display-name lang="pt">Rede Família HD</display-name></channel>
  <channel id="TV.Gazeta.SP"><display-name lang="pt">TV Gazeta SP</display-name></channel>
  <channel id="TV.Aracati"><display-name lang="pt">TV Aracati HD</display-name></channel>
  <channel id="Amazon.Sat.SD"><display-name lang="pt">Amazon Sat SD</display-name></channel>
  <channel id="Amazon.Sat.HD"><display-name lang="pt">Amazon Sat HD</display-name></channel>
  <channel id="TVideonews"><display-name lang="pt">TVideonews HD</display-name></channel>
  <channel id="Rede.Minas"><display-name lang="pt">Rede Minas HD</display-name></channel>
  <channel id="TV.Camara"><display-name lang="pt">TV Câmara HD</display-name></channel>
  <channel id="Xtreme.TV"><display-name lang="pt">XTREME TV</display-name></channel>
  <channel id="Caravana.Play"><display-name lang="pt">Caravana Play</display-name></channel>
  <channel id="Adrenalina.Pura"><display-name lang="pt">ADRENALINA PURA TV</display-name></channel>
  <channel id="AW.TV"><display-name lang="pt">AW TV</display-name></channel>
  <channel id="Play.TV"><display-name lang="pt">Play TV</display-name></channel>
  <channel id="Gospel.Movies"><display-name lang="pt">Gospel Movies TV</display-name></channel>
  <channel id="Rede.CNT"><display-name lang="pt">Rede CNT HD</display-name></channel>
  <channel id="TV.Sul.Minas"><display-name lang="pt">TV Sul de Minas HD</display-name></channel>
  <channel id="CATVE.2"><display-name lang="pt">CATVE 2</display-name></channel>
  <channel id="TVE.RS.2"><display-name lang="pt">TVE RS</display-name></channel>
  <channel id="Primer.TV"><display-name lang="pt">Primer TV</display-name></channel>
  <channel id="TV.UFG"><display-name lang="pt">TV UFG</display-name></channel>
  <channel id="TV.Vicosa"><display-name lang="pt">TV Viçosa</display-name></channel>
  <channel id="TV.Grande.Natal"><display-name lang="pt">TV Grande Natal</display-name></channel>
  <channel id="Canal.Boi"><display-name lang="pt">Canal do Boi HD</display-name></channel>
  <channel id="Agro.Canal"><display-name lang="pt">Agro Canal</display-name></channel>
  <channel id="Agro.Mais"><display-name lang="pt">Agro + HD</display-name></channel>
  <channel id="Record.SP"><display-name lang="pt">RecordTV SP HD</display-name></channel>
  <channel id="Record.Nacional"><display-name lang="pt">RecordTV HD</display-name></channel>
  <channel id="Record.RJ"><display-name lang="pt">RecordTV RJ HD</display-name></channel>
  <channel id="Record.MG"><display-name lang="pt">RecordTV MG</display-name></channel>
  <channel id="Record.RJ.SD"><display-name lang="pt">RecordTV RJ SD</display-name></channel>
  <channel id="Record.MT"><display-name lang="pt">RecordTV MT</display-name></channel>
  <channel id="Record.RN"><display-name lang="pt">RecordTV RN</display-name></channel>
  <channel id="Record.Goias"><display-name lang="pt">RecordTV Goiás HD</display-name></channel>
  <channel id="Record.Conquista"><display-name lang="pt">RecordTV Conquista HD</display-name></channel>
  <channel id="Record.MT.HD"><display-name lang="pt">RecordTV Mato MT HD</display-name></channel>
  <channel id="Record.Juara"><display-name lang="pt">RecordTV Juara HD</display-name></channel>
  <channel id="TV.Tropical"><display-name lang="pt">TV Tropical HD</display-name></channel>
  <channel id="Record.SicTV"><display-name lang="pt">Record SicTV (RO)</display-name></channel>
  <channel id="TV.Brusque"><display-name lang="pt">TV BRUSQUE HD</display-name></channel>
  <channel id="Band.SP"><display-name lang="pt">Band SP HD</display-name></channel>
  <channel id="Band.RJ"><display-name lang="pt">Band RJ HD</display-name></channel>
  <channel id="Band.RS"><display-name lang="pt">Band RS</display-name></channel>
  <channel id="Band.Arapuan"><display-name lang="pt">Band Arapuan HD</display-name></channel>
  <channel id="Band.RBA"><display-name lang="pt">Band TV RBA TV</display-name></channel>
  <channel id="Band.Vale.Uruara"><display-name lang="pt">Band TV - Vale do Uruará</display-name></channel>
  <channel id="Band.MG"><display-name lang="pt">Band MG HD</display-name></channel>
  <channel id="Band.MT"><display-name lang="pt">Band Mato Grosso HD</display-name></channel>
  <channel id="New.Brasil"><display-name lang="pt">NEW BRASIL HD</display-name></channel>
  <channel id="Globo.News"><display-name lang="pt">Globo News FHD</display-name></channel>
  <channel id="Band.News"><display-name lang="pt">Band News HD</display-name></channel>
  <channel id="Record.News"><display-name lang="pt">Record News HD</display-name></channel>
  <channel id="ARTV.Portugal"><display-name lang="pt">ARTV Portugal HD</display-name></channel>
  <channel id="Pluto.TV.UOL"><display-name lang="pt">Pluto TV Canal UOL</display-name></channel>
  <channel id="CNN.Brasil.SD"><display-name lang="pt">CNN BRASIL SD</display-name></channel>
  <channel id="CNN.Brasil.HD"><display-name lang="pt">CNN BRASIL HD</display-name></channel>
  <channel id="CNN.Brasil.FHD"><display-name lang="pt">CNN BRASIL FHD</display-name></channel>
  <channel id="4.Por.4"><display-name lang="pt">4 POR 4</display-name></channel>
  <channel id="TV.Camara.HD"><display-name lang="pt">TV Câmara HD</display-name></channel>
  <channel id="TV.Camara.HD2"><display-name lang="pt">TV Câmara HD²</display-name></channel>
  <channel id="Canal.GOV"><display-name lang="pt">Canal GOV</display-name></channel>
  <channel id="TV.Videonews"><display-name lang="pt">TV VIDEONEWS</display-name></channel>
  <channel id="HTO.Kids"><display-name lang="pt">HTO KIDS HD</display-name></channel>
  <channel id="Leo.e.Lully"><display-name lang="pt">Léo e Lully HD</display-name></channel>
  <channel id="Popeye"><display-name lang="pt">Popeye HD</display-name></channel>
  <channel id="Moranguinho"><display-name lang="pt">Moranguinho HD</display-name></channel>
  <channel id="Toon.Goggles"><display-name lang="pt">Toon Goggles HD</display-name></channel>
  <channel id="Discovery.Kids"><display-name lang="pt">DISCOVERY KIDS HD</display-name></channel>
  <channel id="Kuriakos.Kids"><display-name lang="pt">Kuriakos Kids</display-name></channel>
  <channel id="Sonic"><display-name lang="pt">Sonic</display-name></channel>
  <channel id="Nickelodeon"><display-name lang="pt">Nickelodeon FHD</display-name></channel>
  <channel id="Nick.Jr"><display-name lang="pt">Nick jr. FHD</display-name></channel>
  <channel id="Gloobinho"><display-name lang="pt">GLOOBINHO HD</display-name></channel>
  <channel id="Gloob"><display-name lang="pt">GLOOB FHD</display-name></channel>
  <channel id="TV.Ra.Tim.Bum"><display-name lang="pt">TV RA TIM BUM HD</display-name></channel>
  <channel id="TV.Gallo"><display-name lang="pt">TV Gallo</display-name></channel>
  <channel id="Mr.Bean.Animated"><display-name lang="pt">Mr Bean Animated</display-name></channel>
  <channel id="Ministerio.Infantil.TV"><display-name lang="pt">Ministério Infantil TV</display-name></channel>
  <channel id="Peppa.Pig"><display-name lang="pt">Peppa Pig YT</display-name></channel>
  <channel id="Cartoon.Network.SD"><display-name lang="pt">Cartoon Network SD</display-name></channel>
  <channel id="Cartoon.Network.HD"><display-name lang="pt">Cartoon Network HD</display-name></channel>
  <channel id="Retro.Cartoon"><display-name lang="pt">Retro Cartoon</display-name></channel>
  <channel id="Gospel.Cartoon"><display-name lang="pt">Gospel Cartoon</display-name></channel>
  <channel id="Anime.TV"><display-name lang="pt">Anime TV</display-name></channel>
  <channel id="Jetsontv"><display-name lang="pt">Jetsontv</display-name></channel>
  <channel id="Domi.Kids"><display-name lang="pt">Domi Kids</display-name></channel>
  <channel id="Ministerio.Infantil"><display-name lang="pt">Ministério Infantil</display-name></channel>
  <channel id="Hallo.Series"><display-name lang="pt">Hallo! Series</display-name></channel>
  <channel id="Hallo.Classic"><display-name lang="pt">Hallo! Classic</display-name></channel>
  <channel id="Hallo.Movies"><display-name lang="pt">Hallo! Movies</display-name></channel>
  <channel id="Hallo.Anime"><display-name lang="pt">Hallo Anime HD²</display-name></channel>
  <channel id="Hallo.Doc"><display-name lang="pt">Hallo! Doc.</display-name></channel>
  <channel id="Hallo.Music"><display-name lang="pt">Hallo! Music</display-name></channel>
  <channel id="Pluto.TV.Star.Trek"><display-name lang="pt">Pluto TV Star Trek</display-name></channel>
  <channel id="Star.Trek.TNG"><display-name lang="pt">Star Trek: The Next Generation</display-name></channel>
  <channel id="Star.Trek.DS9"><display-name lang="pt">Star Trek: Deep Space Nine</display-name></channel>
  <channel id="Star.Trek.Voyager"><display-name lang="pt">Star Trek: Voyager</display-name></channel>
  <channel id="Space"><display-name lang="pt">SPACE HD</display-name></channel>
  <channel id="Space.2"><display-name lang="pt">SPACE HD²</display-name></channel>
  <channel id="TNT.HD"><display-name lang="pt">TNT HD</display-name></channel>
  <channel id="TNT.SD"><display-name lang="pt">TNT SD</display-name></channel>
  <channel id="Warner.Channel"><display-name lang="pt">Warner Channel HD</display-name></channel>
  <channel id="Warner.Channel.2"><display-name lang="pt">Warner Channel HD²</display-name></channel>
  <channel id="AeE"><display-name lang="pt">A&amp;E HD</display-name></channel>
  <channel id="AeE.2"><display-name lang="pt">A&amp;E HD²</display-name></channel>
  <channel id="AXN"><display-name lang="pt">AXN HD</display-name></channel>
  <channel id="Telecine.Action.2"><display-name lang="pt">Telecine Action HD²</display-name></channel>
  <channel id="Telecine.Action"><display-name lang="pt">Telecine Action HD</display-name></channel>
  <channel id="Telecine.Pipoca"><display-name lang="pt">Telecine Pipoca HD</display-name></channel>
  <channel id="Telecine.Premium"><display-name lang="pt">Telecine Premium HD</display-name></channel>
  <channel id="Telecine.Touch"><display-name lang="pt">Telecine Touch HD</display-name></channel>
  <channel id="Telecine.Cult"><display-name lang="pt">Telecine Cult HD</display-name></channel>
  <channel id="Telecine.Fun"><display-name lang="pt">Telecine Fun HD</display-name></channel>
  <channel id="AMC.SD"><display-name lang="pt">AMC SD</display-name></channel>
  <channel id="AMC.HD"><display-name lang="pt">AMC HD</display-name></channel>
  <channel id="Sony.Channel"><display-name lang="pt">Sony Channel HD</display-name></channel>
  <channel id="Cinemax"><display-name lang="pt">CINEMAX HD</display-name></channel>
  <channel id="Megapix.2"><display-name lang="pt">MEGAPIX HD²</display-name></channel>
  <channel id="HBO"><display-name lang="pt">HBO HD</display-name></channel>
  <channel id="HBO2"><display-name lang="pt">HBO 2 HD</display-name></channel>
  <channel id="HBO.Family"><display-name lang="pt">HBO Family HD</display-name></channel>
  <channel id="HBO.Xtreme"><display-name lang="pt">HBO Xtreme HD</display-name></channel>
  <channel id="HBO.Signature"><display-name lang="pt">HBO SIGNATURE HD</display-name></channel>
  <channel id="HBO.Plus"><display-name lang="pt">HBO+ HD</display-name></channel>
  <channel id="Universal.TV"><display-name lang="pt">Universal Channel HD</display-name></channel>
  <channel id="Universal.TV.2"><display-name lang="pt">Universal Channel HD²</display-name></channel>
  <channel id="MyTime.Movies"><display-name lang="pt">MyTime Movies</display-name></channel>
  <channel id="Movie.Sphere"><display-name lang="pt">MOVIE SPHERE</display-name></channel>
  <channel id="Sony.One.Emocoes"><display-name lang="pt">SONY ONE EMOCOES HD</display-name></channel>
  <channel id="Sony.One.Classics"><display-name lang="pt">Sony One Classics HD</display-name></channel>
  <channel id="Cine.Monde"><display-name lang="pt">Cine Monde HD</display-name></channel>
  <channel id="Dark.Flix"><display-name lang="pt">Dark Flix HD</display-name></channel>
  <channel id="Channel.One"><display-name lang="pt">CHANNEL ONE HD</display-name></channel>
  <channel id="Channel.HD"><display-name lang="pt">CHANNEL HD</display-name></channel>
  <channel id="Cine.Trianon"><display-name lang="pt">Cine Trianon HD</display-name></channel>
  <channel id="Cinerama"><display-name lang="pt">Cinerama 🇧🇴 (Bolívia)</display-name></channel>
  <channel id="Bang.Bang"><display-name lang="pt">Bang Bang HD</display-name></channel>
  <channel id="Runtime.Acao"><display-name lang="pt">Runtime Ação HD</display-name></channel>
  <channel id="Runtime.TV"><display-name lang="pt">Runtime TV e Filmes Grátis HD</display-name></channel>
  <channel id="Runtime.Comedia"><display-name lang="pt">Runtime Comédia HD</display-name></channel>
  <channel id="Runtime.Familia"><display-name lang="pt">Runtime Família HD</display-name></channel>
  <channel id="Runtime.Romance"><display-name lang="pt">Runtime Romance HD</display-name></channel>
  <channel id="Cine.Espanto"><display-name lang="pt">Cine Espanto HD</display-name></channel>
  <channel id="Runtime.Crime"><display-name lang="pt">Runtime Crime HD</display-name></channel>
  <channel id="Runtime"><display-name lang="pt">Runtime</display-name></channel>
  <channel id="Pluto.TV.Cine.Crime"><display-name lang="pt">Pluto TV Cine Crime</display-name></channel>
  <channel id="Pluto.TV.Cine.Inspiracao"><display-name lang="pt">Pluto TV Cine Inspiração</display-name></channel>
  <channel id="Pluto.TV.Cine.Sucessos"><display-name lang="pt">Pluto TV Cine Sucessos</display-name></channel>
  <channel id="Pluto.TV.Filmes.Acao"><display-name lang="pt">Pluto TV Filmes Ação</display-name></channel>
  <channel id="Pluto.TV.Cine.Terror"><display-name lang="pt">Pluto TV Cine Terror</display-name></channel>
  <channel id="Pluto.TV.Cine.Drama"><display-name lang="pt">Pluto TV Cine Drama</display-name></channel>
  <channel id="Pluto.TV.Cine.Familia"><display-name lang="pt">Pluto TV Cine Família</display-name></channel>
  <channel id="Pluto.TV.Cine.Romance"><display-name lang="pt">Pluto TV Cine Romance</display-name></channel>
  <channel id="Pluto.TV.Cine.Comedia.Romantica"><display-name lang="pt">Pluto TV Cine Comédia Romântica</display-name></channel>
  <channel id="Pluto.TV.Cine.Comedia"><display-name lang="pt">Pluto TV Cine Comédia</display-name></channel>
  <channel id="Filmes.Suspense"><display-name lang="pt">Filmes Suspense</display-name></channel>
  <channel id="Pluto.TV.Cine.Classicos"><display-name lang="pt">Pluto TV Cine Clássicos</display-name></channel>
  <channel id="Pluto.TV.Filmes.Nacionais"><display-name lang="pt">Pluto TV Filmes Nacionais</display-name></channel>
  <channel id="Filmelier.TV"><display-name lang="pt">Filmelier TV</display-name></channel>
  <channel id="Pluto.TV.Ficcao.Cientifica"><display-name lang="pt">Pluto TV Ficção Científica</display-name></channel>
  <channel id="Pluto.TV.Adrenalina.Freezone"><display-name lang="pt">Pluto TV Adrenalina Freezone</display-name></channel>
  <channel id="Hallo.Classic.2"><display-name lang="pt">Hallo! Classic</display-name></channel>
  <channel id="Hallo.Movies.2"><display-name lang="pt">Hallo! Movies</display-name></channel>
  <channel id="South.Park.Colecao.Cartman"><display-name lang="pt">South Park: Coleção Cartman</display-name></channel>
  <channel id="South.Park.Colecao.Kenny"><display-name lang="pt">South Park: Coleção Kenny</display-name></channel>
  <channel id="South.Park.Colecao.Kyle"><display-name lang="pt">South Park: Coleção Kyle</display-name></channel>
  <channel id="South.Park.Colecao.Stan"><display-name lang="pt">South Park: Coleção Stan</display-name></channel>
  <channel id="Comedy.Central.South.Park"><display-name lang="pt">Comedy Central South Park</display-name></channel>
  <channel id="Series.De.Comedia"><display-name lang="pt">Séries de Comédia | Pluto TV Brasil</display-name></channel>
  <channel id="Pluto.TV.Series.Criminais"><display-name lang="pt">Pluto TV Séries Criminais</display-name></channel>
  <channel id="Pluto.TV.Series.Acao"><display-name lang="pt">Pluto TV Séries Ação</display-name></channel>
  <channel id="Rookie.Blue"><display-name lang="pt">Rookie Blue</display-name></channel>
  <channel id="Clube.Do.Terror"><display-name lang="pt">Clube do Terror</display-name></channel>
  <channel id="BET.Pluto.TV"><display-name lang="pt">BET Pluto TV</display-name></channel>
  <channel id="NCIS"><display-name lang="pt">NCIS</display-name></channel>
  <channel id="CSI.Miami"><display-name lang="pt">CSI: Miami</display-name></channel>
  <channel id="Pluto.TV.Series.Sci-Fi"><display-name lang="pt">Pluto TV Séries Sci-Fi</display-name></channel>
  <channel id="O.Homem.Que.Veio.Do.Ceu"><display-name lang="pt">O Homem que veio do Céu</display-name></channel>
  <channel id="Hallo.Series.13"><display-name lang="pt">Hallo! Series</display-name></channel>
  <channel id="Naruto"><display-name lang="pt">Naruto</display-name></channel>
  <channel id="Loading.TV"><display-name lang="pt">Loading... TV HD</display-name></channel>
  <channel id="Wording.TV"><display-name lang="pt">WORDING TV</display-name></channel>
  <channel id="Geekdot"><display-name lang="pt">Geekdot</display-name></channel>
  <channel id="AniTV"><display-name lang="pt">AniTV</display-name></channel>
  <channel id="Hallo.Anime"><display-name lang="pt">Hallo Anime HD²</display-name></channel>
  <channel id="Combate"><display-name lang="pt">Combate HD</display-name></channel>
  <channel id="DAZN.Combate"><display-name lang="pt">DAZN Combate HD</display-name></channel>
  <channel id="SFT.Combate"><display-name lang="pt">SFT Combate BR HD</display-name></channel>
  <channel id="MMA"><display-name lang="pt">MMA HD</display-name></channel>
  <channel id="FITE"><display-name lang="pt">FITE HD</display-name></channel>
  <channel id="Lucha.Libre"><display-name lang="pt">LUCHA LIBRE</display-name></channel>
  <channel id="SFT.Combat"><display-name lang="pt">SFT Combat</display-name></channel>
  <channel id="Combatv"><display-name lang="pt">COMBATV</display-name></channel>
  <channel id="Ge.TV"><display-name lang="pt">Ge TV</display-name></channel>
  <channel id="Desimpedidos"><display-name lang="pt">Desimpedidos</display-name></channel>
  <channel id="Caze.TV"><display-name lang="pt">Cazé TV</display-name></channel>
  <channel id="Barcelona"><display-name lang="pt">BARCELONA</display-name></channel>
  <channel id="Real.Madrid"><display-name lang="pt">REAL MADRID</display-name></channel>
  <channel id="NSports"><display-name lang="pt">NSPORTS</display-name></channel>
  <channel id="Band.Sports"><display-name lang="pt">Band Sports HD</display-name></channel>
  <channel id="Auto.TV"><display-name lang="pt">Auto TV</display-name></channel>
  <channel id="SporTV"><display-name lang="pt">SporTV HD</display-name></channel>
  <channel id="SporTV.FHD"><display-name lang="pt">SporTV FHD</display-name></channel>
  <channel id="SporTV.2"><display-name lang="pt">SporTV 2 HD</display-name></channel>
  <channel id="SporTV.3"><display-name lang="pt">SporTV 3 HD</display-name></channel>
  <channel id="SporTV.3.F1"><display-name lang="pt">SporTV 3 F1 AO VIVO</display-name></channel>
  <channel id="ESPN"><display-name lang="pt">ESPN HD</display-name></channel>
  <channel id="ESPN.FHD"><display-name lang="pt">ESPN FHD</display-name></channel>
  <channel id="ESPN.2"><display-name lang="pt">ESPN 2 HD</display-name></channel>
  <channel id="ESPN.3"><display-name lang="pt">ESPN 3 HD</display-name></channel>
  <channel id="ESPN.4"><display-name lang="pt">ESPN 4 HD</display-name></channel>
  <channel id="ESPN.4.SD"><display-name lang="pt">ESPN 4 SD</display-name></channel>
  <channel id="ESPN.5"><display-name lang="pt">ESPN 5 HD</display-name></channel>
  <channel id="ESPN.6"><display-name lang="pt">ESPN 6 HD</display-name></channel>
  <channel id="Premiere.Clubes"><display-name lang="pt">Premiere Clubes HD</display-name></channel>
  <channel id="Premiere.2"><display-name lang="pt">Premiere 2 HD</display-name></channel>
  <channel id="Premiere.3"><display-name lang="pt">Premiere 3 HD</display-name></channel>
  <channel id="Premiere.4"><display-name lang="pt">Premiere 4 HD</display-name></channel>
  <channel id="Premiere.5"><display-name lang="pt">Premiere 5 HD</display-name></channel>
  <channel id="Premiere.6"><display-name lang="pt">Premiere 6 HD</display-name></channel>
  <channel id="Premiere.7"><display-name lang="pt">Premiere 7 HD</display-name></channel>
  <channel id="Animal.Planet"><display-name lang="pt">Animal Planet FHD</display-name></channel>
  <channel id="History"><display-name lang="pt">History HD</display-name></channel>
  <channel id="History.2"><display-name lang="pt">History 2 HD</display-name></channel>
  <channel id="HGTV"><display-name lang="pt">HGTV HD</display-name></channel>
  <channel id="Trace.Brasil"><display-name lang="pt">Trace Brasil</display-name></channel>
  <channel id="Sony.One.Shark.Tank"><display-name lang="pt">SONY ONE SHARK TANK</display-name></channel>
  <channel id="TLC"><display-name lang="pt">TLC HD</display-name></channel>
  <channel id="Prime.Box.Brazil"><display-name lang="pt">Prime Box HD</display-name></channel>
  <channel id="Arte.1"><display-name lang="pt">ARTE 1 HD</display-name></channel>
  <channel id="Film.Arts"><display-name lang="pt">Film &amp; Arts HD</display-name></channel>
  <channel id="Receitas.Fast"><display-name lang="pt">Receita Fast HD</display-name></channel>
  <channel id="Food.Network"><display-name lang="pt">Food Network HD</display-name></channel>
  <channel id="Masterchef"><display-name lang="pt">MASTERCHEF HD</display-name></channel>
  <channel id="Tastemade"><display-name lang="pt">TASTEMADE HD</display-name></channel>
  <channel id="Discovery.Turbo"><display-name lang="pt">Discovery Turbo HD</display-name></channel>
  <channel id="Discovery.World"><display-name lang="pt">Discovery World HD</display-name></channel>
  <channel id="ID"><display-name lang="pt">ID HD</display-name></channel>
  <channel id="Discovery.Home.Health"><display-name lang="pt">Disc. Home &amp; Health HD</display-name></channel>
  <channel id="Discovery.Channel"><display-name lang="pt">Discovery Channel FHD</display-name></channel>
  <channel id="Discovery.Science"><display-name lang="pt">Discovery Science HD</display-name></channel>
  <channel id="Discovery.Theater"><display-name lang="pt">Discovery Theater HD</display-name></channel>
  <channel id="Pluto.TV.Investigacao"><display-name lang="pt">Pluto tv Investigação</display-name></channel>
  <channel id="Pluto.TV.Misterios"><display-name lang="pt">Pluto TV Mistérios</display-name></channel>
  <channel id="People.Are.Awesome"><display-name lang="pt">People Are Awesome</display-name></channel>
  <channel id="Trace.Sport.Stars"><display-name lang="pt">Trace Sport Stars</display-name></channel>
  <channel id="Motorvision"><display-name lang="pt">Motorvision FHD</display-name></channel>
  <channel id="Auto.TV.2"><display-name lang="pt">Auto TV</display-name></channel>
  <channel id="Cultne.TV"><display-name lang="pt">Cultne TV</display-name></channel>
  <channel id="Nature.Moments"><display-name lang="pt">Nature Moments HD</display-name></channel>
  <channel id="Nature.Time"><display-name lang="pt">Nature Time HD</display-name></channel>
  <channel id="WildEarth"><display-name lang="pt">WildEarth 24 horas HD</display-name></channel>
  <channel id="Love.Nature"><display-name lang="pt">Love Nature HD</display-name></channel>
  <channel id="Pesca"><display-name lang="pt">Pesca HD</display-name></channel>
  <channel id="Natureza"><display-name lang="pt">Natureza HD</display-name></channel>
  <channel id="Nature.Time.FHD"><display-name lang="pt">NatureTime FHD</display-name></channel>
  <channel id="Pluto.TV.Paisagens"><display-name lang="pt">Pluto TV Paisagens por Stingray HD</display-name></channel>
  <channel id="Pluto.TV.Animais"><display-name lang="pt">Pluto TV Animais HD</display-name></channel>
  <channel id="O.Encantador.De.Caes"><display-name lang="pt">O Encantador de Cães HD</display-name></channel>
  <channel id="Pluto.TV.Misterios.2"><display-name lang="pt">Pluto TV Mistérios</display-name></channel>
  <channel id="Pluto.TV.Aliens"><display-name lang="pt">Pluto TV Aliens</display-name></channel>
  <channel id="Assombracoes"><display-name lang="pt">Assombrações</display-name></channel>
  <channel id="Estado.Paranormal"><display-name lang="pt">Estado Paranormal</display-name></channel>
  <channel id="Cacadores.de.Ovnis"><display-name lang="pt">Caçadores de Ovnis</display-name></channel>
  <channel id="Tv.Universal"><display-name lang="pt">Igreja Universal HD</display-name></channel>
  <channel id="Tv.Mundial"><display-name lang="pt">Igreja Mundial HD</display-name></channel>
  <channel id="Tv.Plenitude"><display-name lang="pt">Igreja Plenitude HD</display-name></channel>
  <channel id="Novo.Tempo"><display-name lang="pt">Novo Tempo HD</display-name></channel>
  <channel id="Tv.Evangelizar"><display-name lang="pt">Igreja Evangelizar HD</display-name></channel>
  <channel id="Cancao.Nova"><display-name lang="pt">Canção Nova HD</display-name></channel>
  <channel id="TV.Aparecida"><display-name lang="pt">TV Aparecida HD</display-name></channel>
  <channel id="Globoplay.Novelas"><display-name lang="pt">Globoplay Novelas</display-name></channel>
  <channel id="Malhacao.Fast"><display-name lang="pt">Malhação Fast</display-name></channel>
  <channel id="TVI.Ficcao"><display-name lang="pt">TVi Ficção</display-name></channel>
  <channel id="A.Escrava.Isaura"><display-name lang="pt">A Escrava Isaura</display-name></channel>
  <channel id="A.Terra.Prometida"><display-name lang="pt">A Terra Prometida</display-name></channel>
  <channel id="Reis"><display-name lang="pt">Reis</display-name></channel>
  <channel id="Reviva"><display-name lang="pt">REVIVA Novelas HD</display-name></channel>
  <channel id="TNT.Novelas"><display-name lang="pt">TNT Novelas</display-name></channel>
  <channel id="Pluto.TV.Novelas"><display-name lang="pt">PLUTO TV NOVELAS</display-name></channel>
  <channel id="Novelas.Evagina"><display-name lang="pt">Novelas Evagina</display-name></channel>
  <channel id="TV.Telenovelas"><display-name lang="pt">TV Telenovelas</display-name></channel>
  <channel id="Telenovelas"><display-name lang="pt">Telenovelas</display-name></channel>
  <channel id="TV.Telemundo.Telenovelas"><display-name lang="pt">TV Telemundo Telenovelas</display-name></channel>
  <channel id="Novelissima"><display-name lang="pt">Novelissima BR</display-name></channel>
  <channel id="Sony.Novelas"><display-name lang="pt">Sony Novelas</display-name></channel>
  <channel id="Spark.Luz.E.Amor"><display-name lang="pt">Spark Luz E Amor HD</display-name></channel>
  <channel id="Televisa"><display-name lang="pt">TELEVISA</display-name></channel>
  <channel id="Televisa.Telenovelas"><display-name lang="pt">Televisa Telenovelas</display-name></channel>
"""

# Junta tudo e salva o seu principal
with open("epg.xml", "w", encoding="utf-8") as f:
    f.write(xml_header + canais + xml_footer)

print("Arquivo epg.xml principal gerado com sucesso!")

# --- ADIÇÃO DE FONTES EXTERNAS POR LOURIVAL026 ---

def baixar_fontes_adicionais():
    fontes = {
        "iptv_org": "https://iptv-org.github.io/epg/guides/br/brazil.xml",
        "pluto_tv": "https://i.mjh.nz/PlutoTV/br.xml",
        "claro_tv": "https://epg.orangelabs.xyz/claro.xml"
    }
    
    for nome, url in fontes.items():
        print(f"[{'Lourival026'}] Baixando fonte extra: {nome}...")
        try:
            resp = requests.get(url, timeout=30)
            if resp.status_code == 200:
                with open(f"epg_{nome}.xml", "wb") as f:
                    f.write(resp.content)
                print(f"[{'Lourival026'}] Sucesso: epg_{nome}.xml salvo.")
        except Exception as e:
            print(f"Erro ao baixar {nome}: {e}")

# Executar a função extra
baixar_fontes_adicionais()
print("--- Todos os processos finalizados ---")
