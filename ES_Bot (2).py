import telebot
from telebot import types
import random

class TelegramBot(telebot.TeleBot):
      extraversion_introversion = 0
      lies = 0
      neuro = 0
      extra_len = 0
      j = 0
      cnt = 0
      extra_intro_list = ['Мне нравится находиться в оживленной обстановке',
                          'Я не лезу за словом в карман',
                          'Я предпочитаю держаться в тени на вечеринках или в компаниях',
                          'При ссоре я предпочитаю отмолчаться, надеясь, что все обойдется',
                          'Я люблю находиться среди людей',
                          'Меня можно назвать беззаботным человеком',
                          'Мне нравится работать в одиночестве',
                          'Меня считают живым и веселым человеком',
                          'Я не чувствую себя комфортно в какой-либо одежде, кроме повседневной',
                          'Я быстро и правильно могу сформулировать свои мысли словами',
                          'Мне нравится подшучивать над другими',
                          'При споре мои действия носят инмупльсивный характер',
                          'Мне не нравится брать взаймы или продавать что-нибудь, когда я нуждаюсь в деньгах',
                          'Я предпочел бы остаться в одиночестве дома, чем пойти на вечеринку',
                          'Я обычно планирую свои дела тщательно и сильно заранее',
                          'Я справляетесь с делом лучше, обдумав его самостоятельно, а не обсуждая с другими',
                          'Я человек, которого не волнует, чтобы все было именно так, как нужно',
                          'Я предпочитаю больше планировать, чем действовать',
                          'При знакомстве я обычно первым проявляю инициативу',
                          'Я часто думаю, что все само собой уладится и придет в норму',
                          'Иногда я действую необдуманно, под влиянием момента',
                          'Я не спеша обдумываю свои действия и предпочитаю подождать, прежде чем действовать',
                          'Мне не трудно внести оживление в скучную компанию',
                          'Когда на меня кричат, я могу ответить тем же']

      neuro_list = ['Часто у меня возникает чувство, что мне что-нибудь хочется, но я не знаю что',
                    'Я очень обеспокоен своим здоровьем',
                    'Мне не нравится, когда критикуют мою работу',
                    'У меня бывают приступы дрожи',
                    'У меня нет плохих привычек',
                    'Часто я придумываю что ответить слишком поздно',
                    'Я часто мечтаю',
                    'Часто я думаю о том, что мне не следовало что-то говорить или делать',
                    'Часто ли ваши мысли отвлекаются, когда вы пытаетесь сосредоточиться на чем-то?',
                    'У меня частые перепады настроения',
                    'Мне трудно отказываться от своих намерений',
                    'Я часто нуждаюсь в друзьях, которые могут меня понять, ободрить или посочувствовать',
                    'Я чувствителем к некоторым вещам',
                    'Часто мои нервы натянуты до предела',
                    'Бывает, я не могу уснуть из-за мыслей, которые лезут в голову',
                    'У меня бывают сильные сердцебиения',
                    'Меня часто называют раздражительным',
                    'Мне часто снятся кошмары',
                    'У меня бывают сильные головные боли',
                    'Я нервный человек',
                    'После того, как дело сделано, я часто мысленно возвращаюсь к нему и думаю, что мог бы сделать лучше',
                    'Часто мне не дают покоя мысли о разных неприятностях и "ужасах", которые могли бы произойти, но не произошли',
                    'Иногда я думаю, что я хуже других',
                    'Я страдаю бессонницей']

      lie_list = ['Я всегда сдерживаю обещание, даже если оно мне невыгодно',
                  'Я иногда упрямлюсь',
                  'Иногда я смеюсь над неприличными шутками',
                  'Я могу назвать себя человеком, полностью свободным от всяких предрассудков',
                  'Иногда я передаю слухи',
                  'Я всегда отвечаю на письмо сразу после прочтения',
                  'Иногда я откладываю  на завтра то, что должен сделать сегодня',
                  'Бывает, что я говорю неправду',
                  'Бывало, что я опаздывал на работу или встречу с кем-либо']

      FlagExtraIntro = False
      FlagNeuro = False
      FlagLie = False

