array_a = [1, 2, 3, 5]
array_b = [4, 6, 7, 8]


def merge(array1, array2):
    idx_a = 0
    idx_b = 0
    array_c = []

    while idx_a < len(array1) and idx_b < len(array2):
        if array1[idx_a] < array2[idx_b]:
            array_c.append(array1[idx_a])
            idx_a += 1
        else:
            array_c.append(array2[idx_b])
            idx_b += 1

    if idx_a == len(array1):
        for j in range(idx_b, len(array2)):
            array_c.append(array_b[j])
    else:
        for j in range(idx_a, len(array1)):
            array_c.append(array_a[j])

    return array_c

print(merge(array_a, array_b))  # [1, 2, 3, 4, 5, 6, 7, 8] 가 되어야 합니다!