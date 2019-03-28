# Raspagem de dados no site valor economico
# libs Nativas
import datetime
import time

# libs terceiras
import requests
from bs4 import BeautifulSoup as bs
import nltk

# DEF's
def ultimoclose(x):
    a = []
    y = []
    i = 0
    lista = []
    while i < len(x):
        if x[i] == "{":
            a.append(i)
        if x[i] == "}":
            y.append(i)
        i = i+1
    lista = x[a[-1]:y[-1]]
    return lista

def nomedaempresa(a):
    if a == "bovespa" or a=="BOVESPA" or a=="Bovespa" or a=="Indice Bovespa" or a=="Ibovespa" or a=="IBovespa" or a=="IBOVESPA":
        return "IBOV"
    elif  a== "ABCBrasil" or a=="ABC" or a=="A B C" or a=="A B C Brasil":
        return "ABCB4"
#--------------Def para prefixo------------------
def get_bigrams(string):
    s = string.lower()
    return [s[i:i+2] for i in range(len(s) - 1)]

def string_similarity(str1, str2):
    pairs1 = get_bigrams(str1)
    pairs2 = get_bigrams(str2)
    union  = len(pairs1) + len(pairs2)
    hit_count = 0
    for x in pairs1:
        for y in pairs2:
            if x == y:
                hit_count += 1
                break
    return (2.0 * hit_count) / union