token = "token"
bot = TelegramBot(token)

def extra_intro(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in
                   ['Да', 'Нет']])
    question = bot.extra_intro_list[bot.j]
    bot.send_message(message.chat.id, question, reply_markup=keyboard)
    bot.j += 1
    # bot.cnt += 1

def neuro(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in
                   ['Да', 'Нет']])
    question = bot.neuro_list[bot.j]
    bot.send_message(message.chat.id, question, reply_markup=keyboard)
    bot.j += 1
    bot.cnt += 1

def lie(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in
                   ['Да', 'Нет']])
    question = bot.lie_list[bot.j]
    bot.send_message(message.chat.id, question, reply_markup=keyboard)
    bot.j += 1
    bot.cnt += 1

# def between_stat(message):
#     bot.cnt = 0
#     bot.send_message(message.chat.id, f'Проверка подсчета:\n'
#                                       f'Экстраверсия-интроверсия: {bot.extraversion_introversion}, '
#                                       f'шкала лжи: {bot.lies}, баллов по нейротизму: {bot.neuro}'
#                                       f'\nПромежуточные результаты:')
#     results(message)
#     bot.send_message(message.chat.id, f'Продолжаем')

def stats(message):
    bot.send_message(message.chat.id, f'Баллов по экстраверсии-интроверсии {bot.extraversion_introversion}'
                                      f'\nБаллов по шкале лжи - {bot.lies}'
                                      f'\nБаллов по нейротизму - {bot.neuro}')

def results(message):
    # экстраверсия-интроверсия
    if bot.extraversion_introversion < 5:
        bot.send_message(message.chat.id, f'Глубокий интроверт')
    elif bot.extraversion_introversion < 9:
        bot.send_message(message.chat.id, f'Интроверт')
    elif bot.extraversion_introversion < 12:
        bot.send_message(message.chat.id, f'Склонность к интроверсии')
    elif bot.extraversion_introversion == 12:
        bot.send_message(message.chat.id, f'Среднее значение по шкале интроверсия-экстраверсия')
    elif bot.extraversion_introversion <= 15:
        bot.send_message(message.chat.id, f'Склонность к экстраверсии')
    elif bot.extraversion_introversion <= 19:
        bot.send_message(message.chat.id, f'Экстраверт')
    elif bot.extraversion_introversion > 19:
        bot.send_message(message.chat.id, f'Яркий экстраверт')

    # нейротизм
    if bot.neuro < 9:
        bot.send_message(message.chat.id, f'Низкий уровень нейротизма')
    elif bot.neuro < 14:
        bot.send_message(message.chat.id, f'Среднее значение')
    elif bot.neuro <= 19:
        bot.send_message(message.chat.id, f'Высокий уровень нейротизма')
    elif bot.neuro > 19:
        bot.send_message(message.chat.id, f'Очень высокий уровень нейротизма')

    # шкала лжи
    if bot.lies >= 4:
        bot.send_message(message.chat.id, f'Кол-во баллов по шкале лжи больше четырех. Это означает, что Вы '
                         f'отвечали неискренне, также это свидетельствует о некоторой демонстративности поведения'
                         f'и ориентированности на социальное одобрение.')
