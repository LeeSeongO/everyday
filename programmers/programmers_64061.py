"""
프로그래머스 // 카카오 // 크레인 인형뽑기 게임 // 64061
"""
from typing import List


def solution(board: List[List[int]], moves: List[int]) -> int:
    answer = 0

    # 뽑은 인형 보관
    doll_storage = []

    for move in moves:
        for block in range(len(board)):
            if board[block][move - 1] != 0:
                # 뽑은 인형 보관
                doll_storage.append(board[block][move - 1])
                board[block][move - 1] = 0

                # 1보다 작거나 같을때는 뽑은인형과 비교할 필요가 없다.
                if len(doll_storage) > 1:
                    if doll_storage[-1] == doll_storage[-2]:
                        doll_storage.pop()
                        doll_storage.pop()
                        answer += 2

                break

    return answer


"""
# 위는 개선된 코드.. // 밑의 주석의 코드 같은 경우, 인덱스로 접근해서 값을 바로 비교해서 pop 을 하면 되기때문에 아래 코드 처럼,
# 굳이 뽑은 인형을 다른 변수에 담아 두었다가 마지막에 append 하는 것이 불필요하고, 코드 또한 조금 지저분한 것 같다.
            
# 인형 뽑기
doll_claw = board[block][move - 1]
board[block][move - 1] = 0

# 인형 보관함이 비어있으면 index 오류가 발생함으로 처리, 1 보다 크다로 조건을 주어도 가능.
if len(doll_storage) != 0:
    if doll_storage[-1] == doll_claw:
        doll_storage.pop()
        answer += 2
        break

# 보관함이 0이거나, 보관함 마지막 값과 뽑은 이형이 같지 않을때
doll_storage.append(doll_claw)
break
"""


board_param = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
moves_param = [1, 5, 3, 5, 1, 2, 1, 4]

print(solution(board_param, moves_param))
