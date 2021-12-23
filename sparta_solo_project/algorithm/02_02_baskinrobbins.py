"""
1부터 31까지의 숫자를 플레이어와 컴퓨터가 번갈아 가면서 순서대로 말합니다. 숫자를 말할 때는 1개부터 3개까지의 연속된 숫자를 말할 수 있습니다.
즉, 처음 시작하는 사람이 무조건 1 혹은 1, 2 혹은 1, 2, 3을 말하면서 시작하고, 그 뒷 사람은 앞 사람이 말한 숫자에 이어서 또 1개\~3개의 연속된 숫자를 차례대로 말하는 방식입니다. (앞 사람이 3까지 불렀다면, 뒷 사람은 4 혹은 4, 5 혹은 4, 5, 6을 말해야 합니다.) 그렇게 해서 31을 부르는 사람이 지는 게임입니다.

- **[상세설명]**

1. 컴퓨터가 먼저 숫자를 말할지, 플레이어가 먼저 숫자를 말할지는 랜덤으로 정한다.

2. 컴퓨터 혹은 플레이어는 1 혹은 1, 2 혹은 1, 2, 3을 말하면서 게임을 시작한다.
(단, 컴퓨터가 숫자를 1개 부를지, 2개 부를지, 3개 부를지는 random 패키지를 이용해서 랜덤으로 정한다.
플레이어는 input 함수를 통해서 연속해서 부르고 싶은 숫자 개수를 입력한다.)

3. 컴퓨터 혹은 플레이어는 앞 사람이 부른 숫자에 이어서, 1개~3개까지의 연속된 숫자를 말한다.

4. 2\~3번을 31을 말하는 사람이 나올 때까지 반복한다. (즉, 2\~3번을 for문 혹은 while문으로 작성할 것.
단, 컴퓨터와 플레이어 모두 31을 초과해서 숫자를 부를 수는 없다.)

5. 31을 말하는 사람이 컴퓨터라면 '플레이어 승'을, 31을 말하는 사람이 플레이어라면 '컴퓨터 승'을 출력한다.

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
    range_max = 4
    if (current_br + 3) > 31:
        range_max = 31 - current_br + 1

    return random.randrange(1, range_max)

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
