import pzgram
import requests
import time
bot = pzgram.Bot("745277106:AAGJr1oJ8O0Si5tG5lapuWVjKkuLYGMqlJo")

def ricerca(chat, message):
	chat.send(">>Ricerca valori...")
	time.sleep(3)

def valori_istantanei(chat, message):
	temperatura = "temperatura istantanea"
	altitudine = "altitudine istantanea"
	pressione = "pressione istantanea"
	luminosita = "luminosita istantanea"
	ricerca(chat, message)
	chat.send(temperatura)
	chat.send(altitudine)
	chat.send(pressione)
	chat.send(luminosita)

def valori_min_1(chat, message):
	temperatura = "temperatura di 1 minuto"
	altitudine = "altitudine di 1 minuto"
	pressione = "pressione di 1 minuto"
	luminosita = "luminosita di 1 minuto"
	ricerca(chat, message)
	chat.send(temperatura)
	chat.send(altitudine)
	chat.send(pressione)
	chat.send(luminosita)

def valori_min_10(chat, message):
	temperatura = "temperatura di 10 minuti"
	altitudine = "altitudine di 10 minuti"
	pressione = "pressione di 10 minuti"
	luminosita = "luminosita di 10 minuti"
	ricerca(chat, message)
	chat.send(temperatura)
	chat.send(altitudine)
	chat.send(pressione)
	chat.send(luminosita)

def valori_1_ora(chat, message):
	temperatura = "temperatura di 1 ora"
	altitudine = "altitudine di 1 ora"
	pressione = "pressione di 1 ora"
	luminosita = "luminosita di 1 ora"
	ricerca(chat, message)
	chat.send(temperatura)
	chat.send(altitudine)
	chat.send(pressione)
	chat.send(luminosita)

def start_command(chat):
	keyboard = pzgram.create_keyboard([["/Ora", "/1min", "/10min", "/1h"]])
	chat.send("Select a command", reply_markup=keyboard)

def process_message(message, chat):
	if message.text == "Valori_Istantanei":
		valori_istantanei(chat,message)
	elif message.text == "Valori_di_1_minuto":
		valori_min_1(chat,message)  



bot.set_commands({"Ora": valori_istantanei})
bot.set_commands({"1min": valori_min_1})
bot.set_commands({"10min": valori_min_10})
bot.set_commands({"1h": valori_1_ora})
bot.set_commands({"avvia" : start_command})


bot.run()
