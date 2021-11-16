"""
def list_comprehension(item):
    if type(item) is list:
        a = []
        for n in range(1, 10 + 1):
            if n % 2 == 1:
                a.append(n * 2)
        return a

    elif type(item) == dict:
        a = {}
        for key, value in item.items():
            a[key] = value + 5
        return a


풀어서 작성한 코드를 list_comprehension 사용
"""


def list_comprehension(item: list or dict) -> print:
    if type(item) is list:
        a = [n * 2 for n in range(1, 10 + 1) if n % 2 == 1]
        print(a)
    elif type(item) == dict:
        a = {
            "1": 1,
            "2": 2
        }
        a = {key: value + 5 for key, value in a.items()}
        print(a)
        print(list(a))


list_a = []
dict_a = {}
list_comprehension(list_a)
list_comprehension(dict_a)

# 여러 표현식을 여러 줄에 걸쳐 표현하면 가독성이 지나치게 떨어진다.

test = [(x, y, z)
        for x in range(5)
        for y in range(5)
        if x != y
        for z in range(5)
        if y != z
        ]

print(test)