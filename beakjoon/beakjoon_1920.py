"""
if in으로 해결해도 되지만 그러면
O(n)만큼 시간이 계속 걸리기때문에
이분 탐색법으로 대체 해서 해결한다.
"""


# N 의 크기만큼 N_list 를 선언
N = int(input())
N_list = [map(int, input().split())]

# M 의 크기만큼 M_list 를 선언
M = int(input())
M_list = [map(int, input().split())]

# M_list 있는 값 하나씩 꺼내서 N_list 에 있는지 확인
for item in M_list:
    if item in N_list:
        print("1")
    else:
        print("0")