# -*- coding: utf-8 -*-

# import os
# from flask import Flask, request
import logging

import telebot

import config
import parsing
from admin import cmd_admin

# from bs4 import BeautifulSoup

bot = telebot.TeleBot(config.tokenTel)

logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)


@bot.message_handler(content_types=["text"])
def messages(message):
    if message.text == "/start" or message.text == "/start" + config.referenseBot:
        bot.reply_to(message, "Привет, " + message.from_user.username + "! Я только учусь и меня все еще разрабатывают. Не суди строго, если будут ошибки")
    elif message.text == "/key_t" or message.text == "/key_t" + config.referenseBot:
        cmd_admin(message)
    elif message.text == "/about" or message.text == "/about" + config.referenseBot:
        bot.send_message(message.chat.id, "version: " + config.version + " build: " + config.build + "\nbuild date: " + config.builddate)
    elif message.text == "/help" or message.text == "/help" + config.referenseBot:
        bot.send_message(message.chat.id, "/replacement - замены в расписании (актуально для всех групп)" +
                                          "\n/schedule - расписание пар" +
                                          "\n/185monday - расписание на понедельник 185 группа" +
                                          "\n/185tuesday - расписание на вторник 185 группа" +
                                          "\n/185wednesday - расписание на среду 185 группа" +
                                          "\n/185thursday - расписание на четверг 185 группа" +
                                          "\n/185friday - расписание на пятницу 185 группа" +
                                          "\n/185saturday - расписание на субботу 185 группа" +
                                          "\n/about - О боте")
    elif message.text == "/replacement":
        bot.send_message(message.chat.id, "Замены в расписании находятся на этом сайте:")
        bot.send_message(message.chat.id, config.replacement)
    elif message.text == "/schedule" or message.text == "/schedule" + config.referenseBot:
        for i in range(0, 5):
            bot.send_message(message.chat.id,  "Pair " + str(i+1) + ": " + str(config.schedule[i+1]))
    elif message.text == '/185monday' or message.text == "/185monday" + config.referenseBot:
        for i in range(1, 9):
            bot.send_message(message.chat.id, "Lesson " + str(i) + ": " + str(parsing.pars.monday185[i]))
    elif message.text == '/185tuesday' or message.text == "/185tuesday" + config.referenseBot:
        for i in range(1, 9):
            bot.send_message(message.chat.id, "Lesson " + str(i) + ": " + str(parsing.pars.tuesday185[i]))
    elif message.text == '/185wednesday' or message.text == "/185wednesday" + config.referenseBot:
        for i in range(1, 9):
            bot.send_message(message.chat.id, "Lesson " + str(i) + ": " + str(parsing.pars.wednesday185[i]))
    elif message.text == '/185thursday' or message.text == "/185thursday" + config.referenseBot:
        for i in range(1, 9):
            bot.send_message(message.chat.id, "Lesson " + str(i) + ": " + str(parsing.pars.thursday185[i]))
    elif message.text == '/185friday' or message.text == "/185friday" + config.referenseBot:
        for i in range(1, 9):
            bot.send_message(message.chat.id, "Lesson " + str(i) + ": " + str(parsing.pars.friday185[i]))
    elif message.text == '/185saturday' or message.text == "/185saturday" + config.referenseBot:
        for i in range(1, 9):
            bot.send_message(message.chat.id, "Lesson " + str(i) + ": " + str(parsing.pars.saturday185[i]))
    else:
        bot.send_message(message.chat.id, "Я тебя не понимаю, используй /help")


bot.polling(none_stop=True, interval=0)