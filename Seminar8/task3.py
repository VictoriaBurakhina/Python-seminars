# Напишите
# функцию, которая
# сохраняет
# созданный
# в
# прошлом
# задании
# файл
# в
# формате
# CSV.
# Задача 3#

import csv
import json
import os




def my_func(file_json, file_csv):
    with (open(file_json, 'r', encoding='utf-8') as f_read,
          open(file_csv, 'w', encoding='utf-8') as f_write
          ):
        json_dict = json.load(f_read)
        my_list = []
        for level, in_dict in json_dict.items():
            for id_person, name in in_dict.items():
                my_list.append({'id': id_person, 'level': int(level), 'name':name})

        csv_write = csv.DictWriter(f_write, fieldnames=['id', 'level', 'name'], dialect='excel-tab')
        csv_write.writeheader()
        csv_write.writerows(my_list)


if __name__ == '__main__':
    my_func('file.json', 'data.csv')


