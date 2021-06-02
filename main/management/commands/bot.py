from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext, Filters, RegexHandler, MessageHandler
import requests, calendar
import datetime
import simplejson
from django.conf import settings
from ._base import BotBase
from ._words import getword
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
                InlineKeyboardButton("O'zbekcha", callback_data='asd1')
            ],
            [
                InlineKeyboardButton("русский", callback_data='asd2')
            ],
            [
                InlineKeyboardButton("english", callback_data='asd3')
            ]
        ]

        reply_markup = InlineKeyboardMarkup(keyboard)
        update.message.reply_text(f"выберите язык", reply_markup=reply_markup)

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
                InlineKeyboardButton(f"{getword('1',str(user.lan))} " + str(user.bed), callback_data='number'),
                InlineKeyboardButton(f"{getword('2',str(user.lan))} {'❌' if user.breakfast == '0' else '✅'}", callback_data='meal')

            ],
            [
                InlineKeyboardButton(f"{getword('3',str(user.lan))} {'❌' if user.baby == '0' else '✅'}", callback_data='baby'),
                InlineKeyboardButton(f"{getword('4',str(user.lan))} {'❌' if user.pet == '0' else '✅'}", callback_data='pet')
            ],
            [
                InlineKeyboardButton(f"{getword('5',str(user.lan))}", callback_data='calendar2')

            ],
            [
                InlineKeyboardButton(f"{getword('6',str(user.lan))}", callback_data='delete')

            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        print(user.breakfast, user.baby, user.pet)
        query.message.edit_caption(caption=getword('7', str(user.lan)), reply_markup=reply_markup)

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
                InlineKeyboardButton(f"{getword('1', str(user.lan))} " + str(user.bed), callback_data='number'),
                InlineKeyboardButton(f"{getword('2', str(user.lan))} {'❌' if user.breakfast == '0' else '✅'}",
                                     callback_data='meal')

            ],
            [
                InlineKeyboardButton(f"{getword('3', str(user.lan))} {'❌' if user.baby == '0' else '✅'}",
                                     callback_data='baby'),
                InlineKeyboardButton(f"{getword('4', str(user.lan))} {'❌' if user.pet == '0' else '✅'}",
                                     callback_data='pet')
            ],
            [
                InlineKeyboardButton(f"{getword('5', str(user.lan))}", callback_data='calendar2')

            ],
            [
                InlineKeyboardButton(f"{getword('6', str(user.lan))}", callback_data='delete')

            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        print(user.breakfast, user.baby, user.pet)
        query.message.edit_caption(caption=getword('7', str(user.lan)), reply_markup=reply_markup)

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
                InlineKeyboardButton(f"{getword('1', str(user.lan))} " + str(user.bed), callback_data='number'),
                InlineKeyboardButton(f"{getword('2', str(user.lan))} {'❌' if user.breakfast == '0' else '✅'}",
                                     callback_data='meal')

            ],
            [
                InlineKeyboardButton(f"{getword('3', str(user.lan))} {'❌' if user.baby == '0' else '✅'}",
                                     callback_data='baby'),
                InlineKeyboardButton(f"{getword('4', str(user.lan))} {'❌' if user.pet == '0' else '✅'}",
                                     callback_data='pet')
            ],
            [
                InlineKeyboardButton(f"{getword('5', str(user.lan))}", callback_data='calendar2')

            ],
            [
                InlineKeyboardButton(f"{getword('6', str(user.lan))}", callback_data='delete')

            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        print(user.breakfast, user.baby, user.pet)
        query.message.edit_caption(caption=getword('7', str(user.lan)), reply_markup=reply_markup)

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
                InlineKeyboardButton(f"{getword('1', str(user.lan))} " + str(user.bed), callback_data='number'),
                InlineKeyboardButton(f"{getword('2', str(user.lan))} {'❌' if user.breakfast == '0' else '✅'}",
                                     callback_data='meal')

            ],
            [
                InlineKeyboardButton(f"{getword('3', str(user.lan))} {'❌' if user.baby == '0' else '✅'}",
                                     callback_data='baby'),
                InlineKeyboardButton(f"{getword('4', str(user.lan))} {'❌' if user.pet == '0' else '✅'}",
                                     callback_data='pet')
            ],
            [
                InlineKeyboardButton(f"{getword('5', str(user.lan))}", callback_data='calendar2')

            ],
            [
                InlineKeyboardButton(f"{getword('6', str(user.lan))}", callback_data='delete')

            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        print(user.breakfast, user.baby, user.pet)
        query.message.edit_caption(caption=getword('7', str(user.lan)), reply_markup=reply_markup)

    def button(self, update: Update, context: CallbackContext) -> None:
        user = user_func(update)
        go = "0"
        query = update.callback_query
        query.answer()
        keyboard = []
        menu = 'Меню'
        asd = query.data[:3]
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
                    InlineKeyboardButton(getword('6', str(user.lan)), callback_data='asd')

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
                    InlineKeyboardButton(f"{getword('1', str(user.lan))} " + str(user.bed), callback_data='number'),
                    InlineKeyboardButton(f"{getword('2', str(user.lan))} {'❌' if user.breakfast == '0' else '✅'}",
                                         callback_data='meal')

                ],
                [
                    InlineKeyboardButton(f"{getword('3', str(user.lan))} {'❌' if user.baby == '0' else '✅'}",
                                         callback_data='baby'),
                    InlineKeyboardButton(f"{getword('4', str(user.lan))} {'❌' if user.pet == '0' else '✅'}",
                                         callback_data='pet')
                ],
                [
                    InlineKeyboardButton(f"{getword('5', str(user.lan))}", callback_data='calendar2')

                ],
                [
                    InlineKeyboardButton(f"{getword('6', str(user.lan))}", callback_data='delete')

                ]
            ]
            reply_markup = InlineKeyboardMarkup(keyboard)
            query.message.reply_photo(photo=open(photo, 'rb'), caption=getword('7', str(user.lan)), reply_markup=reply_markup)

        elif query.data == '2kom':
            keyboard = [
                [
                    InlineKeyboardButton(getword('8', str(user.lan)), callback_data='spa')

                ],
                [
                    InlineKeyboardButton(getword('9', str(user.lan)), callback_data='basseyn')

                ],
                [
                    InlineKeyboardButton(getword('10', str(user.lan)), callback_data='restoran')

                ],
                [
                    InlineKeyboardButton(getword('6', str(user.lan)), callback_data='asd')

                ]
            ]
            reply_markup = InlineKeyboardMarkup(keyboard)
            query.edit_message_text(text=menu, reply_markup=reply_markup)
        elif asd == 'asd':
            print('asd')
            if len(query.data) == 4:
                print('asd22')
                j = query.data[3]
                print(j)
                user = user_func(update)
                if j == '1':
                    user.lan = 'uz'
                    print('uzzz')
                elif j == '2':
                    user.lan = 'ru'
                    print('susss')
                elif j == '3':
                    user.lan = 'en'
            user.save()

            keyboard = [
                [
                    InlineKeyboardButton(getword('11', str(user.lan)), callback_data='calendar')
                ],
                [
                    InlineKeyboardButton(getword('12', str(user.lan)), callback_data='1kom')

                ],
                [
                    InlineKeyboardButton(getword('13', str(user.lan)), callback_data='2kom')

                ],
                [
                    InlineKeyboardButton(getword('14', str(user.lan)), callback_data='info')

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
                InlineKeyboardButton(getword('6', str(user.lan)), callback_data='delete')

            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.message.reply_photo(photo=open('onas.jpg', 'rb'), caption=getword('15', user.lan), reply_markup=reply_markup)

    def spa(self, update: Update, context: CallbackContext) -> None:
        query = update.callback_query
        query.answer()
        user = user_func(update)

        keyboard = [
            [
                InlineKeyboardButton(getword('6', user.lan), callback_data='delete')

            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.message.reply_photo(photo=open('spa.jpg', 'rb'), caption=getword('16', user.lan), reply_markup=reply_markup)

    def basseyn(self, update: Update, context: CallbackContext) -> None:
        query = update.callback_query
        query.answer()
        user = user_func(update)

        keyboard = [
            [
                InlineKeyboardButton(getword('6', user.lan), callback_data='delete')

            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.message.reply_photo(photo=open('basseyn.jpg', 'rb'), caption=getword('17', user.lan),
                                  reply_markup=reply_markup)

    def restoran(self, update: Update, context: CallbackContext) -> None:
        query = update.callback_query
        query.answer()
        user = user_func(update)

        keyboard = [
            [
                InlineKeyboardButton(getword('6', user.lan), callback_data='delete')

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
                InlineKeyboardButton(getword('18', user.lan), callback_data='{}'.format(d1))
            ],
            [
                InlineKeyboardButton(getword('19', user.lan), callback_data='{}'.format(d2))
            ],
            [
                InlineKeyboardButton(getword('20', user.lan), callback_data='days')
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text(getword('21', user.lan), reply_markup=reply_markup)

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
                InlineKeyboardButton(getword('18', user.lan), callback_data='{}'.format(d1))
            ],
            [
                InlineKeyboardButton(getword('19', user.lan), callback_data='{}'.format(d2))
            ],
            [
                InlineKeyboardButton(getword('20', user.lan), callback_data='days')
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.message.reply_text(getword('21', user.lan), reply_markup=reply_markup)


    def days(self, update: Update, context: CallbackContext) -> None:
        query = update.callback_query
        query.answer()
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
        query.edit_message_text(getword('22',user.lan), reply_markup=reply_markup)

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
        query.edit_message_text(getword('23', user.lan), reply_markup=reply_markup)

    def done(self, update: Update, context: CallbackContext) -> None:
        user = user_func(update)
        client = client_func(update, user)
        query = update.callback_query
        query.answer()
        client.state = Client.STATE_FULLNAME
        client.save()

        asd = datetime.date.today()

        keyboard = [
            [
                InlineKeyboardButton(getword('6', user.lan), callback_data='asd')
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text(getword('24', user.lan))

    def message_handler(self, update: Update, context: CallbackContext) -> None:
        user = user_func(update)
        try:
            query = update.callback_query
            query.answer()
        except:
            pass
        client = client_func(update, user)
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
                update.message.reply_text(getword('25', user.lan))
                return
            client.phone = msg
            client.state = Client.STATE_EMAIL
        elif client.state == Client.STATE_EMAIL:
            validator = EmailValidator()
            try:
                validator(msg)
            except:
                update.message.reply_text(getword('26', user.lan))
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
        user = user_func(update)
        text = {
            Client.STATE_FULLNAME: getword('27', user.lan),
            Client.STATE_PHONE: f"{getword('28', user.lan)}\n(+998XXXXXXXXX)",
            Client.STATE_EMAIL: getword('29', user.lan),
            Client.STATE_COUNTRY: getword('30', user.lan),
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
                    InlineKeyboardButton(getword('31', user.lan), callback_data='asd')

                ]
            ]
            #todo adminga
            adminkey = [[InlineKeyboardButton('qabul qilish', callback_data='asd')]]
            reply_markup = InlineKeyboardMarkup(adminkey)
            self.updater.bot.send_message(chat_id=920393608, text=str(client), reply_markup=reply_markup)

            reply_markup = InlineKeyboardMarkup(keyboard)
            self.updater.bot.send_message(chat_id=client.telegram_user_id,
                                          text=getword('32', user.lan),
                                          reply_markup=reply_markup)
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
