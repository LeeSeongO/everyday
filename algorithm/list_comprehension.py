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


def list_comprehension(item):
    if type(item) is list:
        return [n * 2 for n in range(1, 10 + 1) if n % 2 == 1]
    elif type(item) is dict:
        return {key: value + 5 for key, value in item.items()}
