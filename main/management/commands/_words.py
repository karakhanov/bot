def getword(word, lang):
    language = {
        '1': {
            'uz': 'Yotoq soni',
            'ru': 'Кол-во спальных мест',
            'en': 'asd'
        },
        '2': {
            'uz': 'Nonushta',
            'ru': 'Завтрак',
            'en': 'asd'
        },
        '3': {
            'uz': 'Yosh bolalar',
            'ru': 'Дети',
            'en': 'asd'
        },
        '4': {
            'uz': 'Uy hayvoni',
            'ru': 'Домашние питомцы',
            'en': 'asd'
        },
        '5': {
            'uz': 'Band qilish',
            'ru': 'Забронировать',
            'en': 'asd'
        },
        '6': {
            'uz': 'orqaga',
            'ru': 'назад ',
            'en': 'asd'
        },
        '7': {
            'uz': '''
            Xona narxiga 2 kishilik nonushta kiradi. 3 yoshgacha bo'lgan bolalarga - nonushta bepul. 3 yoshdan ortiq -
          Bir kishiga 100.000 so'm.

      Shuningdek, siz mehmonlar ixtiyorida mehmonxona xonasini ijaraga olish majburiyatisiz qo'ng'iroq qilishingiz mumkin

      basseyn
      3 ta sauna
      restoran majmuasi
      1 kishi uchun 300 000 so'm, 12 yoshgacha bo'lgan bolalarga bepul. Tashrif 18:00 gacha mavjud.
            ''',
            'ru': '''
            ***В стоимость номеров входит завтрак на 2 персоны. Детям до 3х лет - завтрак бесплатный. Свыше 3х лет - 
         100.000 сум за персону.

     Также можно заехать без обязательства снятия гостиничного номера, в распоряжении гостей

     бассейн
     3 сауны
     ресторанный комплекс
     Стоимость на 1 человека - 300.000 сум, детям до 12 лет бесплатно. Посещение доступно до 18:00.
            ''',
            'en': 'asd'
        },
        '8': {
            'uz': 'Spa',
            'ru': 'Спа',
            'en': 'asd'
        },
        '9': {
            'uz': 'Basseyn',
            'ru': 'Бассейн',
            'en': 'asd'
        },
        '10': {
            'uz': 'Restoran',
            'ru': 'Ресторан',
            'en': 'asd'
        },
        '11': {
            'uz': 'Avvaldan buyurtma bermoq',
            'ru': 'Бронировать',
            'en': 'asd'
        },
        '12': {
            'uz': 'Xonalar',
            'ru': 'Комнаты',
            'en': 'asd'
        },
        '13': {
            'uz': 'Shartlar',
            'ru': 'Условия',
            'en': 'asd'
        },
        '14': {
            'uz': 'Biz haqimizda',
            'ru': 'О нас',
            'en': 'asd'
        },
        '15': {
            'uz': '''
            HEAVENS GARDEN mehmonxonasi 2020 yil 31 avgustda ochilgan, 46 xonadan iborat;
         12 ta yarimlyuks, 4 ta lyuks, 4 ta ekonom va 26 ta standart. Hovuz tashqarida joylashgan va isitiladi.
         Spa fin saunasi va turk hammomdan iborat. Mehmonxonada bepul internet va sun'iy yo'ldoshli televidenie mavjud.
       
            ''',
            'ru': '''
            Гостиница HEAVENS GARDEN открылась 31 августа 2020 года, имеет 46 номеров;  
        12 полулюксов, 4 люкса, 4 эконома и 26 стандарта. Бассейн расположен на улице и имеет подогрев. 
        Спа состоит из Финской сауны и Турецкого хаммама. В гостинице имеется бесплатный интернет а также спутниковое телевидение.
        
            ''',
            'en': 'asd'
        },
        '16': {
            'uz': '''
               Spa ikkita saunadan (fin, turk) va turk hammomdan iborat
                ''',
            'ru': '''
                Спа состоит из двух саун(финская,турецкая) и турецкий хаммам
                ''',
            'en': 'asd'
        },
        '17': {
            'uz': '''
                   Mehmonlar uchun bepul ochiq basseyn Endless pool formatida tayyorlangan va isitish tizimiga ega .
                    ''',
            'ru': '''
                    Бесплатный открытый бассейн для гостей сделан в формате Endless pool и имеет подогрев.
                    ''',
            'en': 'asd'
        },
        '18': {
            'uz': 'bugun',
            'ru': 'Cегодня',
            'en': 'asd'
        },
        '19': {
            'uz': 'ertaga',
            'ru': 'завтра',
            'en': 'asd'
        },
        '20': {
            'uz': 'kalendar',
            'ru': 'календарь',
            'en': 'asd'
        },
        '21': {
            'uz': 'kunni tanlash',
            'ru': 'выберите день',
            'en': 'asd'
        },
        '22': {
            'uz': "Boshlang'ich kunni tanlang",
            'ru': 'Выберите дату начала',
            'en': 'asd'
        },
        '23': {
            'uz': "oxirgi kunni tanlang ",
            'ru': 'выберите последний день',
            'en': 'asd'
        },
        '24': {
            'uz': "Xona olish uchun iltimos shaxsim ma'lumotlaringizni to'ldiring\nTo'liq ismingizni kiriting",
            'ru': 'Чтобы получить номер, введите свои личные данные \nВведите свое полное имя',
            'en': 'asd'
        },
        '25': {
            'uz': "Iltmos to'g'ri telefon raqam kiriting",
            'ru': 'Пожалуйста, введите правильный номер телефона',
            'en': 'asd'
        },
        '26': {
            'uz': "Iltmos to'g'ri email kiriting",
            'ru': 'Пожалуйста, введите правильный адрес электронной почты',
            'en': 'asd'
        },
        '27': {
            'uz': "To'liq ismingizni jo'nating",
            'ru': 'Отправьте свое полное имя',
            'en': 'asd'
        },
        '28': {
            'uz': "Telefon raqamingizni kiriting",
            'ru': 'Введите свой номер телефона',
            'en': 'asd'
        },
        '29': {
            'uz': "Elektron pochtangizni kiriting",
            'ru': 'Введите адрес электронной почты',
            'en': 'asd'
        },
        '30': {
            'uz': "Manzilingizni kiriting",
            'ru': 'Введите ваш адрес',
            'en': 'asd'
        },
        '31': {
            'uz': "Asosiy",
            'ru': 'Базовый',
            'en': 'asd'
        },
        '32': {
            'uz': "Sizning arizangiz Qabul qilindi javobni kuting",
            'ru': 'Ваша заявка принята. Ждите ответа',
            'en': 'asd'
        }

    }

    return language[word][lang]


print(getword('6','uz'))
