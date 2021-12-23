"""
앞서 본 게임과 규칙은 동일하지만, 이번에는 플레이어가 어떤 식으로 숫자를 부르든,
컴퓨터는 항상 자신이 이기도록 나름의 방식의 가지고 숫자를 부릅니다.
(그 방식이 무엇인지는 검색을 해보아도 좋고, 직접 생각해보셔도 좋습니다. *'항상'이라고 명시했지만, 딱 한 가지 경우에는 컴퓨터가 질 수도 있습니다.)

- **[상세설명]**

1. 컴퓨터가 먼저 숫자를 말할지, 플레이어가 먼저 숫자를 말할지는 랜덤으로 정한다.

2. 기존의 게임과 마찬가지로 1부터 순서대로 연속된 숫자를 말하되,
플레이어는 input 함수를 통해서 부르고 싶은 숫자까지 이어서 말한다. 컴퓨터는 나름의 방식을 가지고 숫자를 말한다.

3. 2번 과정을 31을 말하는 사람이 나올 때까지 반복한다.
(즉, 2번을 for문 혹은 while문으로 작성할 것. 단, 컴퓨터와 플레이어 모두 31을 초과해서 숫자를 부를 수는 없다.)

4. 31을 말하는 사람이 컴퓨터라면 '플레이어 승'을, 31을 말하는 사람이 플레이어라면 '컴퓨터 승'을 출력한다.
(단, 컴퓨터는 자신이 항상 이기도록 나름의 방식을 가지고 숫자를 부르기 때문에, 딱 한 가지 경우를 제외하고는 항상 컴퓨터가 이길 수 밖에 없을 것임에 유의)

(가능하다면, 컴퓨터가 숫자를 뽑는 코드와 플레이어가 숫자를 뽑는 코드는 함수화를 해보세요!)
"""


import random


def people_turn(current_br):
    my_turn = int(input('제거 할 만큼의 범위 입력: '))

    while True:
        if not(0 < my_turn <= 3) and (current_br + my_turn) > 31:
            my_turn = int(input(f'입력 숫자 + {current_br}(현재 숫자)가 31초과 하지않는 1~3 입력해주세요>'))
        elif not(0 < my_turn <= 3):
            my_turn = int(input(f'제거할 범위 1~3 사이의 수를 입력해주세요>'))
        elif (current_br + my_turn) > 31:
            my_turn = int(input(f'입력값 + {current_br}(현재 숫자)가 31초과 하지않는 숫자를 입력해주세요>'))
        else:
            return my_turn

def computer_turn(current_br):
    answer = current_br % 4

    if answer == 2:
        range_max = 4
        if (current_br + 3) > 31:
            range_max = 31 - current_br + 1
        return random.randrange(1, range_max)
    elif answer == 0:
        return 2
    elif answer == 1:
        return 1
    elif answer == 3:
        return 3

player_list = ['people', 'computer']
turn = random.choice(player_list)
br = 0
count = 0

print(f'먼저 할 플레이어 뽑기: {turn}')

while True:
    breaker = False
    if turn == 'people':
        count = people_turn(br)
    else:
        count = computer_turn(br)

    for _ in range(count):
        br += 1
        print(f'{turn}: {br}')
        if br > 30:
            breaker = True
            break

    if turn == 'people':
        turn = 'computer'
    else:
        turn = 'people'

    if breaker:
        break

print(f'{turn} 승리!')