def temp_results(message):
    # полярные
    if bot.extraversion_introversion <= 6 and bot.neuro >= 18: # 0-6, 18-24  6, 6
        bot.send_message(message.chat.id, f'Полярный Меланхолик')
    elif 6 < bot.extraversion_introversion < 12 and bot.neuro >= 18: #6-12 18-24
        bot.send_message(message.chat.id, f'Меланхолик с холеризмом')
    elif 12 < bot.extraversion_introversion <= 18 and bot.neuro >= 18: #12-18 18-24
        bot.send_message(message.chat.id, f'Холерик с меланхолизмом')
    elif bot.extraversion_introversion >= 18 and bot.neuro >= 18: # 18 -24 18-24
        bot.send_message(message.chat.id, f'Полярный Холерик')
    elif bot.extraversion_introversion >= 18 and 12 <= bot.neuro <= 12: # 18-24 6-12
        bot.send_message(message.chat.id, f'Холерик с сангвинизмом')
    elif bot.extraversion_introversion >= 18 and 6 <= bot.neuro < 0:# 18-24 0-6
        bot.send_message(message.chat.id, f'Сангвиник с холеризмом')
    elif bot.extraversion_introversion >= 18 and bot.neuro <= 6: # 18-24  0-6
        bot.send_message(message.chat.id, f'Полярный Сангвиник')
    elif 12 < bot.extraversion_introversion <= 18 and bot.neuro <= 6: # 12-18  0-6
        bot.send_message(message.chat.id, f'Сангвиник с флегматизмом')
    elif 6 < bot.extraversion_introversion <= 12 and bot.neuro <= 6: #6 - 12  0-6
        bot.send_message(message.chat.id, f'Флегматик с сангвинизмом')
    elif bot.extraversion_introversion <= 6 and bot.neuro <= 6: # 0-6  0-6
        bot.send_message(message.chat.id, f'Полярный Флегматик')
    elif bot.extraversion_introversion <= 6 and 6 < bot.neuro <= 12: # 0-6  6-12
        bot.send_message(message.chat.id, f'Флегматик с меланхолизмом')
    elif bot.extraversion_introversion <= 6 and 12 <= bot.neuro <= 18: # 0-6  12 -18
        bot.send_message(message.chat.id, f'Меланхолик с флегматизмом')
    elif 6 < bot.extraversion_introversion <= 12 and 12 <= bot.neuro <= 18: # 6-12  12-18
        bot.send_message(message.chat.id, f'Меланхолик с сангвинизмом')
    elif 12 < bot.extraversion_introversion <= 18 and 12 <= bot.neuro <= 18: # 12-18  12-18
        bot.send_message(message.chat.id, f'Холерик с флегматизмом')
    elif 6 < bot.extraversion_introversion <= 12 and 6 <= bot.neuro <= 12: # 6-12 6-12
        bot.send_message(message.chat.id, f'Флегматик с холеризмом')
    elif 12 < bot.extraversion_introversion <= 18 and 6 <= bot.neuro <= 12: # 12-18  6-12
        bot.send_message(message.chat.id, f'Сангвиник с меланхолизмом')

def second_temp(message):
    bot.send_message(message.chat.id, f'Также вам близок:')
    if bot.extraversion_introversion <= 6 and bot.neuro <= 6:
        bot.extraversion_introversion += 6
        bot.neuro += 6
    if bot.extraversion_introversion > 6 and bot.neuro > 6:
        bot.extraversion_introversion -= 6
        bot.neuro -= 6
        temp_results(message)

@bot.message_handler(commands=['start'])
def send_welcome(message):
   bot.j = 0
   bot.FlagExtraIntro = False
   bot.FlagNeuro = False
   bot.FlagLie = False
   bot.extraversion_introversion = 0
   bot.neuro = 0
   bot.lies = 0

   bot.reply_to(message, f"Привет, {message.from_user.first_name}")
   keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
   keyboard.add(*[types.KeyboardButton(name) for name in
               ['Начнем', 'Результат']])
   bot.send_message(message.chat.id,  f'Я - бот, который определит твой темперамент'
                                      f'\nТы ведь знаешь, что людей с полярными темпераментами (чистыми) крайне мало?'
                                      f'\nПоэтому я помогу тебе определить твой смешанный тип темперамента.'
                                      f'\nВ качестве основы для опроса я использую методику известного психолога Г. Айзенка'
                                      f'\n'
                                      f'\nВсего тест содержит 57 вопросов, которые направлены на выявление экстраверсии или'
                                      f' интроверсии, а также твою степень нейротизма (степень эмоционально стабильности'
                                      f' или нестабильности)'
                                      f'\n'
                                      f'\nНу что, начнем?', reply_markup=keyboard)

