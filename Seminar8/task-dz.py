# Напишите функцию, которая получает на вход директорию и рекурсивно
# обходит её и все вложенные директории. Результаты обхода сохраните в
# файлы json, csv и pickle.
# ○ Для дочерних объектов указывайте родительскую директорию.
# ○ Для каждого объекта укажите файл это или директория.
# ○ Для файлов сохраните его размер в байтах, а для директорий размер
# файлов в ней с учётом всех вложенных файлов и директорий.

__all__ = ['my_func']


import os
import json
import csv
import pickle


def my_func(dir_name, file_json, file_csv, file_pickle):
    files = []
    directories = []
    for dir_path, dir_name, file_name in os.walk(dir_name):
        for elem in file_name:
            files.append({'name': elem, 'size': os.path.getsize(f'{dir_path}\\{elem}'), 'type': 'file',
                          'directory': str(dir_path)})
        if len(dir_name) != 0:
            for elem in dir_name:
                total_size = 0
                for entry in os.scandir(f'{dir_path}\\{elem}'):
                    if entry.is_file():
                        total_size += entry.stat().st_size
                    elif entry.is_dir():
                        total_size += os.path.getsize(entry)
                directories.append({'name': elem, 'size': total_size, 'type': 'directory', 'directory': str(dir_path)})
    all_data = files + directories
    with (open(file_json, 'w', encoding='utf-8') as f_json,
          open(file_csv, 'w', encoding='utf-8', newline='') as f_csv,
          open(file_pickle, 'wb') as f_pickle
          ):
        json.dump(all_data, f_json, ensure_ascii=False, indent=2)

        csv_write = csv.DictWriter(f_csv, fieldnames=['name', 'size', 'type', 'directory'])
        csv_write.writeheader()
        csv_write.writerows(all_data)

        pickle.dump(all_data, f_pickle)


if __name__ == '__main__':
    my_func(r'C:\Users\burah\PycharmProjects\Python-seminars\Seminar8', 'directories.json', 'directories.csv',
            'directories.pickle')
    with open('directories.pickle', 'rb') as f_pickle:
        print(pickle.load(f_pickle))

        