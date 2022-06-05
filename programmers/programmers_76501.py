"""
프로그래머스 // 월간 코드 챌린지 // 음양 더하기 // 76501
"""

from typing import List


def solution(absolutes: List[int], signs: List[bool]) -> int:
    answer = 0

    for absolute, sign in zip(absolutes, signs):
        answer += absolute if sign else -absolute

    return answer


absolutes_temp = [4, 7, 12]
signs_temp = [True, False, True]

print(solution(absolutes_temp, signs_temp))

