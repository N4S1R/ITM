# Часть 1. Все входные и выходные данные в заданиях этой группы являются вещественными числами.

pi = 3.14


def task_10(a: float, b: float):
    return (a**2) + (b**2), (a**2) - (b**2), (a**2) * (b**2), (a**2) / (b**2)


def task_9(a: float, b: float):
    return (a * b) ** 0.5


def task_8(a: float, b: float):
    return (a + b)/2


def task_7(r: float):
    return 2 * pi * r, pi * r ** 2


def task_6(a: float, b: float, c: float):
    return a * b * c, 2 * (a * b + b * c + a * c)


def task_5(a: float):
    return a ** 3, 6 * a ** 2


def task_4(d: float):
    return pi * d


def task_3(a: float, b: float):
    return a * b, 2 * (a + b)


def task_2(a: float):
    return a ** 2


def task_1(a: float):
    return 4 * a


def main():

    # 1. Дана сторона квадрата a. Найти его периметр P = 4·a
    # square_a = float(input('Введите сторону квадрата: '))
    square_a = 23.0
    perimeter = task_1(square_a)
    print(f"\n1.  Периметр квадрата стороной {square_a} = {perimeter:.4f}")

    # 2. Дана сторона квадрата a. Найти его площадь S = a2
    square = task_2(square_a)
    print(f"\n2.  Площадь квадрата со стороной {square_a} = {square:.4f}")

    # 3. Даны стороны прямоугольника a и b. Найти его площадь S = a·b и периметр P = 2·(a + b)
    # rec_a, rec_b = map(float, input('Введите 2 стороны прямоугольника: ').split())
    rec_a, rec_b = 32.0, 42.0
    square_rec, perimeter_rec = task_3(rec_a, rec_b)
    print(
        f"\n3.  Площадь прямоуголника со сторонами {rec_a}, {rec_b}  = {square_rec:.4f}")
    print(
        f"    Периметр прямоуголника со сторонами {rec_a}, {rec_b} = {perimeter_rec:.4f}")

    # 4. Дан диаметр окружности d. Найти ее длину L = π·d, π = 3.14
    # diametr = float(input("Введите диаметр окружности: "))
    diametr = 27.0
    circle_len = task_4(diametr)
    print(f"\n4.  Длина окружности диаметром {diametr} = {circle_len:.4f}")

    # 5. Дана длина ребра куба a. Найти объем куба V = a3 и площадь его поверхности S = 6·a2
    # cub_a = float(input("Введите длину ребра куба: "))
    cub_a = 21.0
    cub_vol, cub_square = task_5(cub_a)
    print(f"\n5.  Объём куба стороной {cub_a} = {cub_vol:.4f}")
    print(
        f"    Площадь всей поверхности куба стороной {cub_a} = {cub_square:.4f}")

    # 6. Даны длины ребер a, b, c прямоугольного параллелепипеда. Найти его объем V = a·b·c и площадь поверхности S = 2·(a·b + b·c + a·c)
    # a, b, c = map(float, input("Введите длину рёбер прямоугольного параллелeпипеда: ").split())
    a, b, c = 2.0, 5.0, 4.0
    rec_vol, rec_square = task_6(a, b, c)
    print(
        f"\n6.  Объём прямоугольного параллелепипеда со сторонами {a, b, c} = {rec_vol:.4f}")
    print(
        f"    Площадь всей поверхности прямоугольного параллелепипеда со сторонами {a, b, c} = {rec_square:.4f}")

    # 7. Найти длину окружности L и площадь круга S заданного радиуса R: L = 2·π·R, S = π·R2, π=3.14
    # circle_r = float(input("Введите радиус окружности: "))
    circle_r = 27.0
    circle_len, circle_square = task_7(circle_r)
    print(f"\n7.  Длина окружности радиусом {circle_r} = {circle_len:.4f}")
    print(f"    Площадь круга радиусом {circle_r} = {circle_square:.4f}")

    # 8. Даны два числа a и b. Найти их среднее арифметическое: (a + b)/2
    # num_a, num_b = map(float, input("Введите 2 числа для нахождения среднего арифметического этих чисел: ").split())
    num_a, num_b = 23.9, 42.34
    arit_mean = task_8(num_a, num_b)
    print(
        f"\n8.  Среднее арифметическое чисел {num_a} и {num_b}  = {arit_mean:.4f}")

    # 9. Даны два неотрицательных числа a и b. Найти их среднее геометрическое, т. е. квадратный корень из их произведения (a·b)1/2
    # num_a, num_b = map(float, input("Введите 2 числа для нахождения среднего геометрического этих чисел: ").split())
    num_a, num_b = 5.0, 5.0
    geom_mean = task_9(num_a, num_b)
    print(
        f"\n9.  Среднее геометрическое чисел {num_a} и {num_b}  = {geom_mean:.4f}")

    # 10. Даны два ненулевых числа. Найти сумму, разность, произведение и частное их квадратов
    # num_a, num_b = map(float, input("Введите 2 не нулевых числа : ").split())
    num_a, num_b = 2.2, 2.5
    sum_ab, diff_ab, prod_ab, quot_ab = task_10(num_a, num_b)
    print(f"\n10. Сумма квадратов чисел {num_a} и {num_b} = {sum_ab:.4f}")
    print(f"    Разность квадратов чисел {num_a} и {num_b} = {diff_ab:.4f}")
    print(
        f"    Произведение квадратов чисел {num_a} и {num_b} = {prod_ab:.4f}")
    print(f"    Частное квадратов чисел {num_a} и {num_b} = {quot_ab:.4f}")


if __name__ == "__main__":
    main()
