# Raspagem de dados no site valor economico
# libs Nativas
import datetime
import time

# libs terceiras
import requests
from bs4 import BeautifulSoup as bs

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

def scrap(x):
        

    url = "https://www.valor.com.br/valor-data" #site do Valor Econômico inserido em 16/03/2019
    response = requests.get(url)

    soup = bs(response.text, "html.parser")

    dataini = datetime.datetime.today() - datetime.timedelta(hours=120) #diferença de 5 dias, convencionando que o usuário acesse antes da abertura do mercado em uma segunda onde sabado e domingo não houveram transações e que tenham sido seguidos de dois feriados.

    datainid = dataini.strftime("%d/%m/%Y") #Formatando as horas
    datafim = datetime.datetime.today().strftime("%d/%m/%Y %I:%M:%S")

    empresa = x

    
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
    tag3 = tag2[tag2.find("Close")+7:tag2.find("Close")+12]
    return(tag3)
