# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ - значение переданного аргумента, а значение - имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.
from collections.abc import Hashable


def function(**kwargs):
    dict = {}
    for key, value in kwargs.items():
        if not isinstance(value, Hashable):
            value = str(value)
        dict[value] = key
    return dict


print(function(a = 5, b = 7, c = [1, 2]))