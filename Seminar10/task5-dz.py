# Создайте три (или более) отдельных классов животных. Например рыбы, птицы и т.п.
# У каждого класса должны быть как общие свойства, например имя, так и специфичные для класса.
# Для каждого класса создайте метод, выводящий информацию специфичную для данного класса.

# 📌Доработайте задачу 5.
# 📌Вынесите общие свойства и методы классов в класс Животное.
# 📌Остальные классы наследуйте от него.
# 📌Убедитесь, что в созданные ранее классы внесены правки.
class Animals:
    def __init__(self, name, tail):
        self.name = name
        self.tail = tail


class Fish(Animals):
    def __init__(self, deep, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.deep = deep

    def specific(self):
        if self.deep < 5:
            return 'Мелководная'
        elif 5 < self.deep < 20:
            return 'Среднеглубинная'
        return 'Глубоководная'


class Birds(Animals):
    def __init__(self, wingspan, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.wingspan = wingspan

    def specific(self):
        wing_length = self.wingspan * 0.45
        return wing_length


class Mammals(Animals):
    def __init__(self, hibernate, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.hibernate = hibernate

    def specific(self):
        if self.hibernate:
            return 'Впадает в спячку'
        return 'Не впадает в спячку'


if __name__ == '__main__':
    dog = Mammals(False, 'Собака', True)
    print(f'Название: {dog.name}, хвост: {dog.tail}, спячка: {dog.specific()}')

    swan = Birds(4, 'Лебедь', True)
    print(f'Название: {swan.name}, хвост: {swan.tail}, длина крыла: {swan.specific()}')

    shark = Fish(15, 'Акула', True)
    print(f'Название: {shark.name}, хвост: {shark.tail}, глубина обитания: {shark.specific()}')