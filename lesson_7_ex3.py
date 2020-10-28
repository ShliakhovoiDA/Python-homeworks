class Cell:
    def __init__(self, cell):
        self.cell = cell

    def __str__(self):
        return '(%)' * self.cell

    def __add__(self, other):
        return self.cell + other.cell

    def __sub__(self, other):
        if self.cell < other.cell:
            return other.cell - self.cell
        else:
            return self.cell - other.cell

    def __mul__(self, other):
        return self.cell * other.cell

    def __floordiv__(self, other):
        return self.cell // other.cell

    def make_order(self, rows):
        output = ''
        for i in range(int(self.cell / rows)):
            output += '(%)' * rows + '\n'
        output += '(%)' * (self.cell % rows) + '\n'
        return output


cell_1 = Cell(int(input('Введите целое число для элементов 1-й клетки вируса: \n')))
cell_2 = Cell(int(input('Введите целое число для элементов 2-й клетки вируса: \n')))
print(f'Клетка 1:\n{cell_1.make_order(5)}\n')
print(f'Клетка 2:\n{cell_2.make_order(5)}\n')
print(f'При слиянии двух клеток получилась новая клетка: \n{Cell(cell_1 + cell_2).make_order(5)} '
      f'длиной в {cell_1 + cell_2} элементов.\n')  # 25
print( f'При взаимопоглощении двух клеток получилась новая клетка: \n{Cell(cell_1 - cell_2).make_order(5)} '
       f'длиной в {cell_1 - cell_2} элементов.\n')
print(f'При гиперслиянии двух клеток получилась новая клетка: \n{Cell(cell_1 * cell_2).make_order(5)} '
      f'длиной в {cell_1 * cell_2} элементов.\n')
print(f'При взаимоуничтожении двух клеток получилась новая клетка: \n{Cell(cell_1 // cell_2).make_order(5)} '
      f'длиной в {cell_1 // cell_2} элементов.\n')
