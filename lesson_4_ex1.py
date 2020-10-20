from sys import argv

name, salary_hour, hours, bonus = argv

print('File name: ', name)
print('Введите суммы оплаты труда за 1 час : ', salary_hour)
print('Введите количество отработанных часов : ', hours)
if float(hours) >= 168:                                     # Около 168 часов положено работнику по ТК ежемесячно
    print('Размер премии сотрудника в процентах: ', bonus)
    print(f'Заработная плата сотрудника составляет '
          f'{(int(hours) * int(salary_hour)) + int(bonus) * int(hours) * int(salary_hour) / 100} р. '
          f', из которых {bonus} % - премия (в рублях = {int(bonus) * int(hours) * int(salary_hour) / 100}) ')
else:
    print(f"Заработная плата сотрудника составляет {int(hours) * int(salary_hour)} р."
          f" Премию в этом месяце не заслужил! ")