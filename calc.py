"""Задание 6 (средняя сложность): калькулятор.

Калькулятор с меню: пользователь выбирает действие по номеру и вводит
два числа. Выбор действия сделан цепочкой if/elif/else — это основная
конструкция ветвления структурного программирования.
"""
import math

ACTIONS = """
1 - сложение          5 - возведение в степень
2 - вычитание         6 - процент (x % от y)
3 - умножение         7 - квадратный корень из x
4 - деление           0 - выход"""


def calculate(action, x, y=0.0):
    """Выполняет действие по его номеру и возвращает результат.

    >>> calculate("1", 2, 3)
    5
    >>> calculate("4", 7, 2)
    3.5
    >>> calculate("6", 15, 200)
    30.0
    >>> calculate("7", 16)
    4.0
    >>> calculate("4", 1, 0)
    Traceback (most recent call last):
    ...
    ZeroDivisionError: на ноль делить нельзя
    """
    if action == "1":
        return x + y
    elif action == "2":
        return x - y
    elif action == "3":
        return x * y
    elif action == "4":
        if y == 0:
            raise ZeroDivisionError("на ноль делить нельзя")
        return x / y
    elif action == "5":
        return x ** y
    elif action == "6":
        return x * y / 100
    elif action == "7":
        if x < 0:
            raise ValueError("корень из отрицательного числа не определён")
        return math.sqrt(x)
    else:
        raise ValueError(f"нет действия с номером {action}")


def read_number(prompt):
    """Читает число с плавающей точкой; запятая тоже допускается."""
    while True:
        text = input(prompt).replace(",", ".")
        try:
            return float(text)
        except ValueError:
            print("Это не число.")


def main():
    count = 0
    while True:
        print(ACTIONS)
        action = input("Действие: ").strip()
        if action == "0":
            break
        if action not in "1234567" or len(action) != 1:
            print("Такого действия нет.")
            continue
        x = read_number("x = ")
        y = 0.0 if action == "7" else read_number("y = ")
        try:
            result = calculate(action, x, y)
        except (ZeroDivisionError, ValueError) as error:
            print("Ошибка:", error)
        else:
            count += 1
            print("Результат:", round(result, 6))
    print("Выполнено вычислений:", count)


if __name__ == "__main__":
    main()
