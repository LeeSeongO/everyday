"""
프로그래머스 // 월간 코드 챌린지 // 없는 숫자 더하기 // 86051
"""
from typing import List


def solution(numbers: List[int]) -> int:
    answer = 0

    for number in range(1, 10):
        if number not in numbers:
            answer += number

    return answer


print(solution([1, 2, 3, 4, 6, 7, 8, 0]))
