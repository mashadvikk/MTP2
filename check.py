"""Проверка всех заданий: запускает doctest-примеры из docstring модулей.

Запуск: python check.py
"""
import doctest

import calc
import guess
import nod
import rec_sum
import squares

MODULES = [nod, calc, squares, guess, rec_sum]

if __name__ == "__main__":
    failed = 0
    total = 0
    for module in MODULES:
        result = doctest.testmod(module)
        failed += result.failed
        total += result.attempted
        status = "OK" if result.failed == 0 else "ОШИБКИ"
        print(f"{module.__name__:<8} примеров: {result.attempted:>2}  "
              f"{status}")
    print(f"Всего примеров: {total}, провалено: {failed}")
    raise SystemExit(1 if failed else 0)
