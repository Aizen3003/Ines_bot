import telebot
import random
import json
import tokenn
xxx = open("wospominania", "r", encoding="UTF-8")
vse_slowari = json.load(xxx)

def woswrat(polso):
    return True

bot = telebot.TeleBot(tokenn.token)
@bot.message_handler(["start"])
def start(polso):
    bot.send_message(polso.chat.id, "Привет")
    bot.send_message(polso.chat.id, "Что хотите?")

@bot.message_handler(["zapom"])
def zapom(polso):
    if str(polso.chat.id) in vse_slowari:
        slowar = vse_slowari[str(polso.chat.id)]
    else :
        slowar = {}
    zapomineischen = polso.text
    slowa = zapomineischen.split(" ")
    if len(slowa) == 3:
        eng = slowa[1]
        rus = slowa[2]
        print(eng, rus)
        slowar[eng] = rus
        vse_slowari[polso.chat.id] = slowar
        xxx = open("wospominania", "w", encoding="UTF-8")
        json.dump(vse_slowari, xxx, ensure_ascii=False, indent=4)
        xxx.close()
        bot.send_message(polso.chat.id, "Слово добавлено успешно")
    else :
        bot.send_message(polso.chat.id, "Недостаточно инфорации")
@bot.message_handler(["show_words"])
def show_words(polso):
    if str(polso.chat.id) in vse_slowari:
        slovrik = vse_slowari[str(polso.chat.id)]
        numer = 1
        for perew in slovrik:
            bot.send_message(polso.chat.id, str(numer) + " " + perew + " - " + slovrik[perew])
            numer += 1
        numer -= 1
        bot.send_message(polso.chat.id, str(numer) + " " + "слов(а)")
    else :
        bot.send_message(polso.chat.id, "У вас нет слов")
@bot.message_handler(["help"])
def spisok(polso):
    bot.send_message(polso.chat.id, "start - запускает бота")
    bot.send_message(polso.chat.id, "zapom - добавляет новое слово с переводом в словарь")
    bot.send_message(polso.chat.id, "show_words - выводит по очереди пронумерованные слова из словаря с переводом и общее количество слов")
def prower(polso, otwet):
    if otwet == polso.text:
        bot.send_message(polso.chat.id, "Правильный ответ")
    else :
        bot.send_message(polso.chat.id, "Неправильный ответ")
        bot.send_message(polso.chat.id, "Ответ" + " " + otwet)
@bot.message_handler(["treners"])
def lerer(polso):
    solowarizek = vse_slowari[str(polso.chat.id)]
    engli = solowarizek.keys()
    engli = list(engli)
    sluchang = random.choice(engli)
    otwet = solowarizek[sluchang]
    bot.send_message(polso.chat.id, "Введите перевод слова - " + sluchang)
    bot.register_next_step_handler_by_chat_id(polso.chat.id, prower, otwet)
@bot.message_handler(func=woswrat)
def obrabwse(polso):
    if polso.text == "Привет":
        bot.send_message(polso.chat.id, "...")
    elif polso.text == "Как дела?":
        bot.send_message(polso.chat.id, "Хорошо")
    else :
        bot.send_message(polso.chat.id, "Error"*10)

bot.polling()