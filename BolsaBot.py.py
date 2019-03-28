import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, InlineQueryHandler, ChosenInlineResultHandler
from telegram import InlineQueryResultArticle, InputTextMessageContent, ReplyKeyboardMarkup
import logging

from BolsaBot_Scrap.Scrap import *


#Info do Bot
bot = telegram.Bot(token='602188716:AAFBEQpRqUqe3abwMxNEUJzFy0R7ap9nvpE')
updater = Updater(token='602188716:AAFBEQpRqUqe3abwMxNEUJzFy0R7ap9nvpE')
dispatcher = updater.dispatcher


#log de erros
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)



# -------------- Definições ------------------ #
# Definição de /start
def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="""--- Bem vindo ao Bolsabot!--- \n
Digite o nome da empresa listado na bolsa de valores mais "On" para ações "Ordinárias" ou "Pn" para ações preferênciais, para receber as informações referentes a cotação atual""")
    
def cotacao(bot,update): #Apresenta as informações referente a cotação da empresa escolhida
    elemento = update.message.text
    valor = scrap(elemento)
    escolhido = escolh(elemento)
    if valor == str('ess":'):
        bot.send_message(chat_id=update.message.chat_id, text="Insira um nome de empresa válido ou com mais detalhes e 'On' para ações ordinárias e 'Pn' para ações preferênciais")
    else:
        bot.send_message(chat_id=update.message.chat_id, text=f"- Empresa selecionada:'{escolhido}'\n- O último fechamento foi de: R$ {valor}")
        bot.send_message(chat_id=update.message.chat_id, text=f"Fonte: ValorEconomico - Atraso de 15 minutos \nInsira o nome de outra empresa que deseja saber sua última cotação!")
   


    
# ------------------ Main ---------------------- #



start_handler = CommandHandler('start', start) #Inicializa a função start
dispatcher.add_handler(start_handler, group=0)

cotacao_handler = MessageHandler(Filters.text, cotacao) #Inicializa a função opção1
dispatcher.add_handler(cotacao_handler)





updater.start_polling() #Realiza a leitura do update do bot a cada ação
updater.idle()
        









                               
