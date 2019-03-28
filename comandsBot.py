# -*- coding: utf-8 -*-

# import os
# from flask import Flask, request
import logging

import telebot

import config
import parsing
from admin import main_admin

# from bs4 import BeautifulSoup

idAdmin = config.adminUserId
idAdmin2 = config.adminUserId2

bot = telebot.TeleBot(config.tokenTel)

logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)


@bot.message_handler(content_types=["text"])
def messages(message):
    if message.text == "/start" or message.text == "/start" + config.referenseBot:
        bot.reply_to(message, "Привет, " + message.from_user.username + "! Я только учусь и меня все еще разрабатывают. Не суди строго, если будут ошибки")
    elif message.text == "/admin" or message.text == "/admin" + config.referenseBot:
        if message.from_user.id == idAdmin or message.from_user.id == idAdmin2:
            bot.send_message(message.from_user.id, "Ты в панели администратора. Можешь воспользоваться /helpAdmin")
            main_admin()
        else:
            bot.send_message(message.from_user.id,
                             "Я тебе не дам доступ к панели администратора! Ты не fozema67 и не viper47!")
    elif message.text == "/about" or message.text == "/about" + config.referenseBot:
        bot.send_message(message.chat.id, "version: " + config.version + " build: " + config.build + "\nbuild date: " + config.builddate + "\nAuthor: " + config.author + "\nGithub:"+ config.authorGit)
    elif message.text == "/help" or message.text == "/help" + config.referenseBot:
        bot.send_message(message.chat.id, "/replacement - замены в расписании (актуально для всех групп)" +
                                          "\n/schedule - расписание пар" +
                                          "\n/185monday - расписание на понедельник 185 группа" +
                                          "\n/185tuesday - расписание на вторник 185 группа" +
                                          "\n/185wednesday - расписание на среду 185 группа" +
                                          "\n/185thursday - расписание на четверг 185 группа" +
                                          "\n/185friday - расписание на пятницу 185 группа" +
                                          "\n/185saturday - расписание на субботу 185 группа" +
                                          "\n/185all_week - Расписание занятий на всю неделю для 185 группы"
                                          "\n/about - О боте")
    elif message.text == "/replacement":
        bot.send_message(message.chat.id, "Замены в расписании находятся на этом сайте:")
        bot.send_message(message.chat.id, config.replacement)
    elif message.text == "/schedule" or message.text == "/schedule" + config.referenseBot:
        for i in range(0, 4):
            bot.send_message(message.chat.id,  "Pair " + str(i+1) + ": " + str(config.schedule[i+1]))
    elif message.text == "/185monday" or message.text == "/185monday" + config.referenseBot:
        for i in range(1, 9):
            bot.send_message(message.chat.id, "Lesson " + str(i) + ": " + str(parsing.pars.monday185[i]))
    elif message.text == "/185tuesday" or message.text == "/185tuesday" + config.referenseBot:
        for i in range(1, 9):
            bot.send_message(message.chat.id, "Lesson " + str(i) + ": " + str(parsing.pars.tuesday185[i]))
    elif message.text == "/185wednesday" or message.text == "/185wednesday" + config.referenseBot:
        for i in range(1, 9):
            bot.send_message(message.chat.id, "Lesson " + str(i) + ": " + str(parsing.pars.wednesday185[i]))
    elif message.text == "/185thursday" or message.text == "/185thursday" + config.referenseBot:
        for i in range(1, 9):
            bot.send_message(message.chat.id, "Lesson " + str(i) + ": " + str(parsing.pars.thursday185[i]))
    elif message.text == "/185friday" or message.text == "/185friday" + config.referenseBot:
        for i in range(1, 9):
            bot.send_message(message.chat.id, "Lesson " + str(i) + ": " + str(parsing.pars.friday185[i]))
    elif message.text == "/185saturday" or message.text == "/185saturday" + config.referenseBot:
        for i in range(1, 9):
            bot.send_message(message.chat.id, "Lesson " + str(i) + ": " + str(parsing.pars.saturday185[i]))
    elif message.text == "/185mondaynew" or message.text == "/185mondaynew" + config.referenseBot:
        for i in range(1, 5):
            mondaynew185 = parsing.pars.monday185[::2]
            bot.send_message(message.chat.id, "Monday:")
            bot.send_message(message.chat.id, str(i) + ". " + str(mondaynew185[i]))
    elif message.text == "/185tuesdaynew" or message.text == "/185tuesdaynew" + config.referenseBot:
        for i in range(1, 5):
            tuesdaynew185 = parsing.pars.monday185[::2]
            bot.send_message(message.chat.id, "Tuesday:")
            bot.send_message(message.chat.id, str(i) + ". " + str(tuesdaynew185[i]))
    elif message.text == "/185wednesdaynew" or message.text == "/185wednesdaynew" + config.referenseBot:
        for i in range(1, 5):
            wednesdaynew185 = parsing.pars.monday185[::2]
            bot.send_message(message.chat.id, "Tuesday:")
            bot.send_message(message.chat.id, str(i) + ". " + str(wednesdaynew185[i]))
    elif message.text == "/185thursdaynew" or message.text == "/185thursdaynew" + config.referenseBot:
        for i in range(1, 5):
            thursdaynew185 = parsing.pars.monday185[::2]
            bot.send_message(message.chat.id, "Tuesday:")
            bot.send_message(message.chat.id, str(i) + ". " + str(thursdaynew185[i]))
    elif message.text == "/185fridaynew" or message.text == "/185fridaynew" + config.referenseBot:
        for i in range(1, 5):
            fridaynew185 = parsing.pars.monday185[::2]
            bot.send_message(message.chat.id, "Tuesday:")
            bot.send_message(message.chat.id, str(i) + ". " + str(fridayew185[i]))
    elif message.text == "/185saturdaynew" or message.text == "/185saturdaynew" + config.referenseBot:
        for i in range(1, 5):
            saturdaynew185 = parsing.pars.monday185[::2]
            bot.send_message(message.chat.id, "Tuesday:")
            bot.send_message(message.chat.id, str(i) + ". " + str(saturdaynew185[i]))
    elif message.text == "/185all_week" or message.text == "/185all_week" + config.referenseBot:
        for i in range(1, 5):
            monday1185 = parsing.pars.monday185[::2]
            bot.send_message(message.chat.id, "Monday: " + str(i) + ". " + str(monday1185[i]))
        for i in range(1, 5):
            tuesday1185 = parsing.pars.tuesday185[::2]
            bot.send_message(message.chat.id, "Tuesday: " + str(i) + ". " + str(tuesday1185[i]))
        for i in range(1, 5):
            wednesday1185 = parsing.pars.wednesday185[::2]
            bot.send_message(message.chat.id, "Wednesday: " + str(i) + ". " + str(wednesday1185[i]))
        for i in range(1, 5):
            thursday1185 = parsing.pars.thursday185[::2]
            bot.send_message(message.chat.id, "Thursday: " + str(i) + ". " + str(thursday1185[i]))
        for i in range(1, 5):
            friday1185 = parsing.pars.friday185[::2]
            bot.send_message(message.chat.id, "Friday: " + str(i) + ". " + str(friday1185[i]))
        for i in range(1, 5):
            saturday1185 = parsing.pars.saturday185[::2]
            bot.send_message(message.chat.id, "Saturday: " + str(i) + ". " + str(saturday1185[i]))
    else:
        bot.send_message(message.chat.id, "Я тебя не понимаю, используй /help")


bot.polling(none_stop=True, interval=0)
