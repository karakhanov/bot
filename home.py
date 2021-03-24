import random

def exe1():
    films = [
        "Тихоокеанский рубеж 2",
        "Тихое место",
        "Лига справедливости",
        "Человек-паук: Вдали от дома",
        "Тетрадь смерти",
        "Люди в чёрном: Интернэшнл",
        "Zомбилэнд: Контрольный выстрел",
        "Чудо-женщина",
        "Монстры на каникулах 3: Море зовёт",
        "Мумия",
        "Трансформеры: Последний рыцарь",
        "Оно",
        "Босс-молокосос",
        "Ма",
        "Отряд самоубийц",
        "Варкрафт",
        "До встречи с тобой",
        "Восемь подруг Оушена",
        "Люди Икс: Апокалипсис",
        "Форсаж 8",
        "Малыш на драйве",
        "Великая стена",
        "Спасатели Малибу"
    ]
    print('A)')
    for i in films:
        print(i)
    print('b)')
    for i, val in enumerate(films):
        i = i +1
        print("{0:<35}".format(val), end=' ')
        if i % 3 ==0:
            print()
    print('\nV)')
    for val in films:
        print(val+', ', end='') 

def exe2():
    print('Нажмите Enter, чтобы закончить')
    names = []
    while True:
        a = input('write a name: ')
        if a == '':
            break
        names.append(a)
    names = sorted(names)
    for i in names:
        print(i)

def exe3():
    num1 = random.randint(-1000,1000)
    num2 = random.randint(-1000,1000)
    num3 = random.randint(-1000,1000)
    num4 = random.randint(-1000,1000)
    num5 = random.randint(-1000,1000)
    
    print(num1,num2,num3,num4,num5)
    print('sum = ',num1+num2+num3+num4+num5)

def exe4():
    numbs = []
    for i in range(10):  
        numbs.append(random.randint(-1000,1000))
    for i in numbs:
        print(i)
    print('max = ',max(numbs))

def exe5():
    numbs = []
    for i in range(10):  
        numbs.append(random.randint(1,1000))
    for i in numbs:
        print(i)

    for i in range(len(numbs)-1):
        if numbs[i] % 2 == 1:
            numbs[i] = 0
    print('-----------')
    for i in numbs:
        print(i)

def exe6():
    numbs = []
    for i in range(10):  
        numbs.append(random.randint(-100,100))
    for i in numbs:
        if i >0:
            print(i)
    for i in numbs:
        if i <0:
            print(i)
    for i in numbs:
        if i ==0:
            print(i)

def exe7():
    a = []
    b = []
    for i in range(10):  
        a.append(random.randint(0,10))
    for i in a:
        if i < 5:
            b.append(i)
    print('A massive')
    for i in a:
        print(' ',i)
    print('B massive')
    for i in b:
        print(' ',i)

# domashniye zadaniya

def dom1():
    song = [
        "The Weeknd - Save Your Tears (Official Music Video)",
        "Olivia Rodrigo - drivers license (Official Video)",
        "Bruno Mars, Anderson .Paak, Silk Sonic - Leave the Door Open [Official Video]",
        "BRELAND - Cross Country (Music Video)",
        "Maroon 5 - Beautiful Mistakes ft. Megan Thee Stallion (Official Music Video)",
        "DJ Snake & Selena Gomez - Selfish Love (Official Video)",
        "L.L.A.M.A, Ne-Yo, Carmen DeLeon - Shake",
        "Imagine Dragons - Follow You (Official Music Video)",
        "Waterparks - Snow Globe (Official Music Video)",
        "Tee Grizzley - Robbery Part Two [Official Video]"
    ]
    song = sorted(song)
    for i in song:
        print(i)

def dom2():
    numbs = []
    for i in range(10):  
        numbs.append(random.randint(-1000,1000))
    for i in numbs:
        print(i)
    print('min = ',min(numbs))

def dom3():
    numbs = []
    summin = 0
    for i in range(5):  
        numbs.append(random.randint(-100,100))
    for i in numbs:
        print(i)
        if i < 0:
            summin += i
    if summin != 0:
        print('sum = ',summin)
    else:
        print('отрицательних елементов нет')

dom3()