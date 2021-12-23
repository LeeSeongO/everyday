input = [3, 5, 6, 1, 2, 4]


def find_max_num(array):
    array_max = array[0]
    for number in array:
        if array_max < number:
            array_max = number
    return array_max


result = find_max_num(input)
print(result)