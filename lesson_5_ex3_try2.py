with open("employees.txt", "r", encoding="utf-8") as file:
    try:
        employees_dict = {line.split()[0]: float(line.split()[1]) for line in file}
        print(f"Средняя зарплата составляет {round(sum(employees_dict.values()) / len(employees_dict), 2)}\n"
              f"Сотрудники с зарплатой меньше 20000: {[e[0] for e in employees_dict.items() if e[1] < 20000]}")
    except IndexError:
        print("Сломалось....")
# попробовал многое, но работать не хочет
# Traceback (most recent call last):
#   File "C:/Users/admin/PycharmProjects/Project1/lesson 5/lesson_5_ex3_try2.py", line 2, in <module>
#     employees_dict = {(line.split()[0]): float(line.split()[1]) for line in file}
#   File "C:/Users/admin/PycharmProjects/Project1/lesson 5/lesson_5_ex3_try2.py", line 2, in <dictcomp>
#     employees_dict = {(line.split()[0]): float(line.split()[1]) for line in file}
# IndexError: list index out of range
