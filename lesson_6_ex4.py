class Car:

    def __init__(self, name, color, speed, _is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self._is_police = _is_police
        print(f'Новая машина: {self.name} (цвет {self.color}) машина полицейская - {self._is_police}')

    def go(self):
        print(f'{self.name}: Машина поехала.')

    def stop(self):
        print(f'{self.name}: Машина остановилась.')

    def turn(self, direction):
        print(f'{self.name}: Машина повернула {"налево" if direction == 0 else "направо"}.')

    def show_speed(self):
        return f'{self.name}: Скорость автомобиля: {self.speed}.'

    def crash(self):
        return f'Репортаж с места ДТП с участием {self.name}, за рулем которой находился Халиф Абдулмугамедов.\n' \
               f'Очевидцы рассказывают о том, что машина на огромной скорости в {self.speed} км/ч.\n' \
               f'пробила ограждение набережной и вылетела в реку. Водитель скончался от полученных повреждений.'

    def engine_stall(self):
        return f'У автомобиля {self.name} заглох двигатель, водитель выставил знак аварийной остановки и ожидает ' \
               f'эвакуатор '


class TownCar(Car):

    def show_speed(self):
        return f'{self.name}: Скорость автомобиля: {self.speed}. Превышение скорости!' \
            if self.speed > 60 else f"{self.name}: Скорость автомобиля {self.speed}"


class WorkCar(Car):

    def show_speed(self):
        return f'{self.name}: Скорость автомобиля: {self.speed}. Превышение скорости!' \
            if self.speed > 40 else f"{self.name}: Скорость автомобиля {self.speed}"


class SportCar(Car):

    def show_speed(self):
        return f'{self.name}: Скорость автомобиля: {self.speed}. Сильное превышение скорости!' \
            if self.speed > 120 else f"{self.name}: Скорость автомобиля {self.speed}"


class PoliceCar(Car):

    def __init__(self, name, color, speed, _is_police=True):
        super().__init__(name, color, speed, _is_police)


police_car = PoliceCar('Полицейский автомобиль ДПС', 'белый', 100)
police_car.go()
print(police_car.show_speed())
police_car.turn(1)
police_car.stop()
print()

work_car = WorkCar('Портер "Hyndai"', 'серый', 60)
work_car.go()
work_car.turn(0)
print(work_car.show_speed())
work_car.turn(1)
work_car.stop()

print()
sport_car = SportCar('Porshe-GT', 'золотой', 160)
sport_car.go()
sport_car.turn(0)
print(sport_car.show_speed())
print(sport_car.crash())
print()

town_car = TownCar('"Жигули-4"', 'зеленый', 50)
town_car.go()
town_car.turn(1)
town_car.turn(0)
print(town_car.show_speed())
print(town_car.engine_stall())
print()

print(f'\nМашина {town_car.name} (цвет {town_car.color})')
print(f'Машина {police_car.name} (цвет {police_car.color})')
