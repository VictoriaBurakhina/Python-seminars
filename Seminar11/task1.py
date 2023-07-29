

# 1) Создайте класс МояСтрока где будут доступны все возможности str и
# дополнительно хранится имя автора строки и время создания (time.time)

# Добавьте ко всем задачам с семинара строки документации и методы вывода информации на печать.

import time


class MyString(str):
    """The MyString training class."""

    def __new__(cls, *args, **kwargs):
        """Added a super method."""
        instance = super().__new__(cls, args)
        return instance

    def __init__(self, value, name):
        """Added the name and the time parameters."""
        self.value = value
        self.name = name
        self.time = time.time()

    def __str__(self):
        """Class representation for the print method."""
        return f'Строка {self.value} создана {self.name} в {self.time}'


string_1 = MyString('new', name='ann')
print(string_1)
print(string_1.upper())
print(string_1.title())
print(string_1.time)
print(string_1.name)
help(MyString)