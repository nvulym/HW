test_list = [-2, -1, 2, 3, 5, 5, 5, 5, 10, 15, 15]
a = 6
b = 15

def binary_search(array, value):
    mid = 0  # индекс среднего элемента
    left = 0
    right = len(array) - 1

    while left <= right:
        mid = (left + right) // 2  # индекс среднего элемента отрезка от left до right, разделенного на 2 части
        if value == array[0]:
            return 0
        elif value > array[-1]:
            raise ValueError
        elif value > array[mid]:  # если value больше, то игнорируем левую половину
            left = mid + 1
        elif value == array[mid]:  # если value равно половине
            if value > array[mid - 1]:  # то сравниваем value со значением левее половины / если значение больше
                return mid  # то значение value существует, возвращаем индекс среднего элемента
            right = mid - 1  # значение меньше, игнорируем правую половину
        elif value < array[mid]:  # если value меньше, то игнорируем правую половину
            right = mid - 1
    if left > right:
        raise ValueError
    else:
        return mid

print(binary_search(test_list, a))  # ValueError
print(binary_search(test_list, b))  # 9
