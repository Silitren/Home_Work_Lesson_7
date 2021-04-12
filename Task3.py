class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __add__(self, other):
        return f'Сложение! Размер клетки равен: {self.quantity + other.quantity}'

    def __sub__(self, other):
        subtraction = self.quantity - other.quantity
        return f'Вычитание! теперь она равна: {subtraction}'

    def __truediv__(self, other):
        try:
            delen = self.quantity // other.quantity
            return f"Деление! Размер клетки равен: {delen}"
        except ZeroDivisionError:
            f"На ноль делить нельзя!"

    def __mul__(self, other):
        return f"Умножение! Размер клетки равен: {self.quantity * other.quantity}"

    def make_order(self, row):
        result = ''
        for el in range(int(self.quantity / row)):
            result += '*' * row + '\n'
        result += '*' * (self.quantity % row) + '\n'
        return result


cell = Cell(48)
cell_2 = Cell(6)
print(cell + cell_2)
print(cell - cell_2)
print(cell / cell_2)
print(cell * cell_2)
print(cell.make_order(10))