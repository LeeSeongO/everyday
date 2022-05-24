"""
프로그래머스 / 완전 탐색 / 42840
"""

from typing import List


def solution(answers: List[int]) -> List[int]:
    result = []

    peoples = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]

    # 수포자별 정답 맞은 갯수
    math_test = [0] * len(peoples)

    for answer_index, answer in enumerate(answers):
        for people_index, people in enumerate(peoples):
            # 규칙이 있는 답안을 반복하기 위해서 나머지 값을 사용
            if answer == people[answer_index % len(people)]:
                math_test[people_index] += 1

    most_hit = max(math_test)

    # 정답을 모두 맞추지 못했을 경우 예외 처리
    if most_hit != 0:
        result = [i + 1 for i in range(len(math_test)) if math_test[i] == most_hit]

    return result


print(solution([4, 5, 4, 2, 1]))