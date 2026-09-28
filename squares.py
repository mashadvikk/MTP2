"""Задание 10 (средняя сложность): словарь квадратов чисел.

Словарь строится двумя способами — обычным циклом for и генератором
словаря (dict comprehension); результаты совпадают. Ключ — число,
значение — его квадрат.
"""


def squares_loop(n):
    """Словарь {i: i*i} для i от 1 до n, построенный циклом.

    >>> squares_loop(5)
    {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
    """
    result = {}
    for i in range(1, n + 1):
        result[i] = i * i
    return result


def squares_comprehension(start, stop):
    """Словарь квадратов для чисел из отрезка [start, stop].

    >>> squares_comprehension(-2, 2)
    {-2: 4, -1: 1, 0: 0, 1: 1, 2: 4}
    """
    return {i: i ** 2 for i in range(start, stop + 1)}


def print_squares(squares):
    """Печатает словарь таблицей «число — квадрат»."""
    print(f"{'число':>7} | {'квадрат':>8}")
    print("-" * 18)
    for number, square in squares.items():
        print(f"{number:>7} | {square:>8}")


if __name__ == "__main__":
    d = squares_loop(10)
    print_squares(d)
    print("Совпадает с генератором словаря:",
          d == squares_comprehension(1, 10))
    print("Сумма квадратов 1..10:", sum(d.values()))
