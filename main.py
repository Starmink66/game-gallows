import game

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
    'природа': ['облако', 'снег', 'тропинка', 'ручей', 'дерево', 'камень', 'пурга', 'гроза', 'лист', 'цветок']
}

messageStart = 'Добро пожаловать в игру "Виселица"! Вы можете выбрать категорию, из которой будете угадывать слово.'
messageCategory = 'Выберите категорию из перечисленных: животные, еда, фэнтези или природа. '
messageErrCategory = 'Такой категории нет. Выберите категорию из перечисленных: животные, еда, фэнтези или природа.'
messageLetter = 'Введите букву: '
messageNoLetter = 'Такой буквы нет, упс...'
messageReLetter = 'Вы уже вводили эту букву.'
messageStop = 'Жаль, что мы не смогли дойти до конца...'
messageWinner = 'Ура! вам удалось угадать слово!'
messageLoss = 'Как жаль, попытки закончились...'


game.start(messageStart)
category = game.chooseCategory(messageCategory)
word = game.randomCategory(category)
arrWord = game.breakWord(word)
arrHeart = game.heartLetter(arrWord)
print(*arrHeart)

while game.state['active'] == True:
    letter = game.chooseLeter(messageLetter)
    if letter is None:
        continue

    if letter == game.state["lastLetter"]:
        game.printMessage(messageReLetter)
        continue
    game.state["lastLetter"] = letter

    if game.findLetter(arrWord, letter):
        arrFindLetter = game.findLetter(arrWord, letter)
        print(*game.openLetter(arrFindLetter, letter, arrHeart))
        stateArr = game.state["lastArr"]
        if game.findLetter(stateArr, '♥'):
            continue
        else:
            game.printMessage(messageWinner)
            break
    else:
        game.printMessage(messageNoLetter)
        stateCount = game.state["count"]
        game.printCosole(f'vis{stateCount}.txt')
        if not game.countErr(stateCount):
            game.printMessage(messageLoss)
            print('Загаданное слово: ', *arrWord)
            break


