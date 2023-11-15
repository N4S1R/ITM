# 5. Словари


def task_1():
    return {'name': "Насир", 'age': 22, 'sex': 'man', 'height': 180, 'weight': 67, 'foot_size': 43}


def task_2(dct):
    for i in dct:
        print(i, dct[i])


def task_3(dct):
    dct['foot_size'] = 44


def task_4(dct):
    dct.pop('height')


def main():
    # 1. Создайте словарь содержащий данные о человеке. В качестве строковых ключей используйте его имя, возраст, пол, рост, вес, размер ноги.
    dct = task_1()
    print(dct)

    # 2. Выведите на экран все данные о человеке по ключам.
    task_2(dct)

    # 3. Добавьте в словарь ключ и значение размера ноги ?
    task_3(dct)
    print(dct)

    # 4. Удалите из словаря возраст.
    task_4(dct)
    print(dct)


if __name__ == "__main__":
    main()
