"""
프로그래머스 // 카카오 // 키패드 누르기 // 67256
"""

from typing import List


def solution(numbers: List[int], hand: str) -> str:
    answer = ''
    keypad = {
        1: [0, 0], 2: [1, 0], 3: [2, 0],
        4: [0, 1], 5: [1, 1], 6: [2, 1],
        7: [0, 2], 8: [1, 2], 9: [2, 2],
        '*': [0, 3], 0: [1, 3], '#': [2, 3]
    }

    answer = ''

    left_p = keypad['*']
    right_p = keypad['#']

    for n in numbers:
        if n in [1, 4, 7]:
            answer += 'L'
            left_p = keypad[n]
        elif n in [3, 6, 9]:
            answer += 'R'
            right_p = keypad[n]
        else:
            left_d = 0
            right_d = 0

            target = keypad[n]

            left_d = abs(left_p[0] - target[0]) + abs(left_p[1] - target[1])
            right_d = abs(right_p[0] - target[0]) + abs(right_p[1] - target[1])

            if left_d < right_d:
                answer += 'L'
                left_p = keypad[n]
            elif left_d > right_d:
                answer += 'R'
                right_p = keypad[n]
            else:
                if hand == 'left':
                    answer += 'L'
                    left_p = keypad[n]
                else:
                    answer += 'R'
                    right_p = keypad[n]

    return answer


print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], 'right'))