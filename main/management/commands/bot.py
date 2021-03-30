from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext, Filters, RegexHandler, MessageHandler
import requests, calendar
import datetime
import simplejson
from django.conf import settings
from ._base import BotBase
from main.models import UserTelegram, Client
from main.functions import user_func, client_func
from django.core.validators import EmailValidator
from main.validators import PhoneValidator


class Command(BotBase):
    def delete(self, update: Update, context: CallbackContext) -> None:
        user = user_func(update)

        query = update.callback_query
        query.answer()
        query.message.delete()
        print(user.breakfast, user.baby, user.pet)

    def start(self, update: Update, context: CallbackContext) -> None:
        user = user_func(update)

        keyboard = [
            [
                InlineKeyboardButton("Бронировать", callback_data='calendar')
            ],
            [
                InlineKeyboardButton("Комнаты", callback_data='1kom')

            ],
            [
                InlineKeyboardButton("Условия", callback_data='2kom')

            ],
            [
                InlineKeyboardButton("О нас", callback_data='info')

            ]
        ]

        reply_markup = InlineKeyboardMarkup(keyboard)
        update.message.reply_text(f"Меню", reply_markup=reply_markup)

    def meal(self, update: Update, context: CallbackContext) -> None:
        user = user_func(update)

        if user.breakfast == '0':
            user.breakfast = '1'
        elif user.breakfast == '1':
            user.breakfast = '0'
        user.save()

        query = update.callback_query
        query.answer()
        keyboard = [
            [
                InlineKeyboardButton("Yotoq soni " + str(user.bed), callback_data='number'),
                InlineKeyboardButton(f"Nonushta {'❌' if user.breakfast == '0' else '✅'}", callback_data='meal')

            ],
            [
                InlineKeyboardButton(f"Yosh bolalar {'❌' if user.baby == '0' else '✅'}", callback_data='baby'),
                InlineKeyboardButton(f"Uy hayvoni {'❌' if user.pet == '0' else '✅'}", callback_data='pet')
            ],
            [
                InlineKeyboardButton("Забронировать", callback_data='calendar2')

            ],
            [
                InlineKeyboardButton("nazad", callback_data='delete')

            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        print(user.breakfast, user.baby, user.pet)
        query.message.edit_caption(caption='''
         ***В стоимость номеров входит завтрак на 2 персоны. Детям до 3х лет - завтрак бесплатный. Свыше 3х лет - 100.000 сум за персону.

     Также можно заехать без обязательства снятия гостиничного номера, в распоряжении гостей

     бассейн
     3 сауны
     ресторанный комплекс
     Стоимость на 1 человека - 300.000 сум, детям до 12 лет бесплатно. Посещение доступно до 18:00.
         ''', reply_markup=reply_markup)

    def baby(self, update: Update, context: CallbackContext) -> None:
        user = user_func(update)
        if user.baby == '0':
            user.baby = "1"
        elif user.baby == '1':
            user.baby = "0"
        user.save()

        query = update.callback_query
        query.answer()
        keyboard = [
            [
                InlineKeyboardButton("Yotoq soni " + str(user.bed), callback_data='number'),
                InlineKeyboardButton(f"Nonushta {'❌' if user.breakfast == '0' else '✅'}", callback_data='meal')

            ],
            [
                InlineKeyboardButton(f"Yosh bolalar {'❌' if user.baby == '0' else '✅'}", callback_data='baby'),
                InlineKeyboardButton(f"Uy hayvoni {'❌' if user.pet == '0' else '✅'}", callback_data='pet')

            ],
            [
                InlineKeyboardButton("Забронировать", callback_data='calendar2')

            ],
            [
                InlineKeyboardButton("nazad", callback_data='delete')

            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        print(user.breakfast, user.baby, user.pet)
        query.message.edit_caption(caption='''
         ***В стоимость номеров входит завтрак на 2 персоны. Детям до 3х лет - завтрак бесплатный. Свыше 3х лет - 100.000 сум за персону.

     Также можно заехать без обязательства снятия гостиничного номера, в распоряжении гостей

     бассейн
     3 сауны
     ресторанный комплекс
     Стоимость на 1 человека - 300.000 сум, детям до 12 лет бесплатно. Посещение доступно до 18:00.
         ''', reply_markup=reply_markup)

    def pet(self, update: Update, context: CallbackContext) -> None:
        user = user_func(update)
        if user.pet == '0':
            user.pet = '1'
        elif user.pet == '1':
            user.pet = '0'
        user.save()

        query = update.callback_query
        query.answer()
        keyboard = [
            [
                InlineKeyboardButton("Yotoq soni " + str(user.bed), callback_data='number'),
                InlineKeyboardButton(f"Nonushta {'❌' if user.breakfast == '0' else '✅'}", callback_data='meal')

            ],
            [
                InlineKeyboardButton(f"Yosh bolalar {'❌' if user.baby == '0' else '✅'}", callback_data='baby'),
                InlineKeyboardButton(f"Uy hayvoni {'❌' if user.pet == '0' else '✅'}", callback_data='pet')

            ],
            [
                InlineKeyboardButton("Забронировать", callback_data='calendar2')

            ],
            [
                InlineKeyboardButton("nazad", callback_data='delete')

            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        print(user.breakfast, user.baby, user.pet)
        query.message.edit_caption(caption='''
         ***В стоимость номеров входит завтрак на 2 персоны. Детям до 3х лет - завтрак бесплатный. Свыше 3х лет - 100.000 сум за персону.

     Также можно заехать без обязательства снятия гостиничного номера, в распоряжении гостей

     бассейн
     3 сауны
     ресторанный комплекс
     Стоимость на 1 человека - 300.000 сум, детям до 12 лет бесплатно. Посещение доступно до 18:00.
         ''', reply_markup=reply_markup)

    def number(self, update: Update, context: CallbackContext) -> None:
        user = user_func(update)
        user.bed = int(user.bed) + 1
        if int(user.bed) > 3:
            user.bed = '1'
        user.save()

        query = update.callback_query
        query.answer()
        keyboard = [
            [
                InlineKeyboardButton("Yotoq soni " + str(user.bed), callback_data='number'),
                InlineKeyboardButton(f"Nonushta {'❌' if user.breakfast == '0' else '✅'}", callback_data='meal')

            ],
            [
                InlineKeyboardButton(f"Yosh bolalar {'❌' if user.baby == '0' else '✅'}", callback_data='baby'),
                InlineKeyboardButton(f"Uy hayvoni {'❌' if user.pet == '0' else '✅'}", callback_data='pet')

            ],
            [
                InlineKeyboardButton("Забронировать", callback_data='calendar2')

            ],
            [
                InlineKeyboardButton("nazad", callback_data='delete')

            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        print(user.breakfast, user.baby, user.pet)
        query.message.edit_caption(caption='''
         ***В стоимость номеров входит завтрак на 2 персоны. Детям до 3х лет - завтрак бесплатный. Свыше 3х лет - 100.000 сум за персону.

     Также можно заехать без обязательства снятия гостиничного номера, в распоряжении гостей

     бассейн
     3 сауны
     ресторанный комплекс
     Стоимость на 1 человека - 300.000 сум, детям до 12 лет бесплатно. Посещение доступно до 18:00.
         ''', reply_markup=reply_markup)

    def button(self, update: Update, context: CallbackContext) -> None:
        go = "0"
        query = update.callback_query
        query.answer()
        keyboard = []
        menu = 'Меню'
        if query.data == '1kom':
            keyboard = [
                [
                    InlineKeyboardButton("Economy", callback_data='comnE')

                ],
                [
                    InlineKeyboardButton("Standart", callback_data='comnS')

                ],
                [
                    InlineKeyboardButton("Deluxe", callback_data='comnD')

                ],
                [
                    InlineKeyboardButton("Luxe", callback_data='comnL')

                ],
                [
                    InlineKeyboardButton("Назад", callback_data='asd')

                ]
            ]
            reply_markup = InlineKeyboardMarkup(keyboard)
            query.edit_message_text(text=menu, reply_markup=reply_markup)
        if query.data == 'comnE' or query.data == 'comnS' or query.data == 'comnD' or query.data == 'comnL':
            user = user_func(update)
            photo = ''
            if query.data == 'comnE':
                photo = 'econom.jpg'
            elif query.data == 'comnS':
                photo = 'standart.jpg'
            elif query.data == 'comnD':
                photo = 'yarimluks.jpg'
            elif query.data == 'comnL':
                photo = 'luks.jpg'

            keyboard = [
                [
                    InlineKeyboardButton("Yotoq soni " + str(user.bed), callback_data='number'),
                    InlineKeyboardButton(f"Nonushta {'❌' if user.breakfast == '0' else '✅'}", callback_data='meal')

                ],
                [
                    InlineKeyboardButton(f"Yosh bolalar {'❌' if user.baby == '0' else '✅'}", callback_data='baby'),
                    InlineKeyboardButton(f"Uy hayvoni {'❌' if user.pet == '0' else '✅'}", callback_data='pet')

                ],
                [
                    InlineKeyboardButton("Забронировать", callback_data='calendar2')

                ],
                [
                    InlineKeyboardButton("nazad", callback_data='delete')

                ]
            ]
            reply_markup = InlineKeyboardMarkup(keyboard)
            query.message.reply_photo(photo=open(photo, 'rb'), caption='''
        ***В стоимость номеров входит завтрак на 2 персоны. Детям до 3х лет - завтрак бесплатный. Свыше 3х лет - 100.000 сум за персону.

    Также можно заехать без обязательства снятия гостиничного номера, в распоряжении гостей

    бассейн
    3 сауны
    ресторанный комплекс
    Стоимость на 1 человека - 300.000 сум, детям до 12 лет бесплатно. Посещение доступно до 18:00.
        ''', reply_markup=reply_markup)

        elif query.data == '2kom':
            keyboard = [
                [
                    InlineKeyboardButton("Спа", callback_data='spa')

                ],
                [
                    InlineKeyboardButton("Бассейн", callback_data='basseyn')

                ],
                [
                    InlineKeyboardButton("Ресторан", callback_data='restoran')

                ],
                [
                    InlineKeyboardButton("Назад", callback_data='asd')

                ]
            ]
            reply_markup = InlineKeyboardMarkup(keyboard)
            query.edit_message_text(text=menu, reply_markup=reply_markup)
        elif query.data == 'asd':
            keyboard = [
                [
                    InlineKeyboardButton("Бронировать", callback_data='calendar')
                ],
                [
                    InlineKeyboardButton("Комнаты", callback_data='1kom')

                ],
                [
                    InlineKeyboardButton("Условия", callback_data='2kom')

                ],
                [
                    InlineKeyboardButton("О нас", callback_data='info')

                ]
            ]
            reply_markup = InlineKeyboardMarkup(keyboard)
            query.edit_message_text(text=menu, reply_markup=reply_markup)

    def info(self, update: Update, context: CallbackContext) -> None:
        go = "0"
        query = update.callback_query
        query.answer()
        keyboard = []
        menu = 'Меню'
        user = user_func(update)

        keyboard = [
            [
                InlineKeyboardButton("nazad", callback_data='delete')

            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.message.reply_photo(photo=open('onas.jpg', 'rb'), caption='''
        Гостиница HEAVENS GARDEN открылась 31 августа 2020 года, имеет 46 номеров;  
        12 полулюксов, 4 люкса, 4 эконома и 26 стандарта. Бассейн расположен на улице и имеет подогрев. 
        Спа состоит из Финской сауны и Турецкого хаммама. В гостинице имеется бесплатный интернет а также спутниковое телевидение.
        ''', reply_markup=reply_markup)

    def spa(self, update: Update, context: CallbackContext) -> None:
        go = "0"
        query = update.callback_query
        query.answer()
        keyboard = []
        menu = 'Меню'
        user = user_func(update)

        keyboard = [
            [
                InlineKeyboardButton("nazad", callback_data='delete')

            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.message.reply_photo(photo=open('spa.jpg', 'rb'), caption='''
        Спа состоит из двух саун(финская,турецкая) и турецкий хаммам
        ''', reply_markup=reply_markup)

    def basseyn(self, update: Update, context: CallbackContext) -> None:
        go = "0"
        query = update.callback_query
        query.answer()
        keyboard = []
        menu = 'Меню'
        user = user_func(update)

        keyboard = [
            [
                InlineKeyboardButton("nazad", callback_data='delete')

            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.message.reply_photo(photo=open('basseyn.jpg', 'rb'), caption='''
        Бесплатный открытый бассейн для гостей сделан в формате Endless pool и имеет подогрев.
        ''', reply_markup=reply_markup)

    def restoran(self, update: Update, context: CallbackContext) -> None:
        go = "0"
        query = update.callback_query
        query.answer()
        keyboard = []
        menu = 'Меню'
        user = user_func(update)

        keyboard = [
            [
                InlineKeyboardButton("nazad", callback_data='delete')

            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.message.reply_photo(photo=open('res.jpg', 'rb'), caption='''
        
        ''', reply_markup=reply_markup)

    def calendar(self, update: Update, context: CallbackContext) -> None:

        query = update.callback_query
        query.answer()
        user = user_func(update)
        asd = datetime.date.today()
        d1 = asd + datetime.timedelta(days=1)
        d2 = asd + datetime.timedelta(days=2)
        keyboard = [
            [
                InlineKeyboardButton('bugun', callback_data='{}'.format(d1))
            ],
            [
                InlineKeyboardButton('ertaga', callback_data='{}'.format(d2))
            ],
            [
                InlineKeyboardButton('kalendar', callback_data='days')
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        query.edit_message_text("kunni tanlash", reply_markup=reply_markup)

    def calendar2(self, update: Update, context: CallbackContext) -> None:

        query = update.callback_query
        query.answer()
        query.message.delete()
        asd = datetime.date.today()
        print(asd)
        d1 = asd + datetime.timedelta(days=1)
        d2 = asd + datetime.timedelta(days=2)
        user = user_func(update)
        keyboard = [
            [
                InlineKeyboardButton('bugun', callback_data='{}'.format(d1))
            ],
            [
                InlineKeyboardButton('ertaga', callback_data='{}'.format(d2))
            ],
            [
                InlineKeyboardButton('kalendar', callback_data='days')
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.message.reply_text("kunni tanlash", reply_markup=reply_markup)


    def days(self, update: Update, context: CallbackContext) -> None:
        print('first day')
        go = "0"
        query = update.callback_query
        query.answer()
        keyboard = []
        menu = 'Меню'
        user = user_func(update)
        asd = datetime.date.today()
        print(type(asd))

        tmp = []
        keyboard = []
        i = 1
        y = 1
        while i <= 5:
            while y <= 6:
                tmp.append(InlineKeyboardButton('{0:02d}.{1:02d}'.format(asd.day, asd.month),
                                                callback_data='{}'.format(asd)))
                asd += datetime.timedelta(days=1)

                y += 1
            y = 1
            keyboard.append(tmp)
            tmp = []
            i += 1

        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text("Boshlang'ich kunni tanlang", reply_markup=reply_markup)

    def days2(self, update: Update, context: CallbackContext) -> None:

        query = update.callback_query
        query.answer()

        user = user_func(update)
        mydate = query.data.replace('-', '/')
        print(str(mydate)[2:])
        date_time_str = str(mydate)[2:]+' 00:00:00'

        date_time_obj = datetime.datetime.strptime(date_time_str, '%y/%m/%d %H:%M:%S')

        asd = date_time_obj.date()
        asd = asd + datetime.timedelta(days=1)

        tmp = []
        keyboard = []
        i = 1
        y = 1
        while i <= 5:
            while y <= 6:
                tmp.append(InlineKeyboardButton('{0:02d}.{1:02d}'.format(asd.day, asd.month), callback_data='done'))
                asd += datetime.timedelta(days=1)
                y += 1
            y = 1
            keyboard.append(tmp)
            tmp = []
            i += 1

        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text("oxirgi kunni tanlang", reply_markup=reply_markup)

    def done(self, update: Update, context: CallbackContext) -> None:
        client = client_func(update)
        user = user_func(update)
        query = update.callback_query
        query.answer()
        client.state = Client.STATE_FULLNAME
        client.save()

        asd = datetime.date.today()

        keyboard = [
            [
                InlineKeyboardButton('ortga', callback_data='asd')
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text("Xona olish uchun iltimos shaxsim ma'lumotlaringizni to'ldiring\nTo'liq ismingizni kiriting")

    def message_handler(self, update: Update, context: CallbackContext) -> None:
        try:
            query = update.callback_query
            query.answer()
        except:
            pass
        client = client_func(update)
        try:
            msg = str(update.message.text).strip()
        except:
            pass
        if client.state == Client.STATE_FULLNAME:
            client.fullName = msg
            client.state = Client.STATE_PHONE
        elif client.state == Client.STATE_PHONE:
            phoneValid = PhoneValidator()
            try:
                phoneValid(msg)
            except:
                update.message.reply_text("Iltmos to'g'ri telefon raqam kiriting")
                return
            client.phone = msg
            client.state = Client.STATE_EMAIL
        elif client.state == Client.STATE_EMAIL:
            validator = EmailValidator()
            try:
                validator(msg)
            except:
                update.message.reply_text("Iltmos to'g'ri email kiriting")
                return
            client.email = msg
            client.state = Client.STATE_COUNTRY
        elif client.state == Client.STATE_COUNTRY:
            client.country = msg
            client.state = Client.STATE_IS_FIRM
        elif client.state == Client.STATE_IS_FIRM:
            query.message.delete()

            client.is_firm = int(query.data)
            client.state = 9
        client.save()
        self.state_response(update, client)

    def state_response(self, update: Update, client: Client):
        text = {
            Client.STATE_FULLNAME: "To'liq ismingizni jo'nating",
            Client.STATE_PHONE: "Telefon raqamingizni kiriting\n(+998XXXXXXXXX)",
            Client.STATE_EMAIL: "Elektron pochtangizni kiriting",
            Client.STATE_COUNTRY: "Manzilingizni kiriting",
            Client.STATE_IS_FIRM: "is firm"
        }

        if client.state == 3:
            keyboard = [
                [
                    InlineKeyboardButton("yes", callback_data='1'),
                    InlineKeyboardButton("no", callback_data='0')

                ]
            ]

            reply_markup = InlineKeyboardMarkup(keyboard)
            update.message.reply_text(text.get(client.state), reply_markup=reply_markup)
        elif client.state == 9:
            keyboard = [
                [
                    InlineKeyboardButton("Asosiy", callback_data='asd')

                ]
            ]

            reply_markup = InlineKeyboardMarkup(keyboard)
            self.updater.bot.send_message(chat_id=client.telegram_user_id, text="Sizning arizangiz Qabul qilindi javobni kuting", reply_markup=reply_markup)
            # update.message.reply_text(f"Sizning arizangiz Qabul qilindi javobni kuting", reply_markup=reply_markup)
        else:
            self.updater.bot.send_message(chat_id=client.telegram_user_id, text=text.get(client.state))

    def handle(self, *args, **kwargs):
        dispatcher = self.updater.dispatcher
        dispatcher.add_handler(CallbackQueryHandler(self.delete, pattern="^(delete)$"))
        dispatcher.add_handler(CallbackQueryHandler(self.meal, pattern="^(meal)$"))
        dispatcher.add_handler(CallbackQueryHandler(self.baby, pattern="^(baby)$"))
        dispatcher.add_handler(CallbackQueryHandler(self.pet, pattern="^(pet)$"))
        dispatcher.add_handler(CallbackQueryHandler(self.calendar, pattern="^(calendar)$"))
        dispatcher.add_handler(CallbackQueryHandler(self.calendar2, pattern="^(calendar2)$"))
        dispatcher.add_handler(CallbackQueryHandler(self.days, pattern="^(days)$"))
        dispatcher.add_handler(CallbackQueryHandler(self.days2, pattern="^(\d{4}\-\d{2}\-\d{2})$"))
        dispatcher.add_handler(CallbackQueryHandler(self.message_handler, pattern="^(\d{1})$"))
        dispatcher.add_handler(CallbackQueryHandler(self.done, pattern="^(done)$"))

        dispatcher.add_handler(CallbackQueryHandler(self.spa, pattern="^(spa)$"))
        dispatcher.add_handler(CallbackQueryHandler(self.basseyn, pattern="^(basseyn)$"))
        dispatcher.add_handler(CallbackQueryHandler(self.restoran, pattern="^(restoran)$"))

        dispatcher.add_handler(CallbackQueryHandler(self.info, pattern="^(info)$"))
        dispatcher.add_handler(CallbackQueryHandler(self.number, pattern="^(number)$"))
        dispatcher.add_handler(CommandHandler('start', self.start))
        dispatcher.add_handler(CallbackQueryHandler(self.button))

        dispatcher.add_handler(MessageHandler(Filters.all & ~Filters.command, self.message_handler))

        self.updater.start_polling()
        self.updater.idle()
