class Stationery:
    def __init__(self, title="Выберите пишущие принадлежности!"):
        self.title = title

    def draw(self):
        print(f"Начинаем рисовать! {self.title} :))) ")


class Pen(Stationery):
    def draw(self):
        print(f"Рисуем тонкой ручкой {self.title}!")


class Pencil(Stationery):
    def draw(self):
        print(f"Давайте теперь возьмем мягикий карандаш {self.title}!")


class Marker(Stationery):
    def draw(self):
        print(f"Нарисуем агитационный плакат толстым маркером {self.title}!")


stat = Stationery()
stat.draw()
pen = Pen("Паркер")
pen.draw()
pencil = Pencil("Полёт")
pencil.draw()
marker = Marker("ПОБЕДА")
marker.draw()