def prefixo(x):
    if x == 'ÍNDICE BOVESPA':	prefix = 'IBOV'
    elif x == 'ABC BRASIL PN':	prefix = 'ABCB4'
    elif x == 'AES TIETE E UNT':	prefix = 'TIET11'
    elif x == 'ALIANSCE ON':	prefix = 'ALSC3'
    elif x == 'ALPARGATAS PN':	prefix = 'ALPA4'
    elif x == 'ALUPAR UNT':	prefix = 'ALUP11'
    elif x == 'AMBEV S/A ON':	prefix = 'ABEV3'
    elif x == 'ANIMA ON':	prefix = 'ANIM3'
    elif x == 'AREZZO CO ON':	prefix = 'ARZZ3'
    elif x == 'AZUL PN':	prefix = 'AZUL4'
    elif x == 'B2W DIGITAL ON':	prefix = 'BTOW3'
    elif x == 'B3 ON':	prefix = 'B3SA3'
    elif x == 'BANCO INTER PN':	prefix = 'BIDI4'
    elif x == 'BANRISUL PNB EJ':	prefix = 'BRSR6'
    elif x == 'BBSEGURIDADEON':	prefix = 'BBSE3'
    elif x == 'BK BRASIL ON EJ':	prefix = 'BKBR3'
    elif x == 'BR MALLS PARON':	prefix = 'BRML3'
    elif x == 'BR PROPERT ON':	prefix = 'BRPR3'
    elif x == 'BRADESCO ON EJ':	prefix = 'BBDC3'
    elif x == 'BRADESCO PN EJ':	prefix = 'BBDC4'
    elif x == 'BRADESPAR PN':	prefix = 'BRAP4'
    elif x == 'BRASIL ON EJ':	prefix = 'BBAS3'
    elif x == 'BRASKEM PNA':	prefix = 'BRKM5'
    elif x == 'BRF SA ON':	prefix = 'BRFS3'
    elif x == 'BTGP BANCO UNT':	prefix = 'BPAC11'
    elif x == 'CAMIL ON':	prefix = 'CAML3'
    elif x == 'CARREFOUR BRON':	prefix = 'CRFB3'
    elif x == 'CCR SA ON':	prefix = 'CCRO3'
    elif x == 'CEMIG ON':	prefix = 'CMIG3'
    elif x == 'CEMIG PN':	prefix = 'CMIG4'
    elif x == 'CESP PNB':	prefix = 'CESP6'
    elif x == 'CIA HERING ON':	prefix = 'HGTX3'
    elif x == 'CIELO ON':	prefix = 'CIEL3'
    elif x == 'COPASA ON EJ':	prefix = 'CSMG3'
    elif x == 'COPEL PNB':	prefix = 'CPLE6'
    elif x == 'COSAN ON':	prefix = 'CSAN3'
    elif x == 'COSAN LOG ON':	prefix = 'RLOG3'
    elif x == 'CPFL ENERGIAON':	prefix = 'CPFE3'
    elif x == 'CVC BRASIL ON':	prefix = 'CVCB3'
    elif x == 'CYRELA REALTON':	prefix = 'CYRE3'
    elif x == 'DIRECIONAL ON ED':	prefix = 'DIRR3'
    elif x == 'DOMMO ON':	prefix = 'DMMO3'
    elif x == 'DURATEX ON':	prefix = 'DTEX3'
    elif x == 'ECORODOVIAS ON':	prefix = 'ECOR3'
    elif x == 'ELETROBRAS ON':	prefix = 'ELET3'
    elif x == 'ELETROBRAS PNB':	prefix = 'ELET6'
    elif x == 'EMBRAER ON':	prefix = 'EMBR3'
    elif x == 'ENERGIAS BR ON':	prefix = 'ENBR3'
    elif x == 'ENERGISA UNT':	prefix = 'ENGI11'
    elif x == 'ENEVA ON':	prefix = 'ENEV3'
    elif x == 'ENGIE BRASILON':	prefix = 'EGIE3'
    elif x == 'EQUATORIAL ON':	prefix = 'EQTL3'
    elif x == 'ESTACIO PARTON':	prefix = 'ESTC3'
    elif x == 'EVEN ON':	prefix = 'EVEN3'
    elif x == 'EZTEC ON':	prefix = 'EZTC3'
    elif x == 'FERBASA PN':	prefix = 'FESA4'
    elif x == 'FLEURY ON ED':	prefix = 'FLRY3'
    elif x == 'FORJA TAURUSPN':	prefix = 'FJTA4'
    elif x == 'GAFISA ON':	prefix = 'GFSA3'
    elif x == 'GERDAU PN ED':	prefix = 'GGBR4'
    elif x == 'GERDAU MET PN ED':	prefix = 'GOAU4'
    elif x == 'GOL PN':	prefix = 'GOLL4'
    elif x == 'GRENDENE ON':	prefix = 'GRND3'
    elif x == 'GUARARAPES ON':	prefix = 'GUAR3'
    elif x == 'HAPVIDA ON':	prefix = 'HAPV3'
    elif x == 'HYPERA ON':	prefix = 'HYPE3'
    elif x == 'IGUATEMI ON ED':	prefix = 'IGTA3'
    elif x == 'IHPARDINI ON':	prefix = 'PARD3'
    elif x == 'IMC S/A ON':	prefix = 'MEAL3'
    elif x == 'INTERMEDICA ON':	prefix = 'GNDI3'
    elif x == 'IOCHP-MAXIONON':	prefix = 'MYPK3'
    elif x == 'IRBBRASIL REON':	prefix = 'IRBR3'
    elif x == 'ITAUSA PN':	prefix = 'ITSA4'
    elif x == 'ITAUUNIBANCOON':	prefix = 'ITUB3'
    elif x == 'ITAUUNIBANCOPN':	prefix = 'ITUB4'
    elif x == 'JBS ON':	prefix = 'JBSS3'
    elif x == 'KLABIN S/A UNT':	prefix = 'KLBN11'
    elif x == 'KROTON ON':	prefix = 'KROT3'
    elif x == 'LIGHT S/A ON':	prefix = 'LIGT3'
    elif x == 'LINX ON':	prefix = 'LINX3'
    elif x == 'LOCALIZA ON':	prefix = 'RENT3'
    elif x == 'LOCAMERICA ON':	prefix = 'LCAM3'
    elif x == 'LOG COM PROPON':	prefix = 'LOGG3'
    elif x == 'LOJAS AMERICON':	prefix = 'LAME3'
    elif x == 'LOJAS AMERICPN':	prefix = 'LAME4'
    elif x == 'LOJAS MARISAON':	prefix = 'AMAR3'
    elif x == 'LOJAS RENNERON':	prefix = 'LREN3'
    elif x == 'M.DIASBRANCOON':	prefix = 'MDIA3'
    elif x == 'MAGAZ LUIZA ON':	prefix = 'MGLU3'
    elif x == 'MARCOPOLO PN':	prefix = 'POMO4'
    elif x == 'MARFRIG ON':	prefix = 'MRFG3'
    elif x == 'METAL LEVE ON':	prefix = 'LEVE3'
    elif x == 'MINERVA ON':	prefix = 'BEEF3'
    elif x == 'MOVIDA ON':	prefix = 'MOVI3'
    elif x == 'MRV ON':	prefix = 'MRVE3'
    elif x == 'MULTIPLAN ON':	prefix = 'MULT3'
    elif x == 'MULTIPLUS ON':	prefix = 'MPLU3'
    elif x == 'NATURA ON':	prefix = 'NATU3'
    elif x == 'ODONTOPREV ON':	prefix = 'ODPV3'
    elif x == 'OMEGA GER ON':	prefix = 'OMGE3'
    elif x == 'P.ACUCAR-CBDPN':	prefix = 'PCAR4'
    elif x == 'PETROBRAS ON':	prefix = 'PETR3'
    elif x == 'PETROBRAS PN':	prefix = 'PETR4'
    elif x == 'PETROBRAS BRON':	prefix = 'BRDT3'
    elif x == 'PETRORIO ON':	prefix = 'PRIO3'
    elif x == 'PORTO SEGUROON':	prefix = 'PSSA3'
    elif x == 'QGEP PART ON':	prefix = 'QGEP3'
    elif x == 'QUALICORP ON':	prefix = 'QUAL3'
    elif x == 'RAIADROGASILON':	prefix = 'RADL3'
    elif x == 'RANDON PART PN':	prefix = 'RAPT4'
    elif x == 'RUMO S.A. ON':	prefix = 'RAIL3'
    elif x == 'SABESP ON':	prefix = 'SBSP3'
    elif x == 'SANEPAR PN':	prefix = 'SAPR4'
    elif x == 'SANEPAR UNT':	prefix = 'SAPR11'
    elif x == 'SANTANDER BRUNT':	prefix = 'SANB11'
    elif x == 'SANTOS BRP ON':	prefix = 'STBP3'
    elif x == 'SAO MARTINHOON':	prefix = 'SMTO3'
    elif x == 'SER EDUCA ON':	prefix = 'SEER3'
    elif x == 'SID NACIONALON':	prefix = 'CSNA3'
    elif x == 'SLC AGRICOLAON':	prefix = 'SLCE3'
    elif x == 'SMILES ON':	prefix = 'SMLS3'
    elif x == 'SUL AMERICA UNT':	prefix = 'SULA11'
    elif x == 'SUZANO PAPELON':	prefix = 'SUZB3'
    elif x == 'TAESA UNT':	prefix = 'TAEE11'
    elif x == 'TEGMA ON':	prefix = 'TGMA3'
    elif x == 'TELEF BRASILPN':	prefix = 'VIVT4'
    elif x == 'TENDA ON':	prefix = 'TEND3'
    elif x == 'TIM PART S/AON':	prefix = 'TIMP3'
    elif x == 'TOTVS ON':	prefix = 'TOTS3'
    elif x == 'TRAN PAULISTPN':	prefix = 'TRPL4'
    elif x == 'TUPY ON':	prefix = 'TUPY3'
    elif x == 'ULTRAPAR ON':	prefix = 'UGPA3'
    elif x == 'UNIPAR PNB':	prefix = 'UNIP6'
    elif x == 'USIMINAS PNA':	prefix = 'USIM5'
    elif x == 'VALE ON':	prefix = 'VALE3'
    elif x == 'VALID ON':	prefix = 'VLID3'
    elif x == 'VIAVAREJO ON':	prefix = 'VVAR3'
    elif x == 'VULCABRAS ON':	prefix = 'VULC3'
    elif x == 'WEG ON':	prefix = 'WEGE3'
    elif x == 'WIZ S.A. ON':	prefix = 'WIZS3'

    else: return "erro"

    return prefix

    
