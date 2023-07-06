# Задача 1.Напишите функцию для транспонирования матрицы

def process_trans(array):
    for i in range(len(array)):
        for j in range(i, len(array[i])):
            temp = array[i][j]
            array[i][j] = array[j][i]
            array[j][i] = temp
    return array
matrix = [[1, 9, 2, 5, 4], [6, 5, 2, 8, 9], [8, 1, 4, 7, 8], [6, 3, 8, 2, 5], [7, 2, 4, 6, 2]]
for i in matrix:
    print(i)
print()
matrix = process_trans(matrix)
for i in matrix:
    print(i)