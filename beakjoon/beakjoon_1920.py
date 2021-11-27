"""
if in으로 해결해도 되지만 그러면
O(n)만큼 시간이 계속 걸리기때문에
이분 탐색법으로 대체 해서 해결한다.
"""


# N 의 크기만큼 N_list 를 선언
N = int(input())
N_list = sorted(list(map(int, input().split())))  # 오름차순으로 N_list 에 저장
# 오름차순으로 정리하는 이유는 이분 탐색법을 사용하기 위해 오름차순으로 정리한다.

# M 의 크기만큼 M_list 를 선언
M = int(input())
M_list = [map(int, input().split())]

start = min(M_list)
end = max(M_list)

for value in M_list:
    while start <= end:
        mid = (start + end) // 2

        if mid > value:
            end = mid - 1
        elif mid < value:
            start = mid + 1