def similaridade(x):
    w1 = x
    words = ['ÍNDICE BOVESPA','ABC BRASIL PN','AES TIETE E UNT','ALIANSCE ON','ALPARGATAS PN','ALUPAR UNT','AMBEV S/A ON','ANIMA ON','AREZZO CO ON','AZUL PN','B2W DIGITAL ON','B3 ON','BANCO INTER PN','BANRISUL PNB EJ','BBSEGURIDADEON','BK BRASIL ON EJ','BR MALLS PARON','BR PROPERT ON','BRADESCO ON EJ','BRADESCO PN EJ','BRADESPAR PN','BRASIL ON EJ','BRASKEM PNA','BRF SA ON','BTGP BANCO UNT','CAMIL ON','CARREFOUR BRON','CCR SA ON','CARREFOUR BRON','CCR SA ON','CEMIG ON','CEMIG PN','CESP PNB','CIA HERING ON','CIELO ON','COPASA ON EJ','COPEL PNB','COSAN ON','COSAN LOG ON','CPFL ENERGIAON','CVC BRASIL ON','CYRELA REALTON','DIRECIONAL ON ED','DOMMO ON','DURATEX ON','ECORODOVIAS ON','ELETROBRAS ON','ELETROBRAS PNB','EMBRAER ON','ENERGIAS BR ON','ENERGISA UNT','ENEVA ON','ENGIE BRASILON','EQUATORIAL ON','ESTACIO PARTON','EVEN ON','EZTEC ON','FERBASA PN','FLEURY ON ED','FORJA TAURUSPN','GAFISA ON','GERDAU PN ED','GERDAU MET PN ED','GOL PN','GRENDENE ON','GUARARAPES ON','HAPVIDA ON','HYPERA ON','IGUATEMI ON ED','IHPARDINI ON','IMC S/A ON','INTERMEDICA ON','IOCHP-MAXIONON','IRBBRASIL REON','ITAUSA PN','ITAUUNIBANCOON','ITAUUNIBANCOPN','JBS ON','KLABIN S/A UNT','KROTON ON','LIGHT S/A ON','LINX ON','LOCALIZA ON','LOCAMERICA ON','LOG COM PROPON','LOJAS AMERICON','LOJAS AMERICPN','LOJAS MARISAON','LOJAS RENNERON','M.DIASBRANCOON','MAGAZ LUIZA ON','MARCOPOLO PN','METAL LEVE ON','MINERVA ON','MARFRIG ON','MOVIDA ON','MRV ON','MULTIPLAN ON','MULTIPLUS ON','NATURA ON','ODONTOPREV ON','OMEGA GER ON','P.ACUCAR-CBDPN','PETROBRAS ON','PETROBRAS PN','PETROBRAS BRON','PETRORIO ON','PORTO SEGUROON','QGEP PART ON','QUALICORP ON','RAIADROGASILON','RANDON PART PN','RUMO S.A. ON','SABESP ON','SANEPAR PN','SANEPAR UNT','SANTANDER BRUNT','SANTOS BRP ON','SAO MARTINHOON','SER EDUCA ON','SID NACIONALON','SLC AGRICOLAON','SMILES ON','SUL AMERICA UNT','SUZANO PAPELON','TAESA UNT','TEGMA ON','TELEF BRASILPN','TENDA ON','TIM PART S/AON','TOTVS ON','TRAN PAULISTPN','TUPY ON','ULTRAPAR ON','UNIPAR PNB','USIMINAS PNA','VALE ON','VALID ON','VIAVAREJO ON','VULCABRAS ON','WEG ON','WIZ S.A. ON']

    i = 0
    vencedor = "erro"
    for w2 in words:
            if string_similarity(w1, w2) > i and string_similarity(w1, w2) > 0.4 :
                i = string_similarity(w1, w2)
                vencedor = w2

    return prefixo(vencedor)

