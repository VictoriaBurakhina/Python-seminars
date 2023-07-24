# Создайте класс Матрица. Добавьте методы для: - вывода на печать,
# сравнения,
# сложения,
# *умножения матриц

from random import randint as rnd


class Matrix:
    min_value = 1
    max_value = 20

    def __init__(self, columns, rows):
        self.columns = columns
        self.rows = rows
        self.list_matrix = [[rnd(self.min_value, self.max_value) for i in range(self.columns)] for i in range(self.rows)]

    def __str__(self):
        # txt = ''
        # for i in range(len(self.list_matrix)):
        #     for j in range(len(self.list_matrix[i])):
        #         txt += f'{self.list_matrix[i][j]} '
        #     txt += '\n'
        # return txt
        return '\n'.join(' '.join(map(str, line)) for line in self.list_matrix)

    def __eq__(self, other):
        return self.list_matrix == other.list_matrix

    def __add__(self, other):
        if self.rows == other.rows and self.columns == other.columns:
            res = [[self.list_matrix[i][j] + other.list_matrix[i][j] for j in range(self.columns)] for i in
                   range(self.rows)]
            matrix_c = Matrix(self.columns, self.rows)
            matrix_c.list_matrix = res
            return matrix_c
        else:
            return 'Можно складывать только матрицы одинаковой размерности'

    def __mul__(self, other):
        if self.columns == other.rows:
            res = [[sum(self.list_matrix[i][k] * other.list_matrix[k][j] for k in range(self.columns))
                    for j in range(other.columns)] for i in range(self.rows)]
            matrix_c = Matrix(self.columns, self.rows)
            matrix_c.list_matrix = res
            return matrix_c
        else:
            return 'Для операции умножения количество столбцов матрицы A должно совпадать с количеством строк матрицы B'

    @classmethod
    def from_two_stage_list(cls, two_stage_list: list[list]):
        columns = len(two_stage_list[0])
        rows = len(two_stage_list)
        new = Matrix(columns, rows)
        new.list_matrix = two_stage_list
        return new


my_matrix = Matrix(2, 2)
print(my_matrix.list_matrix)
print(my_matrix)
my_matrix_2 = Matrix.from_two_stage_list([[2, 2], [3, 4]])
print()
print(my_matrix_2)
print(my_matrix == my_matrix_2)
new_matrix = my_matrix + my_matrix_2
print(new_matrix)
my_matrix_3 = Matrix(1, 2)
print(my_matrix + my_matrix_3)
my_matrix_2.list_matrix = my_matrix.list_matrix
print(my_matrix == my_matrix_2)
print(my_matrix)
print(my_matrix_3)
print(my_matrix * my_matrix_3)
my_matrix_3 = Matrix(1, 1)
print(my_matrix * my_matrix_3)