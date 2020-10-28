class Clothes:
    def __init__(self, parameter):
        self.parameter = parameter


class Coat(Clothes):
    def __init__(self, height):
        super().__init__(self)
        self.__height = height

    @property
    def calculation(self):
        return int(self.height) / 6.5 / 100 + 0.5

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if height < 120:
            print("Минимальный рост для расчета 120 см.")
            self.__height = 120
        elif height > 220:
            print("Максимальный рост для пошива в нашей компании 220 см.")
            self.__height = 220
        else:
            self.__height = height


class Suit(Clothes):
    def __init__(self, size):
        super().__init__(self)
        self.__size = size

    @property
    def calculation(self):
        return int(self.size) * 2 / 100 + 0.3

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if size < 34:
            print("Минимальный размер для расчета - 34.")
            self.__size = 34
        elif size > 56:
            print("Максимальный размер для пошива костюма в нашей компании - 56.")
            self.__size = 56
        else:
            self.__size = size


while True:
    a = input("Введите необходимый рост в сантиметрах для рассчета материала на пошив пальто (для выхода введите "
              "'quit'): ")
    b = input("Введите необходимый размер для рассчета материала на пошив костюма (для выхода введите 'quit'): ")

    if a != "quit" or b != "quit":
        a = Coat(a)
        b = Suit(b)
        try:
            print(f"{round(a.calculation, 2)}")
            print(f"{round(b.calculation, 2)}")
            print(f"{round((a.calculation + b.calculation), 2)}")
        except ValueError:
            print("Необходимо вводить числовой параметр.")
    else:
        print("До свидания! Будем рады видеть Вас снова")
        break