def escolh(x):
    w1 = x
    words = ['ÍNDICE BOVESPA','ABC BRASIL PN','AES TIETE E UNT','ALIANSCE ON','ALPARGATAS PN','ALUPAR UNT','AMBEV S/A ON','ANIMA ON','AREZZO CO ON','AZUL PN','B2W DIGITAL ON','B3 ON','BANCO INTER PN','BANRISUL PNB EJ','BBSEGURIDADEON','BK BRASIL ON EJ','BR MALLS PARON','BR PROPERT ON','BRADESCO ON EJ','BRADESCO PN EJ','BRADESPAR PN','BRASIL ON EJ','BRASKEM PNA','BRF SA ON','BTGP BANCO UNT','CAMIL ON','CARREFOUR BRON','CCR SA ON','CARREFOUR BRON','CCR SA ON','CEMIG ON','CEMIG PN','CESP PNB','CIA HERING ON','CIELO ON','COPASA ON EJ','COPEL PNB','COSAN ON','COSAN LOG ON','CPFL ENERGIAON','CVC BRASIL ON','CYRELA REALTON','DIRECIONAL ON ED','DOMMO ON','DURATEX ON','ECORODOVIAS ON','ELETROBRAS ON','ELETROBRAS PNB','EMBRAER ON','ENERGIAS BR ON','ENERGISA UNT','ENEVA ON','ENGIE BRASILON','EQUATORIAL ON','ESTACIO PARTON','EVEN ON','EZTEC ON','FERBASA PN','FLEURY ON ED','FORJA TAURUSPN','GAFISA ON','GERDAU PN ED','GERDAU MET PN ED','GOL PN','GRENDENE ON','GUARARAPES ON','HAPVIDA ON','HYPERA ON','IGUATEMI ON ED','IHPARDINI ON','IMC S/A ON','INTERMEDICA ON','IOCHP-MAXIONON','IRBBRASIL REON','ITAUSA PN','ITAUUNIBANCOON','ITAUUNIBANCOPN','JBS ON','KLABIN S/A UNT','KROTON ON','LIGHT S/A ON','LINX ON','LOCALIZA ON','LOCAMERICA ON','LOG COM PROPON','LOJAS AMERICON','LOJAS AMERICPN','LOJAS MARISAON','LOJAS RENNERON','M.DIASBRANCOON','MAGAZ LUIZA ON','MARCOPOLO PN','METAL LEVE ON','MINERVA ON','MARFRIG ON','MOVIDA ON','MRV ON','MULTIPLAN ON','MULTIPLUS ON','NATURA ON','ODONTOPREV ON','OMEGA GER ON','P.ACUCAR-CBDPN','PETROBRAS ON','PETROBRAS PN','PETROBRAS BRON','PETRORIO ON','PORTO SEGUROON','QGEP PART ON','QUALICORP ON','RAIADROGASILON','RANDON PART PN','RUMO S.A. ON','SABESP ON','SANEPAR PN','SANEPAR UNT','SANTANDER BRUNT','SANTOS BRP ON','SAO MARTINHOON','SER EDUCA ON','SID NACIONALON','SLC AGRICOLAON','SMILES ON','SUL AMERICA UNT','SUZANO PAPELON','TAESA UNT','TEGMA ON','TELEF BRASILPN','TENDA ON','TIM PART S/AON','TOTVS ON','TRAN PAULISTPN','TUPY ON','ULTRAPAR ON','UNIPAR PNB','USIMINAS PNA','VALE ON','VALID ON','VIAVAREJO ON','VULCABRAS ON','WEG ON','WIZ S.A. ON']

    i = 0
    vencedor = "erro"
    for w2 in words:
            if string_similarity(w1, w2) > i and string_similarity(w1, w2) > 0.4 :
                i = string_similarity(w1, w2)
                vencedor = w2

    return vencedor
