from random import randint

with open('lesson_5_ex5.txt', 'w+', encoding='utf-8') as new_file:
    new_file.write(" ".join([str(randint(1, 100000)) for i in range(500)]))
    new_file.seek(0)
    print(f"Сумма чисел, записанных в файле {new_file.name} составляет {sum(map(int, new_file.readline().split()))}.")
