class Clothes:
    def __init__(self, parameter):
        self.parameter = parameter

    @property
    def coat(self):
        return f"Для изготовления пальто необходимо {round((float(self.parameter) / 6.5 + 0.5), 3)} единиц ткани"

    @property
    def suit(self):
        return f"Для изготовления костюма необходимо {round((float(self.parameter) * 2 + 0.3), 3)} единиц ткани"


while True:
    a = input("Введите необходимый размер или рост для рассчета материала изделия: ")
    if a != "quit":
        a = Clothes(a)
        try:
            print(a.coat)
            print(a.suit)
        except ValueError:
            print("Необходимо вводить числовой параметр.")
    else:
        print("До свидания! Будем рады видеть Вас снова")
        break

