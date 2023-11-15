def bubble_sort(lst):
    for i in range(len(lst)):
        for j in range(len(lst)-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]


def binary_search(lst, target):
    left, right = 0, len(lst) - 1

    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == target:
            return mid  # Элемент найден, возвращаем его индекс
        elif lst[mid] < target:
            left = mid + 1  # Искомый элемент находится справа от mid
        else:
            right = mid - 1  # Искомый элемент находится слева от mid
    return -1


def main():
    lst = [4, 34, 25, 4, 5, 27, 45, 1, 3, 5]
    bubble_sort(lst)
    print(lst)
    print()
    print(binary_search(lst, 27))
    return
 

if __name__ == "__main__":
    main()
