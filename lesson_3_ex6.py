# наша функция готова сразу принимать предложения из этих слов
#
# тестовое предложение: nice авп ъghj jапро hjjпаро вапрghgh cool

def int_func() -> object:
    for word in input('Введите через пробел слова, используя только латинницу: \n ').split():
        characters = 0
        for character in word:
            if 97 <= ord(character) <= 122:
                characters += 1
        print(word.title() if characters == len(word) else f"{word} - к ответу принимаются только малые латинские символы")

int_func()