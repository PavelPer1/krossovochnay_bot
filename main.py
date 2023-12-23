import telebot

TOKEN = '6969995095:AAFYoCyP9sYiBnDEJsIuZSgiAihXMImNNHI'
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('Рассчитать стоимость', 'Оставить заявку')
    bot.send_message(message.chat.id, "Выберите действие:", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == 'Рассчитать стоимость')
def calculate_price(message):
    bot.send_message(message.chat.id, """Укажите цену товара в ЮАНЯХ (¥)

❗️Указывайте верную стоимость товара, иначе заказ будет отменён. Цена может меняться в зависимости от размера и цвета. ОЧЕНЬ ВАЖНО!

❗️По волнистой линии "≈" НЕ ВЫКУПАЕМ!

❗️ВНИМАНИЕ! Выбирайте цену которая ЗАЧЕРКНУТА. Система отображает скидки для первых покупателей. У нас нет этих скидок.""")


@bot.message_handler(func=lambda message: message.text == 'Оставить заявку')
def leave_order(message):
    bot.send_message(message.chat.id, """Введите ваше имя и фамилию, а также цену товара в ЮАНЯХ (¥)
Пример: Иван Иванов - 500""")



@bot.message_handler(func=lambda message: message.text.isdigit())
def handle_price_input(message):
    user_input = float(message.text)
    rubles = user_input * 13.5
    delivery_cost = 1000
    if rubles > 10000:
        total_price = rubles + delivery_cost + 2000
    else:
        total_price = rubles + delivery_cost + 1000
    bot.send_message(message.chat.id, f"Стоимость товара в рублях: {total_price} руб.")

    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('Оставить заявку')
    bot.send_message(message.chat.id, "Хотите оставить заявку?", reply_markup=markup)


@bot.message_handler(func=lambda message: not message.text.isdigit())
def handle_order_input(message):
    user_info = message.text
    bot.send_message("-4040121997", f"Новая заявка: {user_info} - @{message.chat.username}")
    bot.send_message(message.chat.id, "Спасибо за вашу заявку! Мы свяжемся с вами в ближайшее время.")


bot.polling()