import sys

# 가지고있는 랜선의 개수 K, 필요한 랜선의 개수 N
K, N = map(int, input().split())
lan_list = [int(sys.stdin.readline()) for _ in range(K)]
start, end = 1, max(lan_list)

while start <= end:  # 랜선의 길이를 찾는 알고리즘
    mid = (start + end) // 2  # 중간 위치  802 401
    lines = 0  # 랜선의 수
    for i in lan_list:
        lines += (i // mid)  # 분할 된 랜선의 수

    if lines >= N:
        start = mid + 1
    else:
        end = mid - 1

print(end)
