# Напишите функцию группового переименования файлов. Она должна:
# принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
# принимать параметр количество цифр в порядковом номере.
# принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
# принимать параметр расширение конечного файла.
# принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение. 3.Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами.
#
#

__all__ = ['rename_func']

import os


def rename_func(new_name: str, old_extension: str, new_extension: str, dir_name: str):
    dir_list = os.listdir(dir_name)
    for i, item in enumerate(dir_list, 1):
        file_extension = item.split('.')[1]
        if file_extension == old_extension:
            file_name = os.path.join(dir_name, f'{item.split(".")[0]}_{new_name}_{i}.{new_extension}')
            old_name = os.path.join(dir_name, item)
            os.rename(old_name, file_name)


if __name__ == '__main__':
    rename_func('test', 'txt', 'doc', r'C:\Users\burah\PycharmProjects\Python-seminars\Seminar7')