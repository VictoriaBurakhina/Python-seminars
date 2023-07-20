# Нахождение корней квадратного уравнения
# Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
# Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
# Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.

from random import randint as rnd
import csv
import json

LINES = 100
ARGS = 3
MIN_LIMIT = -100
MAX_LIMIT = 100


def rnd_numbers(file_csv):
    my_list = []
    for _ in range(ARGS):
        my_list.append(rnd(MIN_LIMIT, MAX_LIMIT + 1))
    for i in range(LINES):
        for j in range(ARGS):
            my_list[j] = rnd(MIN_LIMIT, MAX_LIMIT + 1)
            if my_list[j] == 0:
                my_list[j] = 1
        with open(file_csv, 'a', encoding='utf-8', newline='') as f:
            csv_write = csv.writer(f, delimiter=' ')
            csv_write.writerow(my_list)


def deco(func):
    _my_dict = {}

    def wrapper(*args):
        a, b, c = args
        x_1, x_2 = func(*args)
        _my_dict[f'{a = }, {b = }, {c = }'] = f'{x_1 = }, {x_2 = }'
        return _my_dict

    return wrapper


def save_json(func):
    def wrapper(*args, **kwargs):
        with open('result.json', 'w', encoding='utf-8') as f:
            res = func(*args, **kwargs)
            json.dump(res, f, ensure_ascii=False, indent=2)

    return wrapper


@save_json
@deco
def get_roots(a, b, c):
    d = b ** 2 - (4 * a * c)
    x_1 = (-b + d ** 0.5) / (2 * a)
    x_2 = (-b - d ** 0.5) / (2 * a)
    return x_1, x_2


if __name__ == '__main__':
    rnd_numbers('args.csv')
    with open('args.csv', 'r', encoding='utf-8') as f:
        csv_read = csv.reader(f, delimiter=' ')
        for line in csv_read:
            a, b, c = map(int, line)
            get_roots(a, b, c)