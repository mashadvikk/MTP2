"""Задание 4 (средняя сложность): НОД двух чисел.

НОД находится методом последовательного вычитания: из большего числа
вычитается меньшее, пока числа не сравняются. Этот вариант алгоритма
Евклида обходится без деления и хорошо показывает работу цикла while.
Результат сверяется со стандартной функцией math.gcd.
"""
import math


def nod(a, b):
    """Наибольший общий делитель двух целых чисел.

    >>> nod(48, 18)
    6
    >>> nod(17, 5)
    1
    >>> nod(-12, 30)
    6
    >>> nod(0, 7)
    7
    """
    a, b = abs(a), abs(b)
    if a == 0 or b == 0:
        return a + b
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


def nod_many(numbers):
    """НОД нескольких чисел: НОД(a, b, c) = НОД(НОД(a, b), c).

    >>> nod_many([84, 126, 210])
    42
    """
    result = 0
    for number in numbers:
        result = nod(result, number)
    return result


def ask_int(prompt):
    """Запрашивает целое число, пока пользователь не введёт корректно."""
    while True:
        text = input(prompt)
        if text.strip().lstrip("-").isdigit():
            return int(text)
        print("Нужно целое число, попробуйте ещё раз.")


if __name__ == "__main__":
    x = ask_int("Первое число: ")
    y = ask_int("Второе число: ")
    print(f"НОД({x}, {y}) = {nod(x, y)}")
    print(f"Проверка math.gcd: {math.gcd(x, y)}")
