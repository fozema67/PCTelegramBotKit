# -*- coding: utf-8 -*-

# import os
# from flask import Flask, request
import logging

import pyowm
import telebot

import config
import parsing
from admin import cmd_admin

# from bs4 import BeautifulSoup

bot = telebot.TeleBot(config.tokenTel)
owm = pyowm.OWM(config.APIKeyOWM)

logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)


@bot.message_handler(content_types=["text"])
def messages(message):
    if message.text == "/start" or message.text == "/start" + config.referenseBot:
        bot.reply_to(message, "Привет, " + message.from_user.username + "! Я только учусь и меня все еще разрабатывают. Не суди строго, если будут ошибки")
    elif message.text == "/key_t" or message.text == "/key_t" + config.referenseBot:
        cmd_admin(message)
    elif message.text == "/help" or message.text == "/help" + config.referenseBot:
        bot.send_message(message.chat.id, "/replacement - замены в расписании (актуально для всех групп)" +
                                          "\n/schedule - расписание пар" +
                                          "\n/185monday - расписание на понедельник 185 группа" +
                                          "\n/185tuesday - расписание на вторник 185 группа" +
                                          "\n/185wednesday - расписание на среду 185 группа" +
                                          "\n/185thursday - расписание на четверг 185 группа" +
                                          "\n/185friday - расписание на пятницу 185 группа" +
                                          "\n/185saturday - расписание на субботу 185 группа")
    elif message.text == "/replacement":
        bot.send_message(message.chat.id, "Замены в расписании находятся на этом сайте:")
        bot.send_message(message.chat.id, config.replacement)
    elif message.text == "/schedule":
        for i in range(0, 5):
            bot.send_message(message.chat.id,  "Pair " + str(i+1) + ": " + str(config.schedule[i+1]))
    elif message.text == '/185monday':
        for i in range(1, 9):
            bot.send_message(message.chat.id, "Lesson " + str(i) + ": " + str(parsing.pars.monday185[i]))
    elif message.text == '/185tuesday':
        for i in range(1, 9):
            bot.send_message(message.chat.id, "Lesson " + str(i) + ": " + str(parsing.pars.tuesday185[i]))
    elif message.text == '/185wednesday':
        for i in range(1, 9):
            bot.send_message(message.chat.id, "Lesson " + str(i) + ": " + str(parsing.pars.wednesday185[i]))
    elif message.text == '/185thursday':
        for i in range(1, 9):
            bot.send_message(message.chat.id, "Lesson " + str(i) + ": " + str(parsing.pars.thursday185[i]))
    elif message.text == '/185friday':
        for i in range(1, 9):
            bot.send_message(message.chat.id, "Lesson " + str(i) + ": " + str(parsing.pars.friday185[i]))
    elif message.text == '/185saturday':
        for i in range(1, 9):
            bot.send_message(message.chat.id, "Lesson " + str(i) + ": " + str(parsing.pars.saturday185[i]))
    else:
        bot.send_message(message.chat.id, "Я тебя не понимаю, используй /help")


bot.polling(none_stop=True, interval=0)