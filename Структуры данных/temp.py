def funk_sum(num: float, num1: float):
    print('Summa obichnaya', num + num1)
    print()
    num = str(num).split('.')
    num1 = str(num1).split('.')

    num_drob = int(num[1])
    num1_drob = int(num1[1])

    if len(num[1]) < len(num1[1]):
        num_drob = int(num[1]) * 10 ** (len(num1[1]) - len(num[1]))

    elif len(num[1]) > len(num1[1]):
        num1_drob = int(num1[1]) * 10 ** (len(num[1]) - len(num1[1]))

    drob = num_drob + num1_drob
    cel = int(num[0]) + int(num1[0])

    if len(str(drob)) > max(len(num[1]), len(num1[1])):
        drob -= 10 ** (len(str(drob)) - 1)
        cel += 1
    num = float(str(cel) + "." + str(drob))
    print('Summa funkci', num, '\n')
    return num


def main():
    # Использование литерала b перед строкой
    byte_str = b'hello'
    print(byte_str)
    # Использование функции bytes()
    byte_str = bytes([104, 101, 108, 108, 111])

    print(byte_str)
    #    funk_sum(23.2, 52.23023)
    # Использование функции bytearray()
    byte_arr = bytearray([104, 101, 108, 108, 111])
    print(byte_arr)
    # Изменение значения по индексу
    byte_arr[0] = 65  # Заменить 'h' на 'A'
    print(byte_arr)


if __name__ == "__main__":
    main()
