"""
프로그래머스 // 월간 코드 챌린지 // 내적 // 70128
"""
from typing import List


def solution(a: List[int], b: List[int]) -> int:
    answer = 0

    for i, j in zip(a, b):
        answer += i * j

    return answer


print(solution([1, 2, 3, 4], [-3, -1, 0, 2]))
