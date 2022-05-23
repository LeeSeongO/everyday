"""
프로그래머스 - 정렬 - 가장큰 수 - 42746
"""

from typing import List


def solution(numbers: List[int]) -> str:
    # join 후 int 로 다시 형변환 하는 이유는 예외적인 0으로만 이루어져있을 경우를 처리
    # 조건에 따라 numbers의 원소는 0이상 1000이하 이기때문에 자릿수를 맞춰주기 위해 x*3 처리를 한후 정렬해준다.
    # 원소의 수가 더 커지면 디테일하게 자릿수를 맞춰주어야 할 것 같다.
    return str(int("".join(sorted(map(str, numbers), reverse=True, key=lambda x: x*3))))

print(solution([6, 10, 2]))
