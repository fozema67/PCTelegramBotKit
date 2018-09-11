# -*- coding: utf-8 -*-

import telebot
import pyowm
# import parsing
import subprocess
# import os
# from flask import Flask, request
import logging
# from bs4 import BeautifulSoup

import config
from admin import cmd_admin

bot = telebot.TeleBot(config.tokenTel)
owm = pyowm.OWM(config.APIKeyOWM)

logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)


@bot.message_handler(content_types=["text"])
def messages(message):
    if message.text == "/start" or message.text == "/start" + config.referenseBot:
        bot.reply_to(message,
                     "Привет, " +
                     message.from_user.username +
                     ". Я только учусь и меня все еще разрабатывают. Не суди строго, если будут ошибки")
    elif message.text == "/key_t" or message.text == "/key_t" + config.referenseBot:
        cmd_admin(message)
    elif message.text == "/key_ai" or message.text == "/key_ai" + config.referenseBot:
        cmd_admin(message)
    elif message.text == "/chat_id" or message.text == "/chat_id" + config.referenseBot:
        bot.send_message(message.chat.id, "Твой chat id: ")
        bot.send_message(message.chat.id, message.chat.id)
    elif message.text == "/user_id" or message.text == "/user_id" + config.referenseBot:
        bot.send_message(message.chat.id, "Твой user id: ")
        bot.send_message(message.chat.id, message.from_user.id)
    elif message.text == "/id" or message.text == "/id" + config.referenseBot:
        bot.send_message(message.chat.id,
                         "Неправильно использовал комманду! /id<chat_id> or <user_id> Например: /id" +
                         str(config.exampleID))
    elif message.text == "/id" + str(message.chat.id):
        bot.send_message(message.chat.id, "Ты отправил мне свой chat id: " + str(message.chat.id))
    elif message.text == "/id" + str(message.from_user.id):
        bot.send_message(message.chat.id, "Ты отправил мне свой user id: " + str(message.from_user.id))
    elif message.text == "/help" or message.text == "/help" + config.referenseBot:
        bot.send_message(message.chat.id, "Тут будет находиться помощь")
    elif message.text == "/id" + str(config.exampleID) or message.text == "/id" + str(config.exampleID) + config.referenseBot:
        bot.send_message(message.chat.id, "Неверный id! Ты использовал пример!")
    elif message.text == "Замены":
        bot.send_message(message.chat.id, "Замены в расписании находятся на этом сайте:")
        bot.send_message(message.chat.id, config.replacement)
    elif message.text == '/1 171 monday':
        for i in range(1, 11):
            bot.send_message(message.chat.id, "Lesson " + str(i) + ": " + str(parsing.pars.monday1171[i]))
    elif message.text == '/1 171 tuesday':
        for i in range(1, 11):
            bot.send_message(message.chat.id, "Lesson " + str(i) + ": " + str(parsing.pars.tuesday1171[i]))
    elif message.text == '/1 171 wednesday':
        for i in range(1, 11):
            bot.send_message(message.chat.id, "Lesson " + str(i) + ": " + str(parsing.pars.wednesday1171[i]))
    elif message.text == '/1 171 thursday':
        for i in range(1, 11):
            bot.send_message(message.chat.id, "Lesson " + str(i) + ": " + str(parsing.pars.thursday1171[i]))
    elif message.text == '/1 171 friday':
        for i in range(1, 11):
            bot.send_message(message.chat.id, "Lesson " + str(i) + ": " + str(parsing.pars.friday1171[i]))
    elif message.text == '/1 171 saturday':
        for i in range(1, 11):
            bot.send_message(message.chat.id, "Lesson " + str(i) + ": " + str(parsing.pars.saturday1171[i]))
    else:
        bot.send_message(message.chat.id, "Я тебя не понимаю, используй /help")


bot.polling(none_stop=True, interval=0)