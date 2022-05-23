"""
프로그래머스 / 정렬 / H-Index / 42747
"""

from typing import List


def solution(citations: List[int]) -> int:
    answer = len(citations)

    # n번 이상 인용된 논문을 찾기위해 내림 차순으로 정렬한다.
    reverse_citations = sorted(citations, reverse=True)

    for i in range(len(reverse_citations)):
        if i + 1 > reverse_citations[i]:
            return i

    return answer


print(solution([3, 0, 6, 1, 5]))