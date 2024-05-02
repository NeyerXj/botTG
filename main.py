import datetime
import secrets

import telebot
from telebot.types import User
from io import StringIO, BytesIO
from telebot import types
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import db





# Получаем ссылку на Realtime Database

cred = credentials.Certificate("serviceAccountKey.json")



firebase_admin.initialize_app(cred,{
    'databaseURL': 'https://khlmdb-c9a33-default-rtdb.firebaseio.com'
})

ref = db.reference()

BOT_TOKEN = '6341950481:AAFQ1T2eV4rMvG2cJqb4aoVmouUb_xn56jg'

bot = telebot.TeleBot(BOT_TOKEN)
global sent_message
@bot.message_handler(commands=['start'])
def send_welcome(message):
    ref = db.reference("/users")

    # Получаем данные по указанному пути
    users_data = ref.get()
    if users_data and any(name == str(message.chat.id) for name in users_data.keys()):
        send_menu_message(message, str(db.reference("/users").child(str(message.chat.id)).get()))
        return
    else: bot.send_message(message.chat.id, "Введите код доспута:")

@bot.message_handler(func=lambda message: message.text.isdigit())
def handle_digits(message):
    # Получаем текст сообщения, отправленного пользователем
    text = message.text
    # Получаем идентификатор чата
    chat_id = message.chat.id
    ref = db.reference("/users")

# Получаем данные по указанному пути
    users_data = ref.get()
    if users_data and any(name == str(message.chat.id) for name in users_data.keys()):
        send_menu_message(message, str(db.reference("/users").child(str(message.chat.id)).get()))
        return

    def switch_case(argument):
        if argument == int(db.reference("/keys/11a").get()):
            bot.send_message(message.chat.id, "11a")
            db.reference("/users").child(str(message.chat.id)).set("11a")
            send_menu_message(message, str(db.reference("/users").child(str(message.chat.id)).get()))
            return
        elif argument == int(db.reference("/keys/11b").get()):
            bot.send_message(message.chat.id, "11b")
            db.reference("/users").child(str(message.chat.id)).set("11b")
            send_menu_message(message, str(db.reference("/users").child(str(message.chat.id)).get()))
            return
        elif argument == int(db.reference("/keys/10a").get()):
            bot.send_message(message.chat.id, "10a")
            db.reference("/users").child(str(message.chat.id)).set("10a")
            send_menu_message(message, str(db.reference("/users").child(str(message.chat.id)).get()))
            return
        elif argument == int(db.reference("/keys/10b").get()):
            bot.send_message(message.chat.id, "10b")
            db.reference("/users").child(str(message.chat.id)).set("10b")
            send_menu_message(message, str(db.reference("/users").child(str(message.chat.id)).get()))
        elif argument == int(db.reference("/keys/9a").get()):
            bot.send_message(message.chat.id, "9a")
            db.reference("/users").child(str(message.chat.id)).set("9a")
            send_menu_message(message, str(db.reference("/users").child(str(message.chat.id)).get()))
        elif argument == int(db.reference("/keys/9b").get()):
            bot.send_message(message.chat.id, "9b")
            db.reference("/users").child(str(message.chat.id)).set("9b")
            send_menu_message(message, str(db.reference("/users").child(str(message.chat.id)).get()))
        elif argument == int(db.reference("/keys/8a").get()):
            bot.send_message(message.chat.id, "8a")
            db.reference("/users").child(str(message.chat.id)).set("8a")
            send_menu_message(message, str(db.reference("/users").child(str(message.chat.id)).get()))
        elif argument == int(db.reference("/keys/8b").get()):
            bot.send_message(message.chat.id, "8b")
            db.reference("/users").child(str(message.chat.id)).set("8b")
            send_menu_message(message, str(db.reference("/users").child(str(message.chat.id)).get()))
        elif argument == int(db.reference("/keys/7a").get()):
            bot.send_message(message.chat.id, "7a")
            db.reference("/users").child(str(message.chat.id)).set("7a")
            send_menu_message(message, str(db.reference("/users").child(str(message.chat.id)).get()))
        elif argument == int(db.reference("/keys/7b").get()):
            bot.send_message(message.chat.id, "7b")
            db.reference("/users").child(str(message.chat.id)).set("7b")
            send_menu_message(message, str(db.reference("/users").child(str(message.chat.id)).get()))
        elif argument == int(db.reference("/keys/6a").get()):
            bot.send_message(message.chat.id, "6a")
            db.reference("/users").child(str(message.chat.id)).set("6a")
            send_menu_message(message, str(db.reference("/users").child(str(message.chat.id)).get()))
        elif argument == int(db.reference("/keys/6b").get()):
            bot.send_message(message.chat.id, "6b")
            db.reference("/users").child(str(message.chat.id)).set("6b")
            send_menu_message(message, str(db.reference("/users").child(str(message.chat.id)).get()))
        elif argument == int(db.reference("/keys/5a").get()):
            bot.send_message(message.chat.id, "5a")
            db.reference("/users").child(str(message.chat.id)).set("5a")
            send_menu_message(message, str(db.reference("/users").child(str(message.chat.id)).get()))
        elif argument == int(db.reference("/keys/5b").get()):
            bot.send_message(message.chat.id, "5b")
            db.reference("/users").child(str(message.chat.id)).set("5b")
            send_menu_message(message, str(db.reference("/users").child(str(message.chat.id)).get()))
        else:
            return

    switch_case(int(text))

