# Прочитайте созданный в прошлом задании csv файл без
# использования csv.DictReader.
# Распечатайте его как pickle строку.

import csv
import pickle


def my_func(file_csv, file_pkl):
    with open(file_csv, 'r', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        all_data = []
        keys = []
        for i, item in enumerate(spamreader):
            my_dict = {}
            if i == 0:
                keys = item
            else:
                for j, elem in enumerate(item):
                    my_dict[keys[j]] = elem
            if len(my_dict) != 0:
                all_data.append(my_dict)
    with open(file_pkl, 'wb') as pkl:
        res = pickle.dump(all_data, pkl)
        print(f'{res = }')


if __name__ == '__main__':
    my_func('data.csv', 'data.pkl')
