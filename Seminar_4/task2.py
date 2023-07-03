# Задача 2. Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, где ключ — значение переданного аргумента, а значение — имя аргумента. Если
# ключ не хешируем, используйте его строковое представление.

def some_function(**args):
    my_dict = {}
    for key, value in args.items():
        #key = value
        if value.__hash__ == None:
            value = str(value)
        my_dict[value] = key
    return my_dict

print(some_function(x = 324, y ='Function', z = 45.23, g =[3, 8, 2, 3, 9], e = {45, 23, 67}, l = (5, 9, 2, 4, 5)))