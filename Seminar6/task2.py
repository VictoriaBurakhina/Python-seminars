# Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код, решающий задачу о 8 ферзях.
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга. Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга. Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей. Если ферзи не бьют друг друга верните истину, а если бьют - ложь.
# Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше. Проверяйте различный случайные варианты и выведите 4 успешных расстановки.


from itertools import permutations as perm, combinations_with_replacement as comb, combinations


def check_queen(coordinates: list) -> bool:
    for item in coordinates:
        print(item)
        for j in range(coordinates.index(item) + 1, len(coordinates)):
            # проверка диагоналей, затем горизонтали и вертикали
            if item[0] - item[1] == coordinates[j][0] - coordinates[j][1] or \
                    item[0] + item[1] == coordinates[j][0] + coordinates[j][1] or \
                    item[0] == coordinates[j][0] or item[1] == coordinates[j][1]:
                return False
            else:
                return True


def generator_and_print():
    i = 1
    variants = sorted(my_coordinates)
    for item in combinations(variants, 8):
        if check_queen(item):
            print(f'{i}: {item}')
            i += 1


my_coordinates = [[1, 2], [2, 5], [6, 3], [4, 8], [1, 5], [6, 7], [8, 7], [8, 9]]
print(check_queen(my_coordinates))

if __name__ == '__main__':
    generator_and_print()
