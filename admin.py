import telebot
import logging
import config
import mainBot

bot = telebot.TeleBot(config.tokenTel)
idAdmin = config.adminUserId
idAdmin2 = config.adminUserId2

logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)


def cmd_admin(message):
    if message.text == "/key_t" and message.from_user.id == idAdmin:
        bot.send_message(message.from_user.id, config.tokenTel)
    elif message.text == "/key_t@test_fozema67Bot" and message.from_user.id == idAdmin or message.from_user.id == idAdmin2:
        bot.send_message(message.chat.id, config.tokenTel)
    elif message.text == "/key_ai" and message.from_user.id == idAdmin:
        bot.send_message(message.from_user.id, config.tokenDial)
    elif message.text == "/key_ai@test_fozema67Bot" and message.from_user.id == idAdmin or message.from_user.id == idAdmin2:
        bot.send_message(message.chat.id, config.tokenDial)
    else:
        bot.send_message(message.from_user.id, "Я тебе не дам ключ доступа! Ты не fozema67 и не viper47!")


mainBot
