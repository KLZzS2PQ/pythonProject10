import telebot
token = "7922935456:AAHMOi1tmtI_mT5QuK_CdgzlYCYAkWmq_NY"
bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start"])
def start(message):
    pass


bot.infinity_polling()