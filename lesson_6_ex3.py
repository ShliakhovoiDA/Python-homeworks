class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"profit": wage, "bonus": bonus}


class Position(Worker):

    @property
    def get_name(self):
        return f"{self.name} {self.surname}"

    @property
    def get_income(self):
        return f"{round(sum(self._income.values()), 2)}"


employee = Position(input("Введите имя сотрудника: "), input("Введите фамилию сотрудника: "),
                    input("Введите должность сотрудника: "), float(input("Введите зарплату сотрудника: ")),
                    float(input("Введите размер премии сотрудника: ")))
print(employee.get_name)
print(employee.position)
print(employee.get_income)
