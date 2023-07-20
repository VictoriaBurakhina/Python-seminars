# Возьмите любую из задач с прошлых семинаров (например сериализация данных),
# которые вы уже решали. Превратите функции в методы класса, а параметры в свойства.
# Задачи должны решаться через вызов методов экземпляра.

import csv
import json
import pickle


class WorkWithCsv:
    def __init__(self, file_name):
        self.file_name = file_name

    def write_from_json_to_csv(self, file_json):
        with (open(file_json, 'r', encoding='utf-8') as f_read,
              open(self.file_name, 'w', encoding='utf-8', newline='') as f_write
              ):
            json_dict = json.load(f_read)
            my_list = []
            for level, in_dict in json_dict.items():
                for id_person, name in in_dict.items():
                    my_list.append({'id': id_person, 'level': int(level), 'name': name})

            csv_write = csv.DictWriter(f_write, fieldnames=['id', 'level', 'name'])
            csv_write.writeheader()
            csv_write.writerows(my_list)

    def write_from_pickle_to_csv(self, file_pickle):
        with (open(file_pickle, 'rb') as f_read,
              open(self.file_name, 'w', newline='', encoding='utf-8') as f_write
              ):
            new_dict = pickle.load(f_read)
            csv_write = csv.DictWriter(f_write, fieldnames=['id', 'level', 'name'],
                                       dialect='excel-tab', quoting=csv.QUOTE_ALL)
            csv_write.writeheader()
            csv_write.writerows(new_dict)

    def print_csv_to_pickle_string(self):
        with open(self.file_name, 'r', newline='') as f_read:
            csv_read = csv.reader(f_read)
            all_data = []
            keys = []
            for i, item in enumerate(csv_read):
                my_dict = {}
                if i == 0:
                    keys = item
                else:
                    for j, elem in enumerate(item):
                        my_dict[keys[j]] = elem
                if len(my_dict) != 0:
                    all_data.append(my_dict)
            res = pickle.dumps(all_data, protocol=pickle.DEFAULT_PROTOCOL)
            print(f'{res = }')


f_1 = WorkWithCsv('file_1.csv')
f_2 = WorkWithCsv('file_2.csv')
f_1.write_from_pickle_to_csv('user.pickle')
f_2.write_from_json_to_csv('file.json')
f_1.print_csv_to_pickle_string()
f_2.print_csv_to_pickle_string()