finding_target = 17
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


def is_existing_target_number_binary(target, array):
    # 구현해보세요!
    start = array[0]
    end = array[-1]

    while start <= end:
        mid = (start + end) // 2

        if target == mid:
            return True
        elif target > mid:
            start = mid + 1
        else:
            end = mid - 1

    return False

result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)

