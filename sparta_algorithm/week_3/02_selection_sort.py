input = [4, 6, 2, 9, 1]
num = 123
num_list = [1, 2, 3]
# 1. [4, 6, 2, 9, 1]
# 2. [1, 6, 2, 9, 4]

def selection_sort(array):
    n = len(array)

    for i in range(n - 1):
        min_index = i
        for j in range(n - i):
            if array[i + j] < array[min_index]:
                min_index = i + j
        array[i], array[min_index] = array[min_index], array[i]

    return array

def change_sort(number, number_list):
    number = 1
    number_list[0], number_list[1] = number_list[1], number_list[0]
    return number


selection_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!


change_sort(num, num_list)
print(num)
print(num_list)

"""
결론: 리스트로 이루어진 값을 매개로 넘겨서 사용할때
값이 원본도 바뀌기 때문에 주의해야한다./

bubble_sort: 순차적으로 비교해서 맨 뒤 즉, 큰 값을 맨뒤로 정렬하면서 반복 방법
selection_sort: 순차적으로 비교해서 맨 앞 즉, 작은 값을 맨앞으로 정렬하면서 반복하는 방법

"""