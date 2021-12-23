finding_target = 10
finding_numbers = [0, 3, 5, 6, 1, 2, 4]

def is_exist_target_number_binary(target, numbers):
    num_list = sorted(numbers)

    start = num_list[0]
    end = num_list[-1]

    while start <= end:
        mid = (start + end) // 2

        if target == mid:
            print(mid)
            return True

        elif target > mid:
            start = mid + 1

        elif target < mid:
            end = mid -1

    return False

result = is_exist_target_number_binary(finding_target, finding_numbers)
print(result)