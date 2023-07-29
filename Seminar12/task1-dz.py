# Создайте класс студента.
# Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
# Названия предметов должны загружаться из файла CSV при создании экземпляра.
# Другие предметы в экземпляре недопустимы.
# Для каждого предмета можно хранить оценки (от 2 до 5) и
# результаты тестов (от 0 до 100).
# Также экземпляр должен сообщать средний балл по тестам для каждого предмета
# и по оценкам всех предметов вместе взятых.

from random import randint as rnd
import csv
from statistics import mean


class CheckName:
    def __init__(self, name: str = None):
        self.name = name

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def validate(self, value: str):
        if len(value.split()) < 3:
            raise ValueError(f'Значение {value} должно содержать имя, фамилию и отчество, разделенные пробелом')
        for item in value.split():
            if not item.isalpha():
                raise ValueError(f'Значение {value} должно содержать только буквы')
            if not item.istitle():
                raise ValueError(
                    f'Значение {value} должно содержать имя, фамилию и отчество, начинающиеся с заглавной буквы')


class Student:
    MIN_GRADE = 2
    MAX_GRADE = 5
    MIN_TEST = 0
    MAX_TEST = 100
    name = CheckName()

    def __init__(self, name, file_csv, items_of_grades, items_of_test):
        self.name = name
        self._subjects = {}
        self.items_of_grades = items_of_grades
        self.items_of_test = items_of_test
        with open(file_csv, 'r', encoding='utf-8', newline='') as f:
            csv_read = csv.reader(f)
            for line in csv_read:
                self._subjects[str(line).strip("[]'")] = self.generate_grades(), self.generate_tests()

    def __str__(self):
        return f'{self.name} {self._subjects}'

    @property
    def get_subjects(self):
        return self._subjects

    def generate_grades(self):
        return list(rnd(self.MIN_GRADE, self.MAX_GRADE) for i in range(self.items_of_grades))

    def generate_tests(self):
        return list(rnd(self.MIN_TEST, self.MAX_TEST) for i in range(self.items_of_test))

    def get_average_score_on_tests(self):
        new_dict = {}
        for subject, item in self._subjects.items():
            new_dict[subject] = mean(item[1])
        return new_dict

    def get_overall_average_score(self):
        list_grades = []
        for subject, item in self._subjects.items():
            list_grades.append(mean(item[0]))
        return mean(list_grades)


student_1 = Student('Бурахин Степан Сергеевич', 'subjects.csv', 5, 5)
print(student_1)
print(f'Средний балл по тестам для каждого предмета: {student_1.get_average_score_on_tests()}')
print(f'Средний общий балл по всем предметам: {student_1.get_overall_average_score()}')