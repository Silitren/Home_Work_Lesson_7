class Matrix:
    def __init__(self, my_list):
        self.my_list = my_list

    def __str__(self):
        for row in self.my_list:
            for el in row:
                print(f"{el:4}", end="")
            print()
        return ''

    def __add__(self, other):
        for el in range(len(self.my_list)):
            for el2 in range(len(other.my_list[el])):
                self.my_list[el][el2] = self.my_list[el][el2] + other.my_list[el][el2]
        return Matrix.__str__(self)


m = Matrix([[-1, 0, 1], [-1, 0, 1], [0, 1, -1], [1, 1, -1]])
new_m = Matrix([[-2, 0, 2], [-2, 0, 2], [0, 2, -2], [2, 2, -7]])
print(m.__add__(new_m))