#-------------WebScrap---------------------------
def scrap(x):
        

    url = "https://www.valor.com.br/valor-data" #site do Valor Econômico inserido em 16/03/2019
    response = requests.get(url)

    soup = bs(response.text, "html.parser")

    dataini = datetime.datetime.today() - datetime.timedelta(hours=120) #diferença de 5 dias, convencionando que o usuário acesse antes da abertura do mercado em uma segunda onde sabado e domingo não houveram transações e que tenham sido seguidos de dois feriados.

    datainid = dataini.strftime("%d/%m/%Y") #Formatando as horas
    datafim = datetime.datetime.today().strftime("%d/%m/%Y %I:%M:%S")

    empresa = similaridade(x)

    
    #Parametros para enviar ao site a seleção da empresa
    params = (
        ('module', 'valor_data'),
        ('action', 'get_serie'),    
        ('symbol_code', f'{empresa}'),
        ('origin_id', '2'),
        ('period', '1'),
        ('date_from', f'{datainid} 09:00:00'),
        ('date_to', f'{datafim}'),
        ('type_chart', 'bolsas'),
    )

    response = requests.get('https://www.valor.com.br/json.php', params=params)
    tag = response.text
    tag2 = str(bs(ultimoclose(tag), "html.parser"))
    if empresa == "IBOV":
        ibov = str(tag2[tag2.find("Close")+7:tag2.find("Close")+12])
        return ibov[:2] +"." + ibov[2:]
    else:
        tag3 = tag2[tag2.find("Close")+7:tag2.find("Close")+12]
        return tag3



