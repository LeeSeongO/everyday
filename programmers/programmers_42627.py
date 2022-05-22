"""
문제. 디스크 컨트롤러 / 42627
"""

from typing import List
from collections import deque
import heapq


def solution(jobs: List[List[int]]) -> int:
    answer = 0
    ms_time = 0
    # 작업을 처리한 횟수
    process_count = 0

    # 요청 시간이 정렬
    jobs.sort()
    jobs_deque = deque(jobs)

    # 대기중인 작업 넣을 공간
    wait_work = []

    while process_count < len(jobs):
        # 대기중인 작업 큐에 담기
        for _ in range(len(jobs_deque)):
            if ms_time >= jobs_deque[0][0]:
                temp = jobs_deque.popleft()
                heapq.heappush(wait_work, [temp[1], temp[0]])
            else:
                break

        if len(wait_work):
            current_work = heapq.heappop(wait_work)
            # 요청부터 종료까지 ms_time
            answer += ms_time - current_work[1] + current_work[0]
            ms_time += current_work[0]
            process_count += 1
        else:
            ms_time += 1

    return answer // process_count


temp_list = [[0, 10], [4, 10], [15, 2], [5, 11]]
print(solution(temp_list))
