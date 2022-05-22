"""
프로그래머스 힙(Heap) 이중우선순위큐 42628
"""

import heapq
from typing import List


def solution(operations: List[str]) -> List[int]:
    answer = [0] * 2
    min_heap, max_heap = [], []

    for op in operations:
        # 명령어와 숫자를 분리
        temp = op.split()

        # 숫자의 min, max 를 구하기 위해 temp[1] int 형으로 형변환
        temp[1] = int(temp[1])

        # 명령어 확인
        if temp[0] == 'I':
            heapq.heappush(min_heap, temp[1])
            heapq.heappush(max_heap, [temp[1] * -1, temp[1]])
        else:
            if len(min_heap):
                # 최댓값 삭제
                if temp[1] == 1:
                    heapq.heappop(max_heap)
                    min_heap.pop()
                # 최솟값 삭제
                elif temp[1] == -1:
                    heapq.heappop(min_heap)
                    max_heap.pop()

    if len(min_heap):
        answer[0], answer[1] = max_heap[0][1], min_heap[0]

    return answer


print(solution(	["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))