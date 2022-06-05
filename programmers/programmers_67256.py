"""
프로그래머스 // 카카오 // 키패드 누르기 // 67256
"""

from typing import List


def solution(numbers: List[int], hand: str) -> str:
    answer = ''
    keypad = {
        1: [0, 0], 2: [0, 1], 3: [0, 2],
        4: [1, 0], 5: [1, 1], 6: [1, 2],
        7: [2, 0], 8: [2, 1], 9: [2, 2],
        '*': [3, 0], 0: [3, 1], '#': [3, 2]
    }

    # 손의 위치
    left_hand = keypad['*']
    right_hand = keypad['#']

    for number in numbers:
        if number in [1, 4, 7]:
            answer += 'L'
            left_hand = keypad[number]
        elif number in [3, 6, 9]:
            answer += 'R'
            right_hand = keypad[number]
        else:
            temp_l = abs(keypad[number][0] - left_hand[0]) + abs(keypad[number][1] - left_hand[1])
            temp_r = abs(keypad[number][0] - right_hand[0]) + abs(keypad[number][1] - right_hand[1])

            if temp_l > temp_r:
                answer += 'R'
                right_hand = keypad[number]
            elif temp_l < temp_r:
                answer += 'L'
                left_hand = keypad[number]
            else:
                if hand == 'right':
                    answer += 'R'
                    right_hand = keypad[number]
                else:
                    answer += 'L'
                    left_hand = keypad[number]

    return answer


print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], 'right'))