def send_menu_message(message, cls):
    bot.send_message(message.chat.id, "Привіт 👋\nЯ,"+str(cls)+" Чат-бот, який допомагає у навчанні 🤓\nУ моїх розділах, ти знайдеш усе необхідне 📂\nХочу ознайомити з моїми основними функціями:"
                          "\n📅 Актуальний розклад уроків -/rozklad\n📚 Усі підручники у електронному вигляді-/pidruchnyky\n📱 Контакти вчителів для надсилання завдань -/kontakty_menu\nℹ️ Важлива інформація, посилання на класну групу та сайт школи -/infomation\n👩‍🏫 Класрум - /classroom\n💡 Якщо маєш якісь ідеї або побажання що до бота, запрошуємо написати про це - /1k\nСподіваюсь, що я зможу тобі допомогти, і не сумуй якщо знайдеш якісь помилки або неточності. При знаходженні їх, напиши про це будь ласка моїм адмінам - /napishy1 🧑‍💻\n📍 Якщо знову буде потрібна допомога, викликай це меню внизу списку, або натискай - /help_bot 🤖\nНаснаги у навчанні! 📚"
                          "\n")
    markup = types.ReplyKeyboardMarkup(row_width=2)
    item1 = types.KeyboardButton("📚 ПІДРУЧНИКИ 📚")
    item2 = types.KeyboardButton("📨 КОНТАКТИ 📨")
    item3 = types.KeyboardButton("📆 РОЗКЛАД 📆")
    item4 = types.KeyboardButton("👩‍🏫 CLASSROOM 👩‍🏫")
    item5 = types.KeyboardButton("👤 HUMAN 👤")
    item6 = types.KeyboardButton("🛠️ ФУНКЦІЇ БОТА 🛠️")
    item7 = types.KeyboardButton("ЗВОРОТНІЙ ЗВ'ЯЗОК")
    markup.add(item1, item2, item3,item4,item5,item6,item7)

    bot.send_message(message.chat.id, "Выберите опцию:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "btn-movu":
        global sent_message
        keyboard = types.InlineKeyboardMarkup(row_width=1)
    # Создаем кнопки
        print(db.reference("/users").child(str(call.message.chat.id)).get())
        user_data = db.reference("/users").child(str(call.message.chat.id)).get()
        def switch_case(user_data):
            global sent_message
            if user_data in ["10b", "10a"]:
                button1 = types.InlineKeyboardButton(text="🇺🇦 Українська мова ✍️",
                                                     url="https://drive.google.com/file/d/1hdldUZ1XhIKCnBSb66C7SKbrdoXW3osr/view?usp=drivesdk")
                button2 = types.InlineKeyboardButton(text="🇺🇦 Українська література 📚",
                                                     url="https://drive.google.com/file/d/1-tWF8VFdsLOdAVQI2-MauA87gtLEYafM/view?usp=drivesdk")
                button3 = types.InlineKeyboardButton(text="🌍 Зарубіжна література 📚 ",
                                                     url="https://drive.google.com/file/d/1wOf82olgYQ4m8GLAGtfRFufuOYjJ2Ji3/view?usp=drivesdk")
                button4 = types.InlineKeyboardButton(text="🇬🇧 Англійська💂🏻‍♀️",
                                                     url="https://drive.google.com/file/d/16MlY6TCpZK1JAx8tKC6NGXP_G09WFwpF/view?usp=drivesdk")
                button5 = types.InlineKeyboardButton(text="Назад", callback_data="btn-back")
                bot.delete_message(call.message.chat.id, sent_message.message_id)
                # Добавляем кнопки на клавиатуру
                keyboard.add(button1, button2, button3, button4, button5)
                # Отправляем сообщение с кнопками в самом сообщении
                sent_message = bot.send_message(call.message.chat.id, "Оберіть підручник:", reply_markup=keyboard)
            elif user_data in ["11b", "11a"]:
                button1 = types.InlineKeyboardButton(text="🇺🇦 Українська мова ✍️",
                                                     url="https://drive.google.com/file/d/1aMGa4ZKTnXWzLdkN215hvDUuWzkX0ymy/view")
                button2 = types.InlineKeyboardButton(text="🇺🇦 Українська література 📚",
                                                     url="https://drive.google.com/file/d/1uxIfts0xnnxEYNAJos4ajxv3F5IWbuZx/view")
                button3 = types.InlineKeyboardButton(text="🌍 Зарубіжна література 📚",
                                                     url="https://drive.google.com/file/d/15pJoKyRyMVEVAHbz_wGVtNZcR4kqGSpT/view")
                button4 = types.InlineKeyboardButton(text="🇬🇧 Англійська💂🏻‍♀️",
                                                     url="https://drive.google.com/file/d/1Huw61NnGj5sj4wYklbuKVO3PiPoBR0a_/view")
                button5 = types.InlineKeyboardButton(text="Назад", callback_data="btn-back")
                bot.delete_message(call.message.chat.id, sent_message.message_id)
                keyboard.add(button1, button2, button3, button4, button5)
                sent_message = bot.send_message(call.message.chat.id, "Оберіть підручник:", reply_markup=keyboard)
            elif user_data in ["9b", "9a"]:
                button1 = types.InlineKeyboardButton(text="🇺🇦 Українська мова ✍️",
                                                     url="")
                button2 = types.InlineKeyboardButton(text="🇺🇦 Українська література 📚",
                                                     url="https://drive.google.com/file/d/1tbp_ME781Ie0SNlJC2SYsg2inivz0un7/view?usp=drive_link")
                button3 = types.InlineKeyboardButton(text="🌍 Зарубіжна література 📚",
                                                     url="https://drive.google.com/file/d/1X-JkVpK6n1AaZ9LWoqQeE0DPWOokaNbl/view?usp=drive_link")
                button4 = types.InlineKeyboardButton(text="🇬🇧 Англійська💂🏻‍♀️",
                                                     url="")
                button5 = types.InlineKeyboardButton(text="Назад", callback_data="btn-back")
                bot.delete_message(call.message.chat.id, sent_message.message_id)
                keyboard.add(button1, button2, button3, button4, button5)
                sent_message = bot.send_message(call.message.chat.id, "Оберіть підручник:", reply_markup=keyboard)
            elif user_data in ["8b", "8a"]:
                button1 = types.InlineKeyboardButton(text="🇺🇦 Українська мова ✍️",
                                                     url="https://drive.google.com/file/d/1dLgFhR3ZDCyWh0YFtpDF8_u5iKMkl29e/view?usp=drive_link")
                button2 = types.InlineKeyboardButton(text="🇺🇦 Українська література 📚",
                                                     url="https://drive.google.com/file/d/1p6myE29HG7-Ciy0-yWNVen_0z7ZtIiJV/view?usp=drive_link")
                button3 = types.InlineKeyboardButton(text="🌍 Зарубіжна література(Ніколенко) 📚",
                                                     url="https://drive.google.com/file/d/1XihAsROxOf_3-jvjuxFw88CiSW-YcnGU/view?usp=drive_link")
                button4 = types.InlineKeyboardButton(text="🌍 Зарубіжна література(Волощук) 📚",
                                                     url="https://drive.google.com/file/d/18WddhsBdjhxyuCw3KvgEJK8VFVW3iXQe/view?usp=drive_link")
                button5 = types.InlineKeyboardButton(text="🇬🇧 Англійська💂🏻‍♀️",
                                                     url="https://drive.google.com/file/d/1ddiQsWkG3iPSPoalZX8bnOSh8l-43PTy/view?usp=drive_link")
                button6 = types.InlineKeyboardButton(text="Назад", callback_data="btn-back")
                bot.delete_message(call.message.chat.id, sent_message.message_id)
                keyboard.add(button1, button2, button3, button4, button5, button6)
                sent_message = bot.send_message(call.message.chat.id, "Оберіть підручник:", reply_markup=keyboard)
            elif user_data in ["7b", "7a"]:
                button1 = types.InlineKeyboardButton(text="🇺🇦 Українська мова ✍️",
                                                     url="https://drive.google.com/file/d/1l0BTIQT-d9FFYUM3j8HHt0qOVWGcdqiR/view?usp=drive_link")
                button2 = types.InlineKeyboardButton(text="🇺🇦 Українська мова(Заболотний) ✍️",
                                                     url="https://drive.google.com/file/d/1DtLcNtKIp28loAMivkDh3gu7-Nc-IgXM/view?usp=drive_link")
                button3 = types.InlineKeyboardButton(text="🇺🇦 Українська література 📚",
                                                     url="https://drive.google.com/file/d/1QAKBUdpNwmjb-0dxTFycD1GFnrluMTrv/view?usp=drive_link")
                button4 = types.InlineKeyboardButton(text="🌍 Зарубіжна література 📚",
                                                     url="https://drive.google.com/file/d/1Z9b9YymwZGb8R4g4zbD7WYA5alUym4w2/view?usp=drive_link")
                button5 = types.InlineKeyboardButton(text="🇬🇧 Англійська💂🏻‍♀️",
                                                     url="https://drive.google.com/file/d/1H-8ir9OQ2ITVNvEFg7AuOantkvQCyPlU/view?usp=drive_link")
                button6 = types.InlineKeyboardButton(text="Назад", callback_data="btn-back")
                bot.delete_message(call.message.chat.id, sent_message.message_id)
                keyboard.add(button1, button2, button3, button4, button5, button6)
                sent_message = bot.send_message(call.message.chat.id, "Оберіть підручник:", reply_markup=keyboard)
            elif user_data in ["6b", "6a"]:
                button1 = types.InlineKeyboardButton(text="🇺🇦 Українська мова ✍️",
                                                     url="https://drive.google.com/file/d/12bt5pWPt211NnXjg9Dc23nR0U-3NfMgx/view?usp=drive_link")
                button2 = types.InlineKeyboardButton(text="🇺🇦 Українська література 📚",
                                                     url="https://drive.google.com/file/d/1GHepqGnEQyd05oU6NGRRVwNlBneetHif/view?usp=drive_link")
                button3 = types.InlineKeyboardButton(text="🌍 Зарубіжна література 📚",
                                                     url="https://drive.google.com/file/d/1ba4bTE5vSYZu4vfG_0SKXocxcYj6QQJm/view?usp=drive_link")
                button4 = types.InlineKeyboardButton(text="🇬🇧 Англійська💂🏻‍♀️",
                                                     url="https://drive.google.com/file/d/1jE0FOF48w6wMypd5RfDEuNYgnFnTZ7QE/view?usp=drive_link")
                button5 = types.InlineKeyboardButton(text="Назад", callback_data="btn-back")
                bot.delete_message(call.message.chat.id, sent_message.message_id)
                keyboard.add(button1, button2, button3, button4, button5)
                sent_message = bot.send_message(call.message.chat.id, "Оберіть підручник:", reply_markup=keyboard)
            elif user_data in ["5b", "5a"]:
                button1 = types.InlineKeyboardButton(text="🇺🇦 Українська мова ✍️",
                                                     url="https://drive.google.com/file/d/1YBavYsbOpJQLhN7GJMv8-PcVy0z0u-16/view?usp=drive_link")
                button2 = types.InlineKeyboardButton(text="🇺🇦 Українська література 📚",
                                                     url="https://drive.google.com/file/d/1XTYmJrTih9w8uuAmhytq4QscUNLFEiuz/view?usp=drive_link")
                button3 = types.InlineKeyboardButton(text="🇺🇦 Українська література(2022) 📚",
                                                     url="https://drive.google.com/file/d/1yB5hX6QSHCEGWvbGZwlFlw5YjFaF79kW/view?usp=drive_link")
                button4 = types.InlineKeyboardButton(text="🌍 Зарубіжна література 📚",
                                                     url="https://drive.google.com/file/d/1QID9vaWsNBLHf-zPpklEhMyT5GLSWKH3/view?usp=drive_link")
                button5 = types.InlineKeyboardButton(text="🌍 Зарубіжна література(Ніколенко) 📚",
                                                     url="https://drive.google.com/file/d/1fE_IEIUwa0LFa6e5oxiKJZQaBDLfnpSZ/view?usp=drive_link")
                button6 = types.InlineKeyboardButton(text="🇬🇧 Англійська💂🏻‍♀️",
                                                     url="https://drive.google.com/file/d/1MiYEilgV18HigKGtqeD6p1taH76-dEzT/view?usp=drive_link")
                button7 = types.InlineKeyboardButton(text="Назад", callback_data="btn-back")
                bot.delete_message(call.message.chat.id, sent_message.message_id)
                keyboard.add(button1, button2, button3, button4, button5, button6, button7)
                sent_message = bot.send_message(call.message.chat.id, "Оберіть підручник:", reply_markup=keyboard)
        switch_case(user_data)

    if call.data == "btn-prirod":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        # Создаем кнопки
        if str(db.reference("/users").child(str(call.message.chat.id)).get()) == "10b" or str(db.reference("/users").child(str(call.message.chat.id)).get()) == "10a":
            button1 = types.InlineKeyboardButton(text="Хімія️",url="https://drive.google.com/file/d/1rB53rD99yK-v_Nc8_-kCnLmlue9YG36w/view?usp=drive_link")
            button2 = types.InlineKeyboardButton(text="Фізика",url="https://drive.google.com/file/d/10nvSZMvLV_8PUkXvr6KQ6FQPUfbt__rO/view?usp=drive_link")
            button3 = types.InlineKeyboardButton(text="Географія ",url="https://drive.google.com/file/d/1o7C_ZtT1KSGKPsxpYJco0Y4B1R0Ti0ph/view?usp=drive_link")
            button4 = types.InlineKeyboardButton(text="Біологія️",url="https://drive.google.com/file/d/1MBjTiIHOEyXLZOPr38sd0BqsKDDUQJMy/view?usp=drive_link")
            button5 = types.InlineKeyboardButton(text="Назад", callback_data="btn-back")
            keyboard.add(button1, button2, button3, button4, button5)
            bot.delete_message(call.message.chat.id,sent_message.message_id)
    # Отправляем сообщение с кнопками в самом сообщении
            sent_message = bot.send_message(call.message.chat.id, "Оберіть підручник:", reply_markup=keyboard)
            return
    # Отправляем сообщение с кнопками в самом сообщении
        if db.reference("/users").child(str(call.message.chat.id)).get() == "11b" or db.reference("/users").child(str(call.message.chat.id)).get() == "11a":
            button1 = types.InlineKeyboardButton(text="Хімія️",url="https://drive.google.com/file/d/18cRkncomp9L3lmTir17_mqNElHqlP217/view?usp=drive_link")
            button2 = types.InlineKeyboardButton(text="Фізика",url="https://drive.google.com/file/d/1xrUaPTk45fKR0TGM6CKY-5Za4ieMWXKu/view?usp=drive_link")
            button3 = types.InlineKeyboardButton(text="Географія ",url="https://drive.google.com/file/d/14FP9j8Iewh_q1AwfMGspgY8QIUTYmOcl/view?usp=drive_link")
            button4 = types.InlineKeyboardButton(text="Біологія️",url="https://issuu.com/stankobog/docs/11-klas-biologija-sobol-2019")
            button5 = types.InlineKeyboardButton(text="Астрономія️",url="https://drive.google.com/file/d/1sROfWO-mAsIVduoupXYZf4f3DOEhvgXt/view?usp=drive_link")
            button6 = types.InlineKeyboardButton(text="Назад", callback_data="btn-back")
            keyboard.add(button1, button2, button3, button4, button5, button6)
            bot.delete_message(call.message.chat.id,sent_message.message_id)
    # Отправляем сообщение с кнопками в самом сообщении
            sent_message = bot.send_message(call.message.chat.id, "Оберіть підручник:", reply_markup=keyboard)
            return
        print(sent_message.message_id)


    if call.data == "btn-zagalK":
        bot.delete_message(call.message.chat.id,sent_message.message_id)
        with open('zagalK.txt', 'r', encoding='utf-8') as file:
          content = file.read()
        photo = open('kontZagal.png', 'rb')
        bot.send_photo(call.message.chat.id, photo, caption=content)
    if call.data == "btn-myzKont":
        bot.delete_message(call.message.chat.id,sent_message.message_id)
        with open('myzK.txt', 'r', encoding='utf-8') as file:
            content = file.read()
        photo = open('myzKont.png', 'rb')
        bot.send_photo(call.message.chat.id, photo, caption=content)
    if call.data == "btn-teatrKont":
        bot.delete_message(call.message.chat.id,sent_message.message_id)
        with open('teatralK.txt', 'r', encoding='utf-8') as file:
            content = file.read()
        photo = open('kontteatr.png', 'rb')
        bot.send_photo(call.message.chat.id, photo, caption=content)
    if call.data == "btn-myzKoreograph":
        bot.delete_message(call.message.chat.id,sent_message.message_id)
        with open('khoreographK.txt', 'r', encoding='utf-8') as file:
            content = file.read()
        photo = open('khotografPic.png', 'rb')
        bot.send_photo(call.message.chat.id, photo, caption=content)
    if call.data == "get_all_keys":
        get_keys(call.message)
    if call.data == "get_feedback_message":
        feed(call.message)
    if call.data == "generate_keys":
        bot.delete_message(call.message.chat.id, sent_message.message_id)
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        # Создаем кнопки
        button1 = types.InlineKeyboardButton(text=" Так ", callback_data="btn-yes_delete")
        button2 = types.InlineKeyboardButton(text="Назад", callback_data='btn-back_delete')
        # Добавляем кнопки на клавиатуру
        keyboard.add(button1, button2)
        # Отправляем сообщение с кнопками в самом сообщении
        sent_message = bot.send_message(call.message.chat.id,"Вы уверенны?",reply_markup=keyboard)
    if call.data == "delete_all_feedback":
        bot.delete_message(call.message.chat.id, sent_message.message_id)
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        # Создаем кнопки
        button1 = types.InlineKeyboardButton(text=" Так ", callback_data="btn-yes_delete_feed")
        button2 = types.InlineKeyboardButton(text="Назад", callback_data='btn-back_delete_feed')
        # Добавляем кнопки на клавиатуру
        keyboard.add(button1, button2)
        # Отправляем сообщение с кнопками в самом сообщении
        sent_message = bot.send_message(call.message.chat.id,"Вы уверенны?",reply_markup=keyboard)
    if call.data == "btn-yes_delete_feed":
        bot.delete_message(call.message.chat.id, sent_message.message_id)
    if call.data == "btn-back_delete_feed":
        bot.delete_message(call.message.chat.id, sent_message.message_id)
    if call.data == "btn-yes_delete":
        generate_keys(call.message)
    if call.data == "btn-back_delete":
        bot.delete_message(call.message.chat.id,sent_message.message_id)
    if call.data == "btn-backAdmin":
        bot.delete_message(call.message.chat.id,sent_message.message_id)
    if call.data == "btn-back":
        bot.delete_message(call.message.chat.id,sent_message.message_id)
        keyboard = types.InlineKeyboardMarkup(row_width=1)
# Создаем кнопки
        button1 = types.InlineKeyboardButton(text="📝 МОВИ ТА ЛІТЕРАТУРИ 📚", callback_data="btn-movu")
        button2 = types.InlineKeyboardButton(text="🗺️ ПРИРОДНИЧІ НАУКИ 🔬", callback_data="btn-prirod")
        button3 = types.InlineKeyboardButton(text="🪪 СУСПІЛЬНІ НАУКИ ⚖", callback_data="btn-movu")
        button4 = types.InlineKeyboardButton(text="🗿 ІСТОРИЧНІ НАУКИ 🏛", callback_data="btn-movu")
        button5 = types.InlineKeyboardButton(text="📐 МАТЕМАТИКА 📈", callback_data="btn-movu")
# Добавляем кнопки на клавиатуру
        keyboard.add(button1, button2, button3, button4, button5)
# Отправляем сообщение с кнопками в самом сообщении
        f = open("chooseBooks.jpg", 'rb')
        sent_message = bot.send_photo(call.message.chat.id, f ,reply_markup=keyboard)
    if call.data == "btn-pon":
        bot.delete_message(call.message.chat.id, sent_message.message_id)

    if call.data == "btn-backCon":
        bot.delete_message(call.message.chat.id, sent_message.message_id)

    if call.data == "btn-backClass":
        bot.delete_message(call.message.chat.id, sent_message.message_id)

    if call.data == "btn-backHum":
        bot.delete_message(call.message.chat.id, sent_message.message_id)


    if call.data == "btn-pon":
        def switch_casep(cls):
            if cls == "11b":
                with open('rozkladp/11b.txt', 'r', encoding='utf-8') as file:
                    content = file.read()
                bot.send_message(call.message.chat.id,content)
            elif cls == "11a":
                with open('rozkladp/11a.txt', 'r', encoding='utf-8') as file:
                    content = file.read()
                bot.send_message(call.message.chat.id,content)
            elif cls == "10a":
                with open('rozkladp/10a.txt', 'r', encoding='utf-8') as file:
                    content = file.read()
                bot.send_message(call.message.chat.id,content)
            elif cls == "10b":
                with open('rozkladp/10b.txt', 'r', encoding='utf-8') as file:
                    content = file.read()
                bot.send_message(call.message.chat.id,content)
            elif cls == "9a":
                with open('rozkladp/9a.txt', 'r', encoding='utf-8') as file:
                    content = file.read()
                bot.send_message(call.message.chat.id,content)
            elif cls == "9b":
                with open('rozkladp/9b.txt', 'r', encoding='utf-8') as file:
                    content = file.read()
                bot.send_message(call.message.chat.id,content)
            elif cls == "8a":
                with open('rozkladp/8a.txt', 'r', encoding='utf-8') as file:
                    content = file.read()
                bot.send_message(call.message.chat.id,content)
            elif cls == "8b":
                with open('rozkladp/8b.txt', 'r', encoding='utf-8') as file:
                    content = file.read()
                bot.send_message(call.message.chat.id,content)
            elif cls == "7a":
                with open('rozkladp/7a.txt', 'r', encoding='utf-8') as file:
                    content = file.read()
                bot.send_message(call.message.chat.id,content)
            elif cls == "7b":
                with open('rozkladp/7b.txt', 'r', encoding='utf-8') as file:
                    content = file.read()
                bot.send_message(call.message.chat.id,content)
            elif cls == "6a":
                with open('rozkladp/6a.txt', 'r', encoding='utf-8') as file:
                    content = file.read()
                bot.send_message(call.message.chat.id,content)
            elif cls == "6b":
                with open('rozkladp/6b.txt', 'r', encoding='utf-8') as file:
                    content = file.read()
                bot.send_message(call.message.chat.id,content)
            elif cls == "5a":
                with open('rozkladp/5a.txt', 'r', encoding='utf-8') as file:
                    content = file.read()
                bot.send_message(call.message.chat.id,content)
            elif cls == "5b":
                with open('rozkladp/5b.txt', 'r', encoding='utf-8') as file:
                    content = file.read()
                bot.send_message(call.message.chat.id,content)
        switch_casep(db.reference("/users").child(str(call.message.chat.id)).get())

    if call.data == "btn-viv":
        def switch_casep(cls):
            if cls == "11b":
                with open('rozkladv/11b.txt', 'r', encoding='utf-8') as file:
                    content = file.read()
                bot.send_message(call.message.chat.id,content)
            elif cls == "11a":
                with open('rozkladv/11a.txt', 'r', encoding='utf-8') as file:
                    content = file.read()
                bot.send_message(call.message.chat.id,content)
            elif cls == "10a":
                with open('rozkladv/10a.txt', 'r', encoding='utf-8') as file:
                    content = file.read()
                bot.send_message(call.message.chat.id,content)
            elif cls == "10b":
                with open('rozkladv/10b.txt', 'r', encoding='utf-8') as file:
                    content = file.read()
                bot.send_message(call.message.chat.id,content)
            elif cls == "9a":
                with open('rozkladv/9a.txt', 'r', encoding='utf-8') as file:
                    content = file.read()
                bot.send_message(call.message.chat.id,content)
            elif cls == "9b":
                with open('rozkladv/9b.txt', 'r', encoding='utf-8') as file:
                    content = file.read()
                bot.send_message(call.message.chat.id,content)
            elif cls == "8a":
                with open('rozkladv/8a.txt', 'r', encoding='utf-8') as file:
                    content = file.read()
                bot.send_message(call.message.chat.id,content)
            elif cls == "8b":
                with open('rozkladv/8b.txt', 'r', encoding='utf-8') as file:
                    content = file.read()
                bot.send_message(call.message.chat.id,content)
            elif cls == "7a":
                with open('rozkladv/7a.txt', 'r', encoding='utf-8') as file:
                    content = file.read()
                bot.send_message(call.message.chat.id,content)
            elif cls == "7b":
                with open('rozkladv/7b.txt', 'r', encoding='utf-8') as file:
                    content = file.read()
                bot.send_message(call.message.chat.id,content)
            elif cls == "6a":
                with open('rozkladv/6a.txt', 'r', encoding='utf-8') as file:
                    content = file.read()
                bot.send_message(call.message.chat.id,content)
            elif cls == "6b":
                with open('rozkladv/6b.txt', 'r', encoding='utf-8') as file:
                    content = file.read()
                bot.send_message(call.message.chat.id,content)
            elif cls == "5a":
                with open('rozkladv/5a.txt', 'r', encoding='utf-8') as file:
                    content = file.read()
                bot.send_message(call.message.chat.id,content)
            elif cls == "5b":
                with open('rozkladv/5b.txt', 'r', encoding='utf-8') as file:
                    content = file.read()
                bot.send_message(call.message.chat.id,content)
        switch_casep(db.reference("/users").child(str(call.message.chat.id)).get())

    if call.data == "btn-ser":
        def switch_casep(cls):
            if cls == "11b":
                with open('rozklads/11b.txt', 'r', encoding='utf-8') as file:
                    content = file.read()
                bot.send_message(call.message.chat.id,content)
            elif cls == "11a":
                with open('rozklads/11a.txt', 'r', encoding='utf-8') as file:
                    content = file.read()
                bot.send_message(call.message.chat.id,content)
            elif cls == "10a":
                with open('rozklads/10a.txt', 'r', encoding='utf-8') as file:
                    content = file.read()
                bot.send_message(call.message.chat.id,content)
            elif cls == "10b":
                with open('rozklads/10b.txt', 'r', encoding='utf-8') as file:
                    content = file.read()
                bot.send_message(call.message.chat.id,content)
            elif cls == "9a":
                with open('rozklads/9a.txt', 'r', encoding='utf-8') as file:
                    content = file.read()
                bot.send_message(call.message.chat.id,content)
            elif cls == "9b":
                with open('rozklads/9b.txt', 'r', encoding='utf-8') as file:
                    content = file.read()
                bot.send_message(call.message.chat.id,content)
            elif cls == "8a":
                with open('rozklads/8a.txt', 'r', encoding='utf-8') as file:
                    content = file.read()
                bot.send_message(call.message.chat.id,content)
            elif cls == "8b":
                with open('rozklads/8b.txt', 'r', encoding='utf-8') as file:
                    content = file.read()
                bot.send_message(call.message.chat.id,content)
            elif cls == "7a":
                with open('rozklads/7a.txt', 'r', encoding='utf-8') as file:
                    content = file.read()
                bot.send_message(call.message.chat.id,content)
            elif cls == "7b":
                with open('rozklads/7b.txt', 'r', encoding='utf-8') as file:
                    content = file.read()
                bot.send_message(call.message.chat.id,content)
            elif cls == "6a":
                with open('rozklads/6a.txt', 'r', encoding='utf-8') as file:
                    content = file.read()
                bot.send_message(call.message.chat.id,content)
            elif cls == "6b":
                with open('rozklads/6b.txt', 'r', encoding='utf-8') as file:
                    content = file.read()
                bot.send_message(call.message.chat.id,content)
            elif cls == "5a":
                with open('rozklads/5a.txt', 'r', encoding='utf-8') as file:
                    content = file.read()
                bot.send_message(call.message.chat.id,content)
            elif cls == "5b":
                with open('rozklads/5b.txt', 'r', encoding='utf-8') as file:
                    content = file.read()
                bot.send_message(call.message.chat.id,content)
        switch_casep(db.reference("/users").child(str(call.message.chat.id)).get())

    if call.data == "btn-chet":
        def switch_casep(cls):
            if cls == "11b":
                with open('rozkladc/11b.txt', 'r', encoding='utf-8') as file:
                    content = file.read()
                bot.send_message(call.message.chat.id,content)
            elif cls == "11a":
                with open('rozkladc/11a.txt', 'r', encoding='utf-8') as file:
                    content = file.read()
                bot.send_message(call.message.chat.id,content)
            elif cls == "10a":
                with open('rozkladc/10a.txt', 'r', encoding='utf-8') as file:
                    content = file.read()
                bot.send_message(call.message.chat.id,content)
            elif cls == "10b":
                with open('rozkladc/10b.txt', 'r', encoding='utf-8') as file:
                    content = file.read()
                bot.send_message(call.message.chat.id,content)
            elif cls == "9a":
                with open('rozkladc/9a.txt', 'r', encoding='utf-8') as file:
                    content = file.read()
                bot.send_message(call.message.chat.id,content)
            elif cls == "9b":
                with open('rozkladc/9b.txt', 'r', encoding='utf-8') as file:
                    content = file.read()
                bot.send_message(call.message.chat.id,content)
            elif cls == "8a":
                with open('rozkladc/8a.txt', 'r', encoding='utf-8') as file:
                    content = file.read()
                bot.send_message(call.message.chat.id,content)
            elif cls == "8b":
                with open('rozkladc/8b.txt', 'r', encoding='utf-8') as file:
                    content = file.read()
                bot.send_message(call.message.chat.id,content)
            elif cls == "7a":
                with open('rozkladc/7a.txt', 'r', encoding='utf-8') as file:
                    content = file.read()
                bot.send_message(call.message.chat.id,content)
            elif cls == "7b":
                with open('rozkladc/7b.txt', 'r', encoding='utf-8') as file:
                    content = file.read()
                bot.send_message(call.message.chat.id,content)
            elif cls == "6a":
                with open('rozkladc/6a.txt', 'r', encoding='utf-8') as file:
                    content = file.read()
                bot.send_message(call.message.chat.id,content)
            elif cls == "6b":
                with open('rozkladc/6b.txt', 'r', encoding='utf-8') as file:
                    content = file.read()
                bot.send_message(call.message.chat.id,content)
            elif cls == "5a":
                with open('rozkladc/5a.txt', 'r', encoding='utf-8') as file:
                    content = file.read()
                bot.send_message(call.message.chat.id,content)
            elif cls == "5b":
                with open('rozkladc/5b.txt', 'r', encoding='utf-8') as file:
                    content = file.read()
                bot.send_message(call.message.chat.id,content)
        switch_casep(db.reference("/users").child(str(call.message.chat.id)).get())

    if call.data == "btn-piat":
        def switch_casep(cls):
            if cls == "11b":
                with open('rozkladpt/11b.txt', 'r', encoding='utf-8') as file:
                    content = file.read()
                bot.send_message(call.message.chat.id,content)
            elif cls == "11a":
                with open('rozkladpt/11a.txt', 'r', encoding='utf-8') as file:
                    content = file.read()
                bot.send_message(call.message.chat.id,content)
            elif cls == "10a":
                with open('rozkladpt/10a.txt', 'r', encoding='utf-8') as file:
                    content = file.read()
                bot.send_message(call.message.chat.id,content)
            elif cls == "10b":
                with open('rozkladpt/10b.txt', 'r', encoding='utf-8') as file:
                    content = file.read()
                bot.send_message(call.message.chat.id,content)
            elif cls == "9a":
                with open('rozkladpt/9a.txt', 'r', encoding='utf-8') as file:
                    content = file.read()
                bot.send_message(call.message.chat.id,content)
            elif cls == "9b":
                with open('rozkladpt/9b.txt', 'r', encoding='utf-8') as file:
                    content = file.read()
                bot.send_message(call.message.chat.id,content)
            elif cls == "8a":
                with open('rozkladpt/8a.txt', 'r', encoding='utf-8') as file:
                    content = file.read()
                bot.send_message(call.message.chat.id,content)
            elif cls == "8b":
                with open('rozkladpt/8b.txt', 'r', encoding='utf-8') as file:
                    content = file.read()
                bot.send_message(call.message.chat.id,content)
            elif cls == "7a":
                with open('rozkladpt/7a.txt', 'r', encoding='utf-8') as file:
                    content = file.read()
                bot.send_message(call.message.chat.id,content)
            elif cls == "7b":
                with open('rozkladpt/7b.txt', 'r', encoding='utf-8') as file:
                    content = file.read()
                bot.send_message(call.message.chat.id,content)
            elif cls == "6a":
                with open('rozkladpt/6a.txt', 'r', encoding='utf-8') as file:
                    content = file.read()
                bot.send_message(call.message.chat.id,content)
            elif cls == "6b":
                with open('rozkladpt/6b.txt', 'r', encoding='utf-8') as file:
                    content = file.read()
                bot.send_message(call.message.chat.id,content)
            elif cls == "5a":
                with open('rozkladpt/5a.txt', 'r', encoding='utf-8') as file:
                    content = file.read()
                bot.send_message(call.message.chat.id,content)
            elif cls == "5b":
                with open('rozkladpt/5b.txt', 'r', encoding='utf-8') as file:
                    content = file.read()
                bot.send_message(call.message.chat.id,content)
        switch_casep(db.reference("/users").child(str(call.message.chat.id)).get())

    if call.data == "btn-Cpon":
        # Отправляем пользователю запрос на ввод текста
        bot.send_message(call.message.chat.id, "Введіть розклад на понеділок для " + str(db.reference("/users").child(str(call.message.chat.id)).get()))
        # Сохраняем данные о последней нажатой кнопке для последующей обработки
        bot.register_next_step_handler(call.message, save_textp, call.data)
    if call.data == "btn-Cviv":
        # Отправляем пользователю запрос на ввод текста
        bot.send_message(call.message.chat.id, "Введіть розклад на вівторок для " + str(db.reference("/users").child(str(call.message.chat.id)).get()))
        # Сохраняем данные о последней нажатой кнопке для последующей обработки
        bot.register_next_step_handler(call.message, save_textcv, call.data)
    if call.data == "btn-Cser":
        # Отправляем пользователю запрос на ввод текста
        bot.send_message(call.message.chat.id, "Введіть розклад на середу для " + str(db.reference("/users").child(str(call.message.chat.id)).get()))
        # Сохраняем данные о последней нажатой кнопке для последующей обработки
        bot.register_next_step_handler(call.message, save_textcs, call.data)
    if call.data == "btn-Cchet":
        # Отправляем пользователю запрос на ввод текста
        bot.send_message(call.message.chat.id, "Введіть розклад на четвер для " + str(db.reference("/users").child(str(call.message.chat.id)).get()))
        # Сохраняем данные о последней нажатой кнопке для последующей обработки
        bot.register_next_step_handler(call.message, save_textcc, call.data)
    if call.data == "btn-Cpiat":
        # Отправляем пользователю запрос на ввод текста
        bot.send_message(call.message.chat.id, "Введіть розклад на п'ятницю для " + str(db.reference("/users").child(str(call.message.chat.id)).get()))
        # Сохраняем данные о последней нажатой кнопке для последующей обработки
        bot.register_next_step_handler(call.message, save_textcp, call.data)



def save_textp(message, button_data):
    def switch_boxp(cls):
        if cls == "11b":
            with open("rozkladp/11b.txt", "w", encoding="utf-8") as file:
                file.write(f"{message.text}\n")
            bot.send_message(message.chat.id, "Текст успешно сохранен.")
        elif cls == "11a":
            with open("rozkladp/11a.txt", "w", encoding="utf-8") as file:
                file.write(f"{message.text}\n")
            bot.send_message(message.chat.id, "Текст успешно сохранен.")
        elif cls == "10a":
            with open("rozkladp/10a.txt", "w", encoding="utf-8") as file:
                file.write(f"{message.text}\n")
            bot.send_message(message.chat.id, "Текст успешно сохранен.")
        elif cls == "10b":
            with open("rozkladp/10b.txt", "w", encoding="utf-8") as file:
                file.write(f"{message.text}\n")
            bot.send_message(message.chat.id, "Текст успешно сохранен.")
        elif cls == "9a":
            with open("rozkladp/9a.txt", "w", encoding="utf-8") as file:
                file.write(f"{message.text}\n")
            bot.send_message(message.chat.id, "Текст успешно сохранен.")
        elif cls == "9b":
            with open("rozkladp/9b.txt", "w", encoding="utf-8") as file:
                file.write(f"{message.text}\n")
            bot.send_message(message.chat.id, "Текст успешно сохранен.")
        elif cls == "8a":
            with open("rozkladp/8a.txt", "w", encoding="utf-8") as file:
                file.write(f"{message.text}\n")
            bot.send_message(message.chat.id, "Текст успешно сохранен.")
        elif cls == "8b":
            with open("rozkladp/8b.txt", "w", encoding="utf-8") as file:
                file.write(f"{message.text}\n")
            bot.send_message(message.chat.id, "Текст успешно сохранен.")
        elif cls == "7a":
            with open("rozkladp/7a.txt", "w", encoding="utf-8") as file:
                file.write(f"{message.text}\n")
            bot.send_message(message.chat.id, "Текст успешно сохранен.")
        elif cls == "7b":
            with open("rozkladp/7b.txt", "w", encoding="utf-8") as file:
                file.write(f"{message.text}\n")
            bot.send_message(message.chat.id, "Текст успешно сохранен.")
        elif cls == "6a":
            with open("rozkladp/6a.txt", "w", encoding="utf-8") as file:
                file.write(f"{message.text}\n")
            bot.send_message(message.chat.id, "Текст успешно сохранен.")
        elif cls == "6b":
            with open("rozkladp/6b.txt", "w", encoding="utf-8") as file:
                file.write(f"{message.text}\n")
            bot.send_message(message.chat.id, "Текст успешно сохранен.")
        elif cls == "5a":
            with open("rozkladp/5a.txt", "w", encoding="utf-8") as file:
                file.write(f"{message.text}\n")
            bot.send_message(message.chat.id, "Текст успешно сохранен.")
        elif cls == "5b":
            with open("rozkladp/5b.txt", "w", encoding="utf-8") as file:
                file.write(f"{message.text}\n")
            bot.send_message(message.chat.id, "Текст успешно сохранен.")
    cls = db.reference("/users").child(str(message.chat.id)).get()
    switch_boxp(cls)
def save_textcv(message, button_data):
    def switch_boxp(cls):
        if cls == "11b":
            with open("rozkladv/11b.txt", "w", encoding="utf-8") as file:
                file.write(f"{message.text}\n")
            bot.send_message(message.chat.id, "Текст успешно сохранен.")
        elif cls == "11a":
            with open("rozkladv/11a.txt", "w", encoding="utf-8") as file:
                file.write(f"{message.text}\n")
            bot.send_message(message.chat.id, "Текст успешно сохранен.")
        elif cls == "10a":
            with open("rozkladv/10a.txt", "w", encoding="utf-8") as file:
                file.write(f"{message.text}\n")
            bot.send_message(message.chat.id, "Текст успешно сохранен.")
        elif cls == "10b":
            with open("rozkladv/10b.txt", "w", encoding="utf-8") as file:
                file.write(f"{message.text}\n")
            bot.send_message(message.chat.id, "Текст успешно сохранен.")
        elif cls == "9a":
            with open("rozkladv/9a.txt", "w", encoding="utf-8") as file:
                file.write(f"{message.text}\n")
            bot.send_message(message.chat.id, "Текст успешно сохранен.")
        elif cls == "9b":
            with open("rozkladv/9b.txt", "w", encoding="utf-8") as file:
                file.write(f"{message.text}\n")
            bot.send_message(message.chat.id, "Текст успешно сохранен.")
        elif cls == "8a":
            with open("rozkladv/8a.txt", "w", encoding="utf-8") as file:
                file.write(f"{message.text}\n")
            bot.send_message(message.chat.id, "Текст успешно сохранен.")
        elif cls == "8b":
            with open("rozkladv/8b.txt", "w", encoding="utf-8") as file:
                file.write(f"{message.text}\n")
            bot.send_message(message.chat.id, "Текст успешно сохранен.")
        elif cls == "7a":
            with open("rozkladv/7a.txt", "w", encoding="utf-8") as file:
                file.write(f"{message.text}\n")
            bot.send_message(message.chat.id, "Текст успешно сохранен.")
        elif cls == "7b":
            with open("rozkladv/7b.txt", "w", encoding="utf-8") as file:
                file.write(f"{message.text}\n")
            bot.send_message(message.chat.id, "Текст успешно сохранен.")
        elif cls == "6a":
            with open("rozkladv/6a.txt", "w", encoding="utf-8") as file:
                file.write(f"{message.text}\n")
            bot.send_message(message.chat.id, "Текст успешно сохранен.")
        elif cls == "6b":
            with open("rozkladv/6b.txt", "w", encoding="utf-8") as file:
                file.write(f"{message.text}\n")
            bot.send_message(message.chat.id, "Текст успешно сохранен.")
        elif cls == "5a":
            with open("rozkladv/5a.txt", "w", encoding="utf-8") as file:
                file.write(f"{message.text}\n")
            bot.send_message(message.chat.id, "Текст успешно сохранен.")
        elif cls == "5b":
            with open("rozkladv/5b.txt", "w", encoding="utf-8") as file:
                file.write(f"{message.text}\n")
            bot.send_message(message.chat.id, "Текст успешно сохранен.")
    cls = db.reference("/users").child(str(message.chat.id)).get()
    switch_boxp(cls)
def save_textcs(message, button_data):
    def switch_boxp(cls):
        if cls == "11b":
            with open("rozklads/11b.txt", "w", encoding="utf-8") as file:
                file.write(f"{message.text}\n")
            bot.send_message(message.chat.id, "Текст успешно сохранен.")
        elif cls == "11a":
            with open("rozklads/11a.txt", "w", encoding="utf-8") as file:
                file.write(f"{message.text}\n")
            bot.send_message(message.chat.id, "Текст успешно сохранен.")
        elif cls == "10a":
            with open("rozklads/10a.txt", "w", encoding="utf-8") as file:
                file.write(f"{message.text}\n")
            bot.send_message(message.chat.id, "Текст успешно сохранен.")
        elif cls == "10b":
            with open("rozklads/10b.txt", "w", encoding="utf-8") as file:
                file.write(f"{message.text}\n")
            bot.send_message(message.chat.id, "Текст успешно сохранен.")
        elif cls == "9a":
            with open("rozklads/9a.txt", "w", encoding="utf-8") as file:
                file.write(f"{message.text}\n")
            bot.send_message(message.chat.id, "Текст успешно сохранен.")
        elif cls == "9b":
            with open("rozklads/9b.txt", "w", encoding="utf-8") as file:
                file.write(f"{message.text}\n")
            bot.send_message(message.chat.id, "Текст успешно сохранен.")
        elif cls == "8a":
            with open("rozklads/8a.txt", "w", encoding="utf-8") as file:
                file.write(f"{message.text}\n")
            bot.send_message(message.chat.id, "Текст успешно сохранен.")
        elif cls == "8b":
            with open("rozklads/8b.txt", "w", encoding="utf-8") as file:
                file.write(f"{message.text}\n")
            bot.send_message(message.chat.id, "Текст успешно сохранен.")
        elif cls == "7a":
            with open("rozklads/7a.txt", "w", encoding="utf-8") as file:
                file.write(f"{message.text}\n")
            bot.send_message(message.chat.id, "Текст успешно сохранен.")
        elif cls == "7b":
            with open("rozklads/7b.txt", "w", encoding="utf-8") as file:
                file.write(f"{message.text}\n")
            bot.send_message(message.chat.id, "Текст успешно сохранен.")
        elif cls == "6a":
            with open("rozklads/6a.txt", "w", encoding="utf-8") as file:
                file.write(f"{message.text}\n")
            bot.send_message(message.chat.id, "Текст успешно сохранен.")
        elif cls == "6b":
            with open("rozklads/6b.txt", "w", encoding="utf-8") as file:
                file.write(f"{message.text}\n")
            bot.send_message(message.chat.id, "Текст успешно сохранен.")
        elif cls == "5a":
            with open("rozklads/5a.txt", "w", encoding="utf-8") as file:
                file.write(f"{message.text}\n")
            bot.send_message(message.chat.id, "Текст успешно сохранен.")
        elif cls == "5b":
            with open("rozklads/5b.txt", "w", encoding="utf-8") as file:
                file.write(f"{message.text}\n")
            bot.send_message(message.chat.id, "Текст успешно сохранен.")
    cls = db.reference("/users").child(str(message.chat.id)).get()
    switch_boxp(cls)
def save_textcc(message, button_data):
    def switch_boxp(cls):
        if cls == "11b":
            with open("rozkladc/11b.txt", "w", encoding="utf-8") as file:
                file.write(f"{message.text}\n")
            bot.send_message(message.chat.id, "Текст успешно сохранен.")
        elif cls == "11a":
            with open("rozkladc/11a.txt", "w", encoding="utf-8") as file:
                file.write(f"{message.text}\n")
            bot.send_message(message.chat.id, "Текст успешно сохранен.")
        elif cls == "10a":
            with open("rozkladc/10a.txt", "w", encoding="utf-8") as file:
                file.write(f"{message.text}\n")
            bot.send_message(message.chat.id, "Текст успешно сохранен.")
        elif cls == "10b":
            with open("rozkladc/10b.txt", "w", encoding="utf-8") as file:
                file.write(f"{message.text}\n")
            bot.send_message(message.chat.id, "Текст успешно сохранен.")
        elif cls == "9a":
            with open("rozkladc/9a.txt", "w", encoding="utf-8") as file:
                file.write(f"{message.text}\n")
            bot.send_message(message.chat.id, "Текст успешно сохранен.")
        elif cls == "9b":
            with open("rozkladc/9b.txt", "w", encoding="utf-8") as file:
                file.write(f"{message.text}\n")
            bot.send_message(message.chat.id, "Текст успешно сохранен.")
        elif cls == "8a":
            with open("rozkladc/8a.txt", "w", encoding="utf-8") as file:
                file.write(f"{message.text}\n")
            bot.send_message(message.chat.id, "Текст успешно сохранен.")
        elif cls == "8b":
            with open("rozkladc/8b.txt", "w", encoding="utf-8") as file:
                file.write(f"{message.text}\n")
            bot.send_message(message.chat.id, "Текст успешно сохранен.")
        elif cls == "7a":
            with open("rozkladc/7a.txt", "w", encoding="utf-8") as file:
                file.write(f"{message.text}\n")
            bot.send_message(message.chat.id, "Текст успешно сохранен.")
        elif cls == "7b":
            with open("rozkladc/7b.txt", "w", encoding="utf-8") as file:
                file.write(f"{message.text}\n")
            bot.send_message(message.chat.id, "Текст успешно сохранен.")
        elif cls == "6a":
            with open("rozkladc/6a.txt", "w", encoding="utf-8") as file:
                file.write(f"{message.text}\n")
            bot.send_message(message.chat.id, "Текст успешно сохранен.")
        elif cls == "6b":
            with open("rozkladc/6b.txt", "w", encoding="utf-8") as file:
                file.write(f"{message.text}\n")
            bot.send_message(message.chat.id, "Текст успешно сохранен.")
        elif cls == "5a":
            with open("rozkladc/5a.txt", "w", encoding="utf-8") as file:
                file.write(f"{message.text}\n")
            bot.send_message(message.chat.id, "Текст успешно сохранен.")
        elif cls == "5b":
            with open("rozkladc/5b.txt", "w", encoding="utf-8") as file:
                file.write(f"{message.text}\n")
            bot.send_message(message.chat.id, "Текст успешно сохранен.")
    cls = db.reference("/users").child(str(message.chat.id)).get()
    switch_boxp(cls)
def save_textcp(message, button_data):
    def switch_boxp(cls):
        if cls == "11b":
            with open("rozkladpt/11b.txt", "w", encoding="utf-8") as file:
                file.write(f"{message.text}\n")
            bot.send_message(message.chat.id, "Текст успешно сохранен.")
        elif cls == "11a":
            with open("rozkladpt/11a.txt", "w", encoding="utf-8") as file:
                file.write(f"{message.text}\n")
            bot.send_message(message.chat.id, "Текст успешно сохранен.")
        elif cls == "10a":
            with open("rozkladpt/10a.txt", "w", encoding="utf-8") as file:
                file.write(f"{message.text}\n")
            bot.send_message(message.chat.id, "Текст успешно сохранен.")
        elif cls == "10b":
            with open("rozkladpt/10b.txt", "w", encoding="utf-8") as file:
                file.write(f"{message.text}\n")
            bot.send_message(message.chat.id, "Текст успешно сохранен.")
        elif cls == "9a":
            with open("rozkladpt/9a.txt", "w", encoding="utf-8") as file:
                file.write(f"{message.text}\n")
            bot.send_message(message.chat.id, "Текст успешно сохранен.")
        elif cls == "9b":
            with open("rozkladpt/9b.txt", "w", encoding="utf-8") as file:
                file.write(f"{message.text}\n")
            bot.send_message(message.chat.id, "Текст успешно сохранен.")
        elif cls == "8a":
            with open("rozkladpt/8a.txt", "w", encoding="utf-8") as file:
                file.write(f"{message.text}\n")
            bot.send_message(message.chat.id, "Текст успешно сохранен.")
        elif cls == "8b":
            with open("rozkladpt/8b.txt", "w", encoding="utf-8") as file:
                file.write(f"{message.text}\n")
            bot.send_message(message.chat.id, "Текст успешно сохранен.")
        elif cls == "7a":
            with open("rozkladpt/7a.txt", "w", encoding="utf-8") as file:
                file.write(f"{message.text}\n")
            bot.send_message(message.chat.id, "Текст успешно сохранен.")
        elif cls == "7b":
            with open("rozkladpt/7b.txt", "w", encoding="utf-8") as file:
                file.write(f"{message.text}\n")
            bot.send_message(message.chat.id, "Текст успешно сохранен.")
        elif cls == "6a":
            with open("rozkladpt/6a.txt", "w", encoding="utf-8") as file:
                file.write(f"{message.text}\n")
            bot.send_message(message.chat.id, "Текст успешно сохранен.")
        elif cls == "6b":
            with open("rozkladpt/6b.txt", "w", encoding="utf-8") as file:
                file.write(f"{message.text}\n")
            bot.send_message(message.chat.id, "Текст успешно сохранен.")
        elif cls == "5a":
            with open("rozkladpt/5a.txt", "w", encoding="utf-8") as file:
                file.write(f"{message.text}\n")
            bot.send_message(message.chat.id, "Текст успешно сохранен.")
        elif cls == "5b":
            with open("rozkladpt/5b.txt", "w", encoding="utf-8") as file:
                file.write(f"{message.text}\n")
            bot.send_message(message.chat.id, "Текст успешно сохранен.")
    cls = db.reference("/users").child(str(message.chat.id)).get()
    switch_boxp(cls)


@bot.message_handler(func=lambda message: message.text == "Назад")
def send_menu(message):
    # Создаем кнопочное меню
    markup = types.ReplyKeyboardMarkup(row_width=2)
    item1 = types.KeyboardButton("📚 ПІДРУЧНИКИ 📚")
    item2 = types.KeyboardButton("📨 КОНТАКТИ 📨")
    item3 = types.KeyboardButton("📆 РОЗКЛАД 📆")
    item4 = types.KeyboardButton("👩‍🏫 CLASSROOM 👩‍🏫")
    item5 = types.KeyboardButton("👤 HUMAN 👤")
    item6 = types.KeyboardButton("🛠️ ФУНКЦІЇ БОТА 🛠️")
    item7 = types.KeyboardButton("ЗВОРОТНІЙ ЗВ'ЯЗОК")
    markup.add(item1, item2, item3,item4,item5,item6,item7)

    # Отправляем сообщение с кнопочным меню
    bot.send_message(message.chat.id, "Выберите опцию:", reply_markup=markup)

def get_keys(message):
    bot.send_message(message.chat.id,
                     "11A - " + str(db.reference("/keys/11a").get()) +"\n11B - " + str(db.reference("/keys/11b").get()) + "\n10A - " +str(db.reference("/keys/10a").get())
                     + "\n10B - " +str(db.reference("/keys/10b").get()) + "\n9A - " +str(db.reference("/keys/9a").get())+ "\n9B - " +str(db.reference("/keys/9b").get())
                     + "\n8A - " +str(db.reference("/keys/8a").get())+ "\n8B - " +str(db.reference("/keys/8b").get())+ "\n7A - " +str(db.reference("/keys/7a").get())
                     + "\n6B - " +str(db.reference("/keys/6b").get())+ "\n5A - " +str(db.reference("/keys/5a").get())+ "\n5B - " +str(db.reference("/keys/5b").get())
                     )

@bot.message_handler(commands=['adminPanel'])
def adminPanel(message):
    admins_ref = db.reference('/admins')

    # Получение данных из узла "admins"
    admins_data = admins_ref.get()

    # Проверка наличия записи с названием "3123"
    if admins_data is not None and str(message.chat.id) in admins_data:
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        # Создаем кнопки
        button1 = types.InlineKeyboardButton(text=" Отримати ключі доступу ", callback_data="get_all_keys")
        button2 = types.InlineKeyboardButton(text=" Згенерувати нові ключі доступу ", callback_data="generate_keys")
        button3 = types.InlineKeyboardButton(text=" Отримати feedback ", callback_data="get_feedback_message")
        button4 = types.InlineKeyboardButton(text=" Видалити повідомлення feedback(NW) ", callback_data="delete_all_feedback")
        button5 = types.InlineKeyboardButton(text=" Змінити розклад ", callback_data="change_roz")
        button6 = types.InlineKeyboardButton(text="Назад", callback_data='btn-backAdmin')
        # Добавляем кнопки на клавиатуру
        keyboard.add(button1, button2, button3, button4, button5, button6)
        # Отправляем сообщение с кнопками в самом сообщении
        global sent_message
        sent_message = bot.send_message(message.chat.id,"AdminPanel:",reply_markup=keyboard)
    else:
        print("Запись с названием '3123' не найдена в узле 'admins'.")


@bot.message_handler(commands=['cngRoz'])
def adminPanel(message):
    admins_ref = db.reference('/mlAdmins')

    # Получение данных из узла "admins"
    admins_data = admins_ref.get()

    # Проверка наличия записи с названием "3123"
    if admins_data is not None and str(message.chat.id) in admins_data:
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        # Создаем кнопки
        button1 = types.InlineKeyboardButton(text="ПОНЕДІЛОК", callback_data="btn-Cpon")
        button2 = types.InlineKeyboardButton(text="ВІВТОРОК", callback_data="btn-Cviv")
        button3 = types.InlineKeyboardButton(text="СЕРЕДА", callback_data="btn-Cser")
        button4 = types.InlineKeyboardButton(text="ЧЕТВЕР", callback_data="btn-Cchet")
        button5 = types.InlineKeyboardButton(text="П'ЯТНИЦЯ", callback_data="btn-Cpiat")
        button6 = types.InlineKeyboardButton(text="Назад", callback_data='btn-backAdmin')
        # Добавляем кнопки на клавиатуру
        keyboard.add(button1, button2, button3, button4, button5, button6)
        # Отправляем сообщение с кнопками в самом сообщении
        global sent_message
        sent_message = bot.send_message(message.chat.id,"AdminPanel:",reply_markup=keyboard)
        return
    else: return

def generate_keys(message):
    db.reference('/keys').set({
        '11a': secrets.randbelow(10**8),
        '11b': secrets.randbelow(10**8),
        '10a': secrets.randbelow(10**8),
        '10b': secrets.randbelow(10**8),
        '9a': secrets.randbelow(10**8),
        '9b': secrets.randbelow(10**8),
        '8a': secrets.randbelow(10**8),
        '8b': secrets.randbelow(10**8),
        '7a': secrets.randbelow(10**8),
        '7b': secrets.randbelow(10**8),
        '6a': secrets.randbelow(10**8),
        '6b': secrets.randbelow(10**8),
        '5a': secrets.randbelow(10**8),
        '5b': secrets.randbelow(10**8),
    })
    bot.send_message(message.chat.id, "Keys has generated!")

@bot.message_handler(commands=['generate'])
def send_menu(message):
    # Создаем кнопочное меню
    markup = types.ReplyKeyboardMarkup(row_width=2)
    item1 = types.KeyboardButton("📚 ПІДРУЧНИКИ 📚")
    item2 = types.KeyboardButton("📨 КОНТАКТИ 📨")
    item3 = types.KeyboardButton("📆 РОЗКЛАД 📆")
    item4 = types.KeyboardButton("👩‍🏫 CLASSROOM 👩‍🏫")
    item5 = types.KeyboardButton("👤 HUMAN 👤")
    item6 = types.KeyboardButton("🛠️ ФУНКЦІЇ БОТА 🛠️")
    item7 = types.KeyboardButton("ЗВОРОТНІЙ ЗВ'ЯЗОК")
    markup.add(item1, item2, item3,item4,item5,item6,item7)

    # Отправляем сообщение с кнопочным меню
    bot.send_message(message.chat.id, "Выберите опцию:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "🛠️ ФУНКЦІЇ БОТА 🛠️")
def button1(message):
    with open('text_for_BotFuncs.txt', 'r', encoding='utf-8') as file:
        lines = file.read()
        f = open('infoPic.png','rb')
        bot.send_photo(message.chat.id,f,caption=lines)

    return

@bot.message_handler(func=lambda message: message.text == "ЗВОРОТНІЙ ЗВ'ЯЗОК")
def button1(message):
    bot.send_message(message.chat.id,"Write some text: ")
    text_message = bot.register_next_step_handler(message,handle_user_response)
    return

def handle_user_response(message):
    # Здесь можно выполнить любую логику с ответом пользователя
    user_text = message.text
    print("User's response:", user_text)
    # Пример: отправить ответ пользователю
    bot.send_message(message.chat.id, "You wrote: " + user_text)
    write_data(message,user_text)

def write_data(message,user_text):
    # Ссылка на коллекцию
    collection_ref = firestore.client().collection(u'feedback')
    if message.from_user.username:
        user_username = message.from_user.username
        print(f"Ник пользователя: {user_username}")
    else:
        user_username = "None"
    # Данные для записи
    data = {
        u'Chat_Id': u''+str(message.chat.id),
        u'User_Name': u''+str(user_username),
        u'text': user_text
    }
    # Добавление данных в документ
    doc_ref = collection_ref.document(u'feedback ' + str(datetime.datetime.now()))
    doc_ref.set(data)
    print("Данные успешно записаны в коллекцию 'users'.")



def delete_all_feedback(message):
    db = firestore.Client()
    # Получение всех документов из коллекции
    docs = db.collection(u'feedback').stream()

    # Удаление каждого документа
    for doc in docs:
        doc.reference.delete()


def read_collection_and_send_messages(user):
    # Ссылка на коллекцию
    collection_ref = firestore.client().collection(u'feedback')
    # Получение всех документов из коллекции
    docs = collection_ref.get()

    # Создание текстового файла и запись данных в него
    file_content = BytesIO()
    for doc in docs:
        data = doc.to_dict()
        file_content.write(f"Данные документа:\n{data}\n".encode('utf-8'))

    # Установка позиции указателя в начало файла
    file_content.seek(0)

    # Отправка текстового документа боту
    file_content.name = 'feedback_data.txt'
    file_content.seek(0)
    bot.send_document(chat_id=user.chat.id, document=file_content)

def feed(message):
    read_collection_and_send_messages(message)
@bot.message_handler(func=lambda message: message.text == "👩‍🏫 CLASSROOM 👩‍🏫")
def button1(message):
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    # Создаем кнопки
    button1 = types.InlineKeyboardButton(text=" CLASSROOM ", url="https://classroom.google.com/")
    button2 = types.InlineKeyboardButton(text="Назад", callback_data='btn-backClass')
# Добавляем кнопки на клавиатуру
    keyboard.add(button1,button2)
# Отправляем сообщение с кнопками в самом сообщении
    f = open("classroom.png", 'rb')
    global sent_message
    sent_message = bot.send_photo(message.chat.id, f ,reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text == "👤 HUMAN 👤")
def button1(message):
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    # Создаем кнопки
    button1 = types.InlineKeyboardButton(text=" HUMAN ", url="https://id.human.ua/")
    button2 = types.InlineKeyboardButton(text="Назад", callback_data='btn-backHum')
    # Добавляем кнопки на клавиатуру
    keyboard.add(button1,button2)
    # Отправляем сообщение с кнопками в самом сообщении
    f = open("human.png", 'rb')
    global sent_message
    sent_message = bot.send_photo(message.chat.id, f ,reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text == "📨 КОНТАКТИ 📨")
def button1(message):
    if str(db.reference("/users").child(str(message.chat.id)).get()) == "11b":
        with open('cont/11b.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()
            total_lines = len(lines)
            middle_index = total_lines // 2
            first_half = ''.join(lines[:middle_index])
            second_half = ''.join(lines[middle_index:])
            full_text = first_half + '\n\n' + second_half
            f = open('kontZagal.png', 'rb')
            bot.send_photo(message.chat.id, f)
            bot.send_message(message.chat.id, full_text)
    if str(db.reference("/users").child(str(message.chat.id)).get()) == "11a":
        with open('cont/11a.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()
            total_lines = len(lines)
            middle_index = total_lines // 2
            first_half = ''.join(lines[:middle_index])
            second_half = ''.join(lines[middle_index:])
            full_text = first_half + '\n\n' + second_half
            f = open('kontZagal.png', 'rb')
            bot.send_photo(message.chat.id, f)
            bot.send_message(message.chat.id, full_text)
    if str(db.reference("/users").child(str(message.chat.id)).get()) == "10a":
        with open('cont/10a.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()
            total_lines = len(lines)
            middle_index = total_lines // 2
            first_half = ''.join(lines[:middle_index])
            second_half = ''.join(lines[middle_index:])
            full_text = first_half + '\n\n' + second_half
            f = open('kontZagal.png', 'rb')
            bot.send_photo(message.chat.id, f)
            bot.send_message(message.chat.id, full_text)
    if str(db.reference("/users").child(str(message.chat.id)).get()) == "10b":
        with open('cont/10b.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()
            total_lines = len(lines)
            middle_index = total_lines // 2
            first_half = ''.join(lines[:middle_index])
            second_half = ''.join(lines[middle_index:])
            full_text = first_half + '\n\n' + second_half
            f = open('kontZagal.png', 'rb')
            bot.send_photo(message.chat.id, f)
            bot.send_message(message.chat.id, full_text)
    if str(db.reference("/users").child(str(message.chat.id)).get()) == "9a":
        with open('cont/9a.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()
            total_lines = len(lines)
            middle_index = total_lines // 2
            first_half = ''.join(lines[:middle_index])
            second_half = ''.join(lines[middle_index:])
            full_text = first_half + '\n\n' + second_half
            f = open('kontZagal.png', 'rb')
            bot.send_photo(message.chat.id, f)
            bot.send_message(message.chat.id, full_text)
    if str(db.reference("/users").child(str(message.chat.id)).get()) == "9b":
        with open('cont/9b.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()
            total_lines = len(lines)
            middle_index = total_lines // 2
            first_half = ''.join(lines[:middle_index])
            second_half = ''.join(lines[middle_index:])
            full_text = first_half + '\n\n' + second_half
            f = open('kontZagal.png', 'rb')
            bot.send_photo(message.chat.id, f)
            bot.send_message(message.chat.id, full_text)
    if str(db.reference("/users").child(str(message.chat.id)).get()) == "8a":
        with open('cont/8a.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()
            total_lines = len(lines)
            middle_index = total_lines // 2
            first_half = ''.join(lines[:middle_index])
            second_half = ''.join(lines[middle_index:])
            full_text = first_half + '\n\n' + second_half
            f = open('kontZagal.png', 'rb')
            bot.send_photo(message.chat.id, f)
            bot.send_message(message.chat.id, full_text)
    if str(db.reference("/users").child(str(message.chat.id)).get()) == "8b":
        with open('cont/8b.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()
            total_lines = len(lines)
            middle_index = total_lines // 2
            first_half = ''.join(lines[:middle_index])
            second_half = ''.join(lines[middle_index:])
            full_text = first_half + '\n\n' + second_half
            f = open('kontZagal.png', 'rb')
            bot.send_photo(message.chat.id, f)
            bot.send_message(message.chat.id, full_text)
    if str(db.reference("/users").child(str(message.chat.id)).get()) == "7a":
        with open('cont/7a.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()
            total_lines = len(lines)
            middle_index = total_lines // 2
            first_half = ''.join(lines[:middle_index])
            second_half = ''.join(lines[middle_index:])
            full_text = first_half + '\n\n' + second_half
            f = open('kontZagal.png', 'rb')
            bot.send_photo(message.chat.id, f)
            bot.send_message(message.chat.id, full_text)
    if str(db.reference("/users").child(str(message.chat.id)).get()) == "7b":
        with open('cont/7b.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()
            total_lines = len(lines)
            middle_index = total_lines // 2
            first_half = ''.join(lines[:middle_index])
            second_half = ''.join(lines[middle_index:])
            full_text = first_half + '\n\n' + second_half
            f = open('kontZagal.png', 'rb')
            bot.send_photo(message.chat.id, f)
            bot.send_message(message.chat.id, full_text)
    if str(db.reference("/users").child(str(message.chat.id)).get()) == "6a":
        with open('cont/6a.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()
            total_lines = len(lines)
            middle_index = total_lines // 2
            first_half = ''.join(lines[:middle_index])
            second_half = ''.join(lines[middle_index:])
            full_text = first_half + '\n\n' + second_half
            f = open('kontZagal.png', 'rb')
            bot.send_photo(message.chat.id, f)
            bot.send_message(message.chat.id, full_text)
    if str(db.reference("/users").child(str(message.chat.id)).get()) == "6b":
        with open('cont/6b.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()
            total_lines = len(lines)
            middle_index = total_lines // 2
            first_half = ''.join(lines[:middle_index])
            second_half = ''.join(lines[middle_index:])
            full_text = first_half + '\n\n' + second_half
            f = open('kontZagal.png', 'rb')
            bot.send_photo(message.chat.id, f)
            bot.send_message(message.chat.id, full_text)
    if str(db.reference("/users").child(str(message.chat.id)).get()) == "5a":
        with open('cont/5a.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()
            total_lines = len(lines)
            middle_index = total_lines // 2
            first_half = ''.join(lines[:middle_index])
            second_half = ''.join(lines[middle_index:])
            full_text = first_half + '\n\n' + second_half
            f = open('kontZagal.png', 'rb')
            bot.send_photo(message.chat.id, f)
            bot.send_message(message.chat.id, full_text)
    if str(db.reference("/users").child(str(message.chat.id)).get()) == "5b":
        with open('cont/5b.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()
            total_lines = len(lines)
            middle_index = total_lines // 2
            first_half = ''.join(lines[:middle_index])
            second_half = ''.join(lines[middle_index:])
            full_text = first_half + '\n\n' + second_half
            f = open('kontZagal.png', 'rb')
            bot.send_photo(message.chat.id, f)
            bot.send_message(message.chat.id, full_text)


# Добавляем кнопки на клавиатуру

    # Добавляем кнопки на клавиатуру

@bot.message_handler(func=lambda message: message.text == "📆 РОЗКЛАД 📆")
def button1(message):
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text="ПОНЕДІЛОК",callback_data="btn-pon")
    button2 = types.InlineKeyboardButton(text="ВІВТОРОК",callback_data="btn-viv")
    button3 = types.InlineKeyboardButton(text="СЕРЕДА",callback_data="btn-ser")
    button4 = types.InlineKeyboardButton(text="ЧЕТВЕР",callback_data="btn-chet")
    button5 = types.InlineKeyboardButton(text="П'ЯТНИЦЯ",callback_data="btn-piat")
    button6 = types.InlineKeyboardButton(text="РОЗКЛАД ДЗВІНКІВ",callback_data="btn-rozklad")
    button7 = types.InlineKeyboardButton(text="Назад", callback_data="btn-backRoz")
    keyboard.add(button1, button2, button3, button4, button5, button6, button7)
    global sent_message
    f = open("chooseBooks.jpg", 'rb')
    sent_message = bot.send_photo(message.chat.id, f ,reply_markup=keyboard)
    print(sent_message.message_id)


@bot.message_handler(func=lambda message: message.text == "📚 ПІДРУЧНИКИ 📚")
def button1(message):
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    # Создаем кнопки
    button1 = types.InlineKeyboardButton(text="📝 МОВИ ТА ЛІТЕРАТУРИ 📚", callback_data="btn-movu")
    button2 = types.InlineKeyboardButton(text="🗺️ ПРИРОДНИЧІ НАУКИ 🔬", callback_data="btn-prirod")
    button3 = types.InlineKeyboardButton(text="🪪 СУСПІЛЬНІ НАУКИ ⚖", callback_data="btn-movu")
    button4 = types.InlineKeyboardButton(text="🗿 ІСТОРИЧНІ НАУКИ 🏛", callback_data="btn-movu")
    button5 = types.InlineKeyboardButton(text="📐 МАТЕМАТИКА 📈", callback_data="btn-movu")
# Добавляем кнопки на клавиатуру
    keyboard.add(button1, button2, button3, button4, button5)
# Отправляем сообщение с кнопками в самом сообщении
    global sent_message
    f = open("chooseBooks.jpg", 'rb')
    sent_message = bot.send_photo(message.chat.id, f ,reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text == "📝 МОВИ ТА ЛІТЕРАТУРИ 📚")
def button2(message):
    with open("books/mova.jpg", "rb") as photo:
        bot.send_photo(message.chat.id, photo, caption="https://drive.google.com/file/d/1hdldUZ1XhIKCnBSb66C7SKbrdoXW3osr/view?usp=drivesdk")
    with open("books/liter.jpg", "rb") as photo:
        bot.send_photo(message.chat.id, photo, caption="https://drive.google.com/file/d/1-tWF8VFdsLOdAVQI2-MauA87gtLEYafM/view?usp=drivesdk")
    with open("books/zaryb.jpg", "rb") as photo:
        bot.send_photo(message.chat.id, photo, caption="https://drive.google.com/file/d/1wOf82olgYQ4m8GLAGtfRFufuOYjJ2Ji3/view?usp=drivesdk")
    with open("books/eng.jpg", "rb") as photo:
        bot.send_photo(message.chat.id, photo, caption="https://drive.google.com/file/d/16MlY6TCpZK1JAx8tKC6NGXP_G09WFwpF/view?usp=drivesdk")

@bot.message_handler(func=lambda message: message.text == "🗺️ ПРИРОДНИЧІ НАУКИ 🔬")
def button2(message):
    with open("books/xim.jpg", "rb") as photo:
        bot.send_photo(message.chat.id, photo, caption="https://drive.google.com/file/d/1rB53rD99yK-v_Nc8_-kCnLmlue9YG36w/view?usp=drivesdk")
    with open("books/PE.jpg", "rb") as photo:
        bot.send_photo(message.chat.id, photo, caption="https://drive.google.com/file/d/10nvSZMvLV_8PUkXvr6KQ6FQPUfbt__rO/view?usp=drivesdk")
    with open("books/geo.jpg", "rb") as photo:
        bot.send_photo(message.chat.id, photo, caption="https://drive.google.com/file/d/1eO-D_FK3bfLtxiC9_f4w4VnJNSRrVCna/view?usp=drivesdk")
    with open("books/bio.jpg", "rb") as photo:
        bot.send_photo(message.chat.id, photo, caption="https://drive.google.com/file/d/1MBjTiIHOEyXLZOPr38sd0BqsKDDUQJMy/view?usp=drivesdk")
@bot.message_handler(func=lambda message: message.text == "🪪 СУСПІЛЬНІ НАУКИ ⚖")
def button2(message):
    with open("books/grom.jpg", "rb") as photo:
        bot.send_photo(message.chat.id, photo, caption="https://drive.google.com/file/d/1xjEfvMdLkMXRBdsw7GuBqp3ALsbJdA5T/view?usp=drivesdk")
    with open("books/zah.jpg", "rb") as photo:
        bot.send_photo(message.chat.id, photo, caption="https://drive.google.com/file/d/1jQlux1YcDAWuLz5lubKctKb2HjVNgaC2/view?usp=drivesdk")
    with open("books/fin.jpg", "rb") as photo:
        bot.send_photo(message.chat.id, photo, caption="https://drive.google.com/file/d/1ei5JB_vG737qwHEB6wPw-iAsTODlFrIK/view?usp=drivesdk")

@bot.message_handler(func=lambda message: message.text == "🗿 ІСТОРИЧНІ НАУКИ 🏛")
def button2(message):
    with open("books/HofU.jpg", "rb") as photo:
        bot.send_photo(message.chat.id, photo, caption="https://drive.google.com/file/d/1PrTQdEduS3u_pFxLyO1pC1N-A1-uwROS/view?usp=drivesdk")
    with open("books/HofV.jpg", "rb") as photo:
        bot.send_photo(message.chat.id, photo, caption="https://drive.google.com/file/d/1K8uvuNxmY2eQNMHQ2PVndbKlHVlGQlK1/view?usp=drivesdk")
@bot.message_handler(func=lambda message: message.text == "📐 МАТЕМАТИКА 📈")
def button2(message):
    with open("books/math.jpg", "rb") as photo:
        bot.send_photo(message.chat.id, photo, caption="https://drive.google.com/file/d/1r7Um9SD__YJISiXZXDc3dcgzBYS-ClQ7/view?usp=drivesdk")

bot.infinity_polling()