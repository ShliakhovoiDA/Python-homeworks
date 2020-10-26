def task():
    rates = {}
    try:
        with open("new_text.txt", encoding="utf-8") as file:
            for line in file:
                rates[line.split()[0]] = float(line.split()[1])
        print("Меньше 20000.00 получают: ")
        for name, rate in rates.items():
            if rate < 20000:
                print(name)
        print(f"Средняя зарплата сотрудника составляет: {sum(rates.values()) / len(rates)}. \n"
              f"Эх, справедливая же у нас система начисления выплат! Гордость берет!")
    except IOError:
        print("Все сломалось")


task()
