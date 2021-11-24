"""
지민이는 자신의 저택에서 MN개의 단위 정사각형으로 나누어져 있는 M×N 크기의 보드를 찾았다. 어떤 정사각형은 검은색으로 칠해져 있고, 나머지는 흰색으로 칠해져 있다.
지민이는 이 보드를 잘라서 8×8 크기의 체스판으로 만들려고 한다. 체스판은 검은색과 흰색이 번갈아서 칠해져 있어야 한다.
구체적으로, 각 칸이 검은색과 흰색 중 하나로 색칠되어 있고, 변을 공유하는 두 개의 사각형은 다른 색으로 칠해져 있어야 한다.
따라서 이 정의를 따르면 체스판을 색칠하는 경우는 두 가지뿐이다. 하나는 맨 왼쪽 위 칸이 흰색인 경우, 하나는 검은색인 경우이다.
보드가 체스판처럼 칠해져 있다는 보장이 없어서, 지민이는 8×8 크기의 체스판으로 잘라낸 후에 몇 개의 정사각형을 다시 칠해야겠다고 생각했다.
당연히 8*8 크기는 아무데서나 골라도 된다. 지민이가 다시 칠해야 하는 정사각형의 최소 개수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N과 M이 주어진다. N과 M은 8보다 크거나 같고, 50보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에는 보드의 각 행의 상태가 주어진다. B는 검은색이며, W는 흰색이다.

출력
첫째 줄에 지민이가 다시 칠해야 하는 정사각형 개수의 최솟값을 출력한다.
"""


# BW, WB로 시작하는 패턴의 값을 비교하는 함수
def BW_WB_min_cnt(row, column: int) -> int:
    bw_cnt = 0
    wb_cnt = 0
    for i in range(8):
        for j in range(8):
            if value[row + i][column + j] != BW[i][j]:
                bw_cnt += 1
            if value[row + i][column + j] != WB[i][j]:
                wb_cnt += 1
    return min(bw_cnt, wb_cnt)

# 최솟값결과를 저장하는 변수
answer = 12345

# 비교할 정답 만들기 BW로 시작하는 정답, WB로 시작하는 정답
BW = [0 for _ in range(8)]
WB = [0 for _ in range(8)]

for i in range(8):
    if i % 2 == 0:
        BW[i] = list(map(str, "BWBWBWBW"))
        WB[i] = "W B W B W B W B".split()
    else:
        BW[i] = "W B W B W B W B".split()
        WB[i] = "B W B W B W B W".split()

# N = 행, M = 열
# while True:
#     N, M = map(int, input().split())
#     if not (8 <= N <= 50 and 8 <= M <= 50):
#         N, M = map(int, input("N과 M값은 8보다 크거나 같고, 50보다 작거나 같은 자연수를 입력해주세요> ").split())
#         print(N, M)
#         break

N, M = map(int, input().split())

# 사용자에게 입력을 받을 value 을 리스트형태로 선언
value = []

for _ in range(N):
    value.append(list(map(str, input())))

# 8 * 8로 분리하기 위해서 -8을 해주고 8 * 8 일때 최소 한번은 체크해야되기때문에 + 1 해준다
for i in range(N - 8 + 1):
    for j in range(M - 8 + 1):
        tmp = BW_WB_min_cnt(i, j)
        if answer > tmp:
            answer = tmp


print(answer)