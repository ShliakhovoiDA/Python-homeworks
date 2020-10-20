from itertools import count

x = int(input('Введите целое число, до которого будет происходить генерирование: '))
for i in count(1, 1):
    if i > x:
        break
    else:
        print(i)


from itertools import cycle

z = 0
y = int(input('Введите целое число повторений, до которого будет происходить генерирование: '))
for i in cycle('ЖуК'):
    if z > y:
        break
    print(i)
    z += 1
