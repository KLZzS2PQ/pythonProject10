

def button_bot(message, bot, types):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton("Click"))
    bot.send_message(message.chat.id, "Click button", reply_markup=markup)