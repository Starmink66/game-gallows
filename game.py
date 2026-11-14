import random
state = {
    "lastLetter": '',
    "active": False,
    "category": False,
    "lastArr": ['♥'],
    "count": 1
}
words = {
    'животные': ['сова', 'олень', 'орел', 'собака', 'ящерица', 'паук', 'лиса', 'муравей', 'крокодил', 'заяц'],
    'еда': ['арбуз', 'шоколад', 'варенье', 'огурец', 'лимонад', 'паста', 'блин', 'стейк', 'мед', 'кунжут'],
    'фэнтези': ['меч', 'дракон', 'щит', 'заклинание', 'замок', 'сокровище', 'гоблин', 'паладин', 'кольчуга', 'единорог'],
    'природа': ['облако', 'снег', 'тропинка', 'ручей', 'дерево', 'камень', 'пурга', 'гроза', 'лист', 'цветок ']
}

messageStart = 'Добро пожаловать в игру "Виселица"! Вы можете выбрать категорию из которой вы будете угадывать слово.'
messageCategory = 'Выберите категорию из перечисленных: животные, еда, фэнтези или природа. '
messageErrCategory = 'Такой категории нет. Выберите категорию из перечисленных: животные, еда, фэнтези или природа.'
messageLetter = 'Введите букву: '
messageStop = 'Жаль, что мы не смогли дойти до конца...'
messageWinner = 'Ура! вам удалось угадать слово!'
messageLoss = 'Как жаль, попытки закончились...'


def printMessage(text):
    print(text)

def printCosole(nameFile):
    file = open("gallows/"+nameFile, 'r')
    print(file.read())

def checkCategory(choice):
    if choice == 'животные' or choice == 'еда' or choice == 'фэнтези' or choice == 'природа':
        return True
    else:
        printMessage(messageErrCategory)
        return False

def chooseCategory(message):
    category = input(message).strip().lower()
    if checkCategory(category):
        state["category"] = True
        return category

def chooseLeter(message):
    letter = input(message).strip().lower()
    if len(letter) == 0 or len(letter) > 1 or letter == ' ':
        print('Ошибка введении буквы! ')
        return None
    return letter

def randomCategory(nameCategory):
    category = words[nameCategory]
    wordIndex = random.randrange(len(category))
    word = category[wordIndex]
    return word

def breakWord(word):
    arrWord = [*word]
    return arrWord

def findLetter(arr, letter):
    index = [i for i, ltr in enumerate(arr) if ltr == letter]
    if index:
        return index
    else:
        return False

def heartLetter(arr):
    length = len(arr)
    heart = breakWord('♥' * length)
    state["lastArr"] = heart
    return heart

def openLetter(arrIndex, letter, heart):
    for i in range(len(arrIndex)):
        item = arrIndex[i]
        heart[item] = letter
    state["lastArr"] = heart
    return heart

def start(message):
    printMessage(message)
    state['active'] = True

def countErr(count):
    if count >= 6:
        return False
    else:
        state["count"] += 1
        return True






#print(openLetter([1], 'т', ['♥', '♥', '♥', '♥', '♥']))
#printCosole('gallows/vis1.txt')