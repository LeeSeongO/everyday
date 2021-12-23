input = "hello my name is sparta"


def find_max_occurred_alphabet(string):

    arr_string = [0] * 26

    for char in string:
        if char.isalpha():
            arr_index = ord(char) - ord('a')
            arr_string[arr_index] += 1

    arr_max = arr_string[0]
    arr_max_index = 0

    for i, num in enumerate(arr_string):
        if num > arr_max:
            arr_max = num
            arr_max_index = i

    return chr(arr_max_index + ord('a'))


result = find_max_occurred_alphabet(input)
print(result)