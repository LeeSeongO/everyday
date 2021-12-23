import sys

"""
이진탐색을 사용하는 이유는 반복문을 반으로 줄일 수 있다. O(logN)
이잔탐색을 사용하지 않는 경우에는 모든 값을 반복해야 하기 때문에 O(N)만큼의 시간복잡도를 가진다.
"""


K, N = map(int, input().split())  # 가지고있는 랜선 개수 K, 필요한 최대 길이의 랜선 개수 N

K_size_list = [int(sys.stdin.readline()) for _ in range(K)]  # 가지고있는 랜선들의 길이 입력


# end 즉, 최대값에 모든 길이를 더해서 / 필요한 갯수를 나눈 값을 저장하는게 이상적임
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
"""
중간 길이로 모든 랜선을 자른 개수를 확인했는데
필요한 개수보다 적다. 그러면 최대값을 중간길이 -1 를 최대 길이에 저장
다시 사이클을 돌려서
start 값과 바뀐 최대값을 더해서 중간 길이를 다시 구함
바뀐 중간길이를 다시 랜선들을 잘라본다.
이번엔 길이가 남는다.
"""

