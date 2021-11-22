"""Quiz) 하늘에서 떨어지는 똥 피하기 게임을 만드시오


[게임 조건]
1. 캐릭터는 화면 가장 아래에 위치, 좌우로만 이동 가능
2. 똥은 화면 가장 위에서 떨어짐. X 좌표는 매번 랜덤으로 설정
3. 캐릭터가 똥을 피하면 다음 똥이 다시 떨어짐
4. 캐릭터가 똥과 충돌하면 게임 종료
5. FPS 는 30 으로 고정

[게임 이미지]
1. 배경 : 640 * 480 (세로 가로) - background.png
   Mac 그림판어플에서 최소 크기로 생성이 300 * 300이기 때문에 캐릭터 이미지가 300 * 300 이어서 배경을 더 넓게 처리함
2. 캐릭터 : 70 * 70 - character.png
   300 * 300 대체
3. 똥 : 70 * 70 - enemy.png
   300 * 300 대체

"""
import random

import pygame

pygame.init()  # 초기화(반드시 필요)

# 화면 크기 설정
screen_width = 1200  # 가로 길이
screen_height = 960  # 세로 길이
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Quiz Game")  # 게임 이름 설정

# FPS(frame_per_second)
clock = pygame.time.Clock()

# 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 폰트 등)
# 배경화면
background = pygame.image.load("/Users/leesungo/PycharmProjects/everyday/pygame_basic/pygame_background.png/background.png")

# 캐릭터 이미지 불러오기 및 설정
character = pygame.image.load("/Users/leesungo/PycharmProjects/everyday/pygame_basic/character.png")
character_size = character.get_rect().size  # 캐릭터 이미지 정보를 가져오는 함수 get_rect()에서 크기를 가져옴.
character_width = character_size[0]  # 캐릭터의 가로 크기 저장
character_height = character_size[1]  # 캐릭터의 세로 크기 저장

# 캐릭턱 위치할 좌표 설정
character_x_pos = (screen_width / 2) - (character_width / 2)  # 캐릭터가 위치할 x위치 저장
character_y_pos = screen_height - character_height  # 캐릭터가 위치할 y위치 저장

character_speed = 0.3

character_to_x = 0

# 적 이미지 불러오기 및 설정
enemy = pygame.image.load("/Users/leesungo/PycharmProjects/everyday/pygame_basic/enemy.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]

# Quiz 2번 조건
enemy_x_pos = random.randrange(0, screen_width - enemy_width)
enemy_y_pos = 0

enemy_speed = 0.1


running = True
while running:
    # Quiz 5번째 조건
    dt = clock.tick(30)  # 게임화면의 초당 프레임 수를 설정

    # 캐릭터가 1초 동안에 100만큼 이동을 해야할때, 즉 프레임별로 이동거리가 달라져야 같은 동작을 할 수 있다.
    # 10 fps : 1초 동안에 10번 동작 -> 1번에 10만큼이동
    # 20 fps : 1초 동안에 20번 동작 -> 1번에 5만큼이동

    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get():    # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT:   # 창이 닫히는 이벤트가 발생하였는가?
            running = False  # 게임이 진행중이 아님

    # 1. 게임 캐릭터 위치 정의 // 좌우로만 움직이기때문에 좌우만 설정해줌
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            character_to_x -= character_speed
        elif event.key == pygame.K_RIGHT:
            character_to_x += character_speed

        # 키보드에서 손을 떼면
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_to_x = 0


    # 프레임이 바뀌어도 dt와 이동속도를 곱해주면 같은 속도를 유지해 줄 수 있다.
    character_x_pos += character_to_x * dt

    # Quiz 조건 3
    if enemy_y_pos >= screen_height:
        enemy_y_pos = 0
        enemy_x_pos = random.randrange(0, screen_width - enemy_width)

    enemy_y_pos += enemy_speed * dt

    # 가로 경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # 4. 충돌 처리를 위한 rect 정보 업데이트
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    # 충돌 체크
    if character_rect.colliderect(enemy_rect):
        print("충돌했어요")
        running = False

    # 배경 그리기
    screen.fill((100, 100, 50))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))

    # 5. 화면 그리기
    pygame.display.update()  # 게임화면을 다시 그리기!

# pygame 종료
pygame.quit()