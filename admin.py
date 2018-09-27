import logging

import telebot

import config
import mainBot

bot = telebot.TeleBot(config.tokenTel)
idAdmin = config.adminUserId
idAdmin2 = config.adminUserId2

logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)

def main_admin(message):
    if message.text == "/key_t" or message.text == "/key_t" + config.referenseBot:
        bot.send_message(message.chat.id, config.tokenTel)
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю! воспользуйся командой /helpAdmin")
        main_admin(message)


mainBot