@bot.message_handler(content_types="text")
def quesion_call(message):
   if message.text == 'Начнем':
       bot.FlagExtraIntro = True
       extra_intro(message)
   if message.text == 'Назад':
       send_welcome(message)
   if message.text == 'Результат':
       stats(message)
       results(message)
       temp_results(message)
       second_temp(message)
   if message.text == 'Да':
       bot.cnt += 1
       # if bot.cnt == 10:
       #      between_stat(message)
       if bot.FlagExtraIntro == True:
           if bot.j < len(bot.extra_intro_list):
               if bot.j-1 == 0 or bot.j-1 == 1 or bot.j-1 == 3 or bot.j-1 == 4 or bot.j-1 == 5 or bot.j-1 == 7:
                   extra_intro(message)
                   bot.extraversion_introversion += 1
               elif bot.j-1 == 9 or bot.j-1 == 10 or bot.j-1 == 11 or bot.j-1 == 16 or bot.j-1 == 18 or bot.j-1 == 19:
                   extra_intro(message)
                   bot.extraversion_introversion += 1
               elif bot.j-1 == 20 or bot.j-1 == 22 or bot.j-1 == 23:
                   extra_intro(message)
                   bot.extraversion_introversion += 1
               else:
                   extra_intro(message)
           else:
               bot.j = 0
               bot.FlagExtraIntro = False
               bot.FlagLie = True
               lie(message)

       elif bot.FlagLie == True:
           if bot.j < len(bot.lie_list):
               if bot.j-1 == 0 or bot.j-1 == 3 or bot.j-1 == 5:
                   lie(message)
                   bot.lies += 1
               else:
                   lie(message)
           else:
               bot.j = 0
               bot.FlagLie = False
               bot.FlagNeuro = True
               neuro(message)

       elif bot.FlagNeuro == True:
           if bot.j < len(bot.neuro_list):
               neuro(message)
               bot.neuro += 1
           else:
               bot.j = 0
               bot.FlagLie = False
               bot.FlagNeuro = True
               keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
               keyboard.add(*[types.KeyboardButton(name) for name in ['Результат']])
               bot.send_message(message.chat.id, f'Спасибо! Можешь посмотреть результаты', reply_markup=keyboard)

   if message.text == 'Нет':
       bot.cnt += 1
       # if bot.cnt == 10:
       #      between_stat(message)
       if bot.FlagExtraIntro == True:
           if bot.j < len(bot.extra_intro_list):
               if bot.j-1 == 2 or bot.j-1 == 6 or bot.j-1 == 8 or bot.j-1 == 12 or bot.j-1 == 13 or bot.j-1 == 14:
                   extra_intro(message)
                   bot.extraversion_introversion += 1
               elif bot.j-1 == 15 or bot.j-1 == 17 or bot.j-1 == 21:
                   extra_intro(message)
                   bot.extraversion_introversion += 1
               else:
                   extra_intro(message)
           else:
               bot.j = 0
               bot.FlagExtraIntro = False
               bot.FlagLie = True
               lie(message)

       elif bot.FlagLie == True:
           if bot.j < len(bot.lie_list):
               if bot.j-1 == 1 or bot.j-1 == 2 or bot.j-1 == 4 or bot.j-1 == 6 or bot.j-1 == 7 or bot.j-1 == 8:
                   bot.lies += 1
                   lie(message)
               else:
                   lie(message)
           else:
               bot.j = 0
               bot.FlagLie = False
               bot.FlagNeuro = True
               neuro(message)

       elif bot.FlagNeuro == True:
           if bot.j < len(bot.neuro_list):
               neuro(message)
           else:
               keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
               keyboard.add(*[types.KeyboardButton(name) for name in
                              ['Результат']])
               bot.send_message(message.chat.id, f'Спасибо! Можешь посмотреть результаты', reply_markup=keyboard)

bot.infinity_polling()
