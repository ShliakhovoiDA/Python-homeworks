# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их
# деление. Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на
# ноль.

def division(num1, num2):
    try:
        num1 = int(num1)
        num2 = int(num2)
        div_action = num1 / num2
    except ValueError as err:
        return err
    except ZeroDivisionError as null:
        return null
    return round(div_action, 2)


while True:
    print(division(input('Введите делимое: ') == "Q", input('Введите делитель: ')))
    Quit = (input("Для выхода наберите 'Q': "))
    if Quit == "Q":
        break
    else:
        continue
