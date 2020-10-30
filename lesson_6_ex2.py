class Road:
    def __init__(self, _lenght, _width):
        self._lenght = _lenght
        self._width = _width

    def calc(self):
        print(f"Масса асфальта, необходимого для строительства дороги = "
              f"{self._lenght * self._width * 25 * 5 / 1000} тонн")


def calculation():
    while True:
        try:
            road_1 = Road(int(input("Введите желаемую ширину дорожного полотна в м: ")),
                          int(input("Введите желаемую длину дорожного полотна в м: ")))
            road_1.calc()
            break
        except ValueError:
            print("Только целые числа!")


calculation()
