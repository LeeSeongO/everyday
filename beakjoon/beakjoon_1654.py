import sys

K, N = map(int, input().split())  # 가지고있는 랜선 개수 K, 필요한 최대 길이의 랜선 개수 N

K_size_list = [int(sys.stdin.readline()) for _ in range(K)]  # 가지고있는 랜선들의 길이 입력

start, end = 1, max(K_size_list)  # 랜선의 최소길이와 최대길이

# 최소길이가 최대길이보다 길어지면 반복종료
while start <= end:
    mid = (start + end) // 2  # 최소길이와 최대길이를 합쳐서 반으로 나누면 중간 길이 생김
    lines = 0  # 만들어낸 랜선을 저장할 변수

    for i in K_size_list:
        lines += (i // mid)  # 랜선 길이를 mid 사이즈로 쪼개서 개수 저장

    # 만들어낸 랜선의 개수와 필요한 랜선의 개수 비교
    if lines >= N:
        start = mid + 1  # 랜선의 최소 길이를 mid + 1
    else:
        end = mid - 1  # 랜선의 최대 길이를 mid - 1

print(end)