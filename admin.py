import logging

import telebot

import config
import mainBot

bot = telebot.TeleBot(config.tokenTel)
idAdmin = config.adminUserId
idAdmin2 = config.adminUserId2

logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)

@bot.message_handler(content_types=["text"])
def cmd_admin(message):
    if message.from_user.id == idAdmin or message.from_user.id == idAdmin2:
        def main_admin(message):
            if message.text == "/key_t" and message.from_user.id == idAdmin:
                bot.send_message(message.from_user.id, config.tokenTel)
            elif message.text == "/key_t" or message.text == "/key_t" + config.referenseBot:
                bot.send_message(message.chat.id, config.tokenTel)
            else:
                bot.send_message(message.from_user.id, "Я тебя не понимаю! воспользуйся командой /helpAdmin")
                main_admin(message)
    else:
        bot.send_message(message.from_user.id, "Я тебе не дам ключ доступа! Ты не fozema67 и не viper47!")


mainBot
