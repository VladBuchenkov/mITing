import telebot
from telebot import types
from collections import Counter
firstime = 0
lis = []
Topnumber = "Не известно"
Dont = []
numbers = []
numtime = -1
secondtime = 0
name = ''
answer = 0
votes = {}
voting_id = {}
name = False
firsttime = 0
times = ["0:00","1:00","2:00","3:00","4:00","5:00","6:00","7:00","8:00","9:00","10:00","11:00","12:00","13:00","14:00","15:00","16:00","17:00","18:00","19:00","20:00","21:00","22:00","23:00"]
time = []
##btnlist = [btn1,btn2,btn3,btn4,btn5,btn6,btn7,btn8,btn9,btn10,btn11,btn12,btn13,btn14,btn15,btn16,btn17,btn18,btn19,btn20,btn21,btn22,btn23,btn24]
token = "6884856279:AAEIYI5BMvvIh4Oq4AFAOr687zyOOisdSKY"

# подключаемся к телеграму
bot = telebot.TeleBot(token=token)

# реагируем на команды /start и /help
@bot.message_handler(commands=['start', 'help'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton("Создать опрос")
    markup.row(btn1)
    bot.send_message(message.chat.id, "Привет, это бот который может голосовать за выбор времени для встреч.", reply_markup=markup)
    bot.register_next_step_handler(message, public)
    markup.row(btn1)
def public(message):
    a = telebot.types.ReplyKeyboardRemove()
    bot.send_message(message.chat.id, "Напишите название опроса",reply_markup = a)
    bot.register_next_step_handler(message, firsttime)
def firsttime(message):
    global name
    name = message.text.strip()
    markup = types.ReplyKeyboardMarkup(row_width=5)
    buttons = [types.KeyboardButton(text=name) for name in times]
    markup.add(*buttons)

    bot.send_message(message.chat.id, "Выберите начальное время встречи", reply_markup = markup)
    bot.register_next_step_handler(message, secondttime)
def secondttime(message):
    global firstime
    for i in range(0,24):
        if message.text.lower() == times[i]:
            firstime = i
    markup = types.ReplyKeyboardMarkup(row_width=5)
    buttons = [types.KeyboardButton(text=name) for name in times]
    markup.add(*buttons)


    bot.send_message(message.chat.id, "Выберите конечное время встречи",reply_markup = markup)
    bot.register_next_step_handler(message, vote)

            
def vote(message):
    global secondtime
    a = telebot.types.ReplyKeyboardRemove()
    bot.send_message(message.chat.id, "Вы создали опрос" ,reply_markup = a)
    for i in range(0,24):
        if message.text.lower() == times[i]:
            secondtime = i
##    all_choices  = "\n".join(["{user}: смогут в {answer}" for user, choice in vote.items()])
    
    text = f'''Это голосование {name},
Время встречи с {firstime}:00 по {secondtime}:00
лучшее время для встречи {Topnumber}
Пользователи которые смогут:
    
    

    
Пользователи которые не смогут:
    
    
    
Выберите время которое удобно вам
    '''
    
    print(firstime,secondtime+1)
    for i in range(firstime, secondtime+1):
            a = times[i]
            time.append(a)
    keyboard = types.InlineKeyboardMarkup(row_width=5)
    buttons = [types.InlineKeyboardButton(text=name, callback_data=name) for name in time]
    buttons1 = types.InlineKeyboardButton(text="Я не смогу прийти на мероприятие", callback_data=-1)
    keyboard.add(*buttons)
    keyboard.add(buttons1)
    bot.send_message(message.chat.id, text,reply_markup = keyboard)

@bot.callback_query_handler(func = lambda callback: True)
def callback_message(callback):
    if callback.data:
        for i in range(len(time)):
            if callback.data == time[i]:
                numtime = i
            elif callback.data == -1:
                numtime = -1
        voting_id, answer = int(callback.message.from_user.id), int(numtime)

        votes[voting_id] = votes.get(voting_id, list()) + [{
            "user": callback.message.from_user.id,
            "answer": answer
        }]
        votecheck()
def votecheck():
    for i in votes:
        a = votes[i]
        a = a[0]
        b = a["answer"]
        if b != -1:
            numbers.append(b)
        else:
            Dont.append(a)
            print(Dont)
    counter = Counter(numbers)
    Topnumber = counter.most_common(1)[0][0] 
        


bot.polling(none_stop=True)




















