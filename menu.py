"""Главное меню: запуск любого задания лабораторной №2 (вариант 4)."""
import calc
import guess
import nod
import rec_sum
import squares


def task_nod():
    a = nod.ask_int("Первое число: ")
    b = nod.ask_int("Второе число: ")
    print("НОД =", nod.nod(a, b))


def task_squares():
    n = nod.ask_int("До какого числа строить словарь: ")
    squares.print_squares(squares.squares_loop(n))


def task_rec_sum():
    n = nod.ask_int("n = ")
    if n > 900:
        print("Слишком большое n для рекурсии (предел около 1000).")
        return
    print(f"1 + ... + {n} = {rec_sum.rec_sum(n)}")
    print("По формуле Гаусса:", rec_sum.gauss(n))


def main():
    while True:
        print("\nЛабораторная №2, вариант 4")
        print("1 - НОД двух чисел")
        print("2 - калькулятор")
        print("3 - словарь квадратов")
        print("4 - игра «Угадай число»")
        print("5 - рекурсивная сумма")
        print("0 - выход")
        choice = input("> ").strip()
        if choice == "1":
            task_nod()
        elif choice == "2":
            calc.main()
        elif choice == "3":
            task_squares()
        elif choice == "4":
            guess.play()
        elif choice == "5":
            task_rec_sum()
        elif choice == "0":
            print("До свидания!")
            break
        else:
            print("Нет такого пункта.")


if __name__ == "__main__":
    main()
