"""Задание 5 (повышенная сложность): игра «Угадай число».

Компьютер загадывает число модулем random, игрок угадывает его
по подсказкам «больше» / «меньше». Число попыток ограничено:
для диапазона из N чисел хватает ceil(log2(N)) + 1 попыток, если
каждый раз называть середину оставшегося отрезка (бинарный поиск).
"""
import math
import random


def attempts_limit(low, high):
    """Сколько попыток даётся на диапазон [low, high].

    >>> attempts_limit(1, 100)
    8
    >>> attempts_limit(1, 1)
    1
    """
    size = high - low + 1
    return math.ceil(math.log2(size)) + 1


def hint(secret, guess):
    """Подсказка игроку: 'больше', 'меньше' или 'угадала'.

    >>> hint(42, 10)
    'больше'
    >>> hint(42, 50)
    'меньше'
    >>> hint(42, 42)
    'угадала'
    """
    if guess < secret:
        return "больше"
    if guess > secret:
        return "меньше"
    return "угадала"


def play(low=1, high=100, secret=None, ask=input):
    """Одна партия; возвращает число попыток или 0 при проигрыше.

    Функция ввода передаётся параметром, чтобы партию можно было
    сыграть автоматически:

    >>> moves = iter(["50", "25", "37", "31", "34"])
    >>> play(1, 100, secret=34, ask=lambda _: next(moves))
    Попытка 1 из 8: загаданное число меньше
    Попытка 2 из 8: загаданное число больше
    Попытка 3 из 8: загаданное число меньше
    Попытка 4 из 8: загаданное число больше
    Угадала за 5 попыток!
    5
    """
    if secret is None:
        secret = random.randint(low, high)
    limit = attempts_limit(low, high)
    tries = 0
    while tries < limit:
        text = ask(f"Число от {low} до {high}: ")
        if not text.strip().lstrip("-").isdigit():
            print("Введите целое число.")
            continue
        tries += 1
        answer = hint(secret, int(text))
        if answer == "угадала":
            print(f"Угадала за {tries} попыток!")
            return tries
        print(f"Попытка {tries} из {limit}: загаданное число {answer}")
    print(f"Попытки закончились, было загадано {secret}.")
    return 0


if __name__ == "__main__":
    wins = 0
    rounds = 0
    again = "д"
    while again.lower().startswith("д"):
        rounds += 1
        if play():
            wins += 1
        again = input("Сыграть ещё? (д/н): ")
    print(f"Партий: {rounds}, побед: {wins}")
