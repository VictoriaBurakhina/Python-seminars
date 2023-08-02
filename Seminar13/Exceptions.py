class MyException(Exception):
    pass


class FactorialException(MyException):
    def __init__(self, stop):
        self.stop = stop

    def __str__(self):
        return f'Ошибка! Программа считает только факториал положительного числа! {self.stop} не положительное число'


class TypeException(MyException):
    def __init__(self, item):
        self.item = item

    def __str__(self):
        return f'Ошибка! Тип {self.item} должен быть int, а не {type(self.item)}'


class MyStopIteration(MyException):
    def __init__(self, stop):
        self.stop = stop

    def __str__(self):
        return f'Вы достигли конца итерации {self.stop}'