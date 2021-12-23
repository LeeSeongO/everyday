input = [4, 6, 2, 9, 1]


def bubble_sort(array):
    n = len(array)

    for j in range(n - 1):
        for i in range(n - i - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]

    return array


input_sort = bubble_sort(input)
print(input_sort)  # [1, 2, 4, 6, 9] 가 되어야 합니다!
