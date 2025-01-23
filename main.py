import telebot
import buttons
import types
token = "7922935456:AAHMOi1tmtI_mT5QuK_CdgzlYCYAkWmq_NY"
bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start"])
def start(message):
    buttons.button_bot(message, bot, types)


bot.infinity_polling()