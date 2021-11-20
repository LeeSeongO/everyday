import pygame

pygame.init()  # 초기화(반드시 필요)

# 화면 크기 설정
screen_width = 1200  # 가로 길이
screen_height = 960  # 세로 길이
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Nado game")  # 게임 이름 설정

# FPS(frame_per_second)
clock = pygame.time.Clock()

# 배경 이미지 불러오기
background = pygame.image.load("/Users/leesungo/PycharmProjects/everyday/pygame_basic/pygame_background.png/background.png")

# 캐릭터(스프라이트) 불러오기
character = pygame.image.load("/Users/leesungo/PycharmProjects/everyday/pygame_basic/character.png")
character_size = character.get_rect().size  # 이미지의 크기를 가져옴
character_width = character_size[0]  # 캐릭터의 가로 크기
character_height = character_size[1]   # 캐릭터의 세로 크기
character_x_pos = (screen_width / 2) - (character_width / 2)  # 화면 가로의 절반 크기에 해당하는 곳에 위치
character_y_pos = screen_height - character_height  # 화면 세로 크기 가장 아래에 해당하는 곳에 위치

# 이동할 좌표
to_x = 0
to_y = 0

# 이동 속도
character_speed = 0.3

# 적 enemy 캐릭터
enemy = pygame.image.load("/Users/leesungo/PycharmProjects/everyday/pygame_basic/enemy.png")
enemy_size = character.get_rect().size  # 이미지의 크기를 가져옴
enemy_width = enemy_size[0]  # 캐릭터의 가로 크기
enemy_height = enemy_size[1]   # 캐릭터의 세로 크기
enemy_x_pos = (screen_width / 2) - (enemy_width / 2)  # 화면 가로의 절반 크기에 해당하는 곳에 위치
enemy_y_pos = (screen_height / 2) - (enemy_height / 2) - 100 # 화면 세로 크기 가장 아래에 해당하는 곳에 위치

# 폰트 정의
game_font = pygame.font.Font(None, 40)  # 폰트 객체 생성 (폰트, 크기)

# 총 시간
total_time = 10

# 시작 시간
start_ticks = pygame.time.get_ticks() # 시작 tick을 받아옴


# Game Loop
running = True
while running:
    dt = clock.tick(60) # 게임화면의 초당 프레임 수를 설정

    # 캐릭터가 1초 동안에 100만큼 이동을 해야할때, 즉 프레임별로 이동거리가 달라져야 같은 동작을 할 수 있다.
    # 10 fps : 1초 동안에 10번 동작 -> 1번에 10만큼이동
    # 20 fps : 1초 동안에 20번 동작 -> 1번에 5만큼이동

    # fps 체크
    # print("fps : " + str(clock.get_fps()))


    for event in pygame.event.get():    # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT:   # 창이 닫히는 이벤트가 발생하였는가?
            running = False # 게임이 진행중이 아님

        if event.type == pygame.KEYDOWN:    # 키가 눌렸는지 확인
            if event.key == pygame.K_LEFT:   # 캐릭터를 왼쪽
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:  # 캐릭터를 오른쪽
                to_x += character_speed
            elif event.key == pygame.K_UP:    # 캐릭터를 위로
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:  # 캐릭터를 아래
                to_y += character_speed

        if event.type == pygame.KEYUP: # 방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    # 캐릭터 이동거리와 * dt를 곱해주면 같은 속도를 유지 할 수 있다.
    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    # 가로 경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # 세로 경계값 처리
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    # 충돌 처리를 위한 rect 정보 업데이트
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

    screen.fill((100, 100, 50))  # 배경 그리기
    # screen.blit(background, (0, 0))  # 배경 그리기
    screen.blit(character, (character_x_pos, character_y_pos))  # 캐릭터 그리기
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))  # 적 캐릭터 그리기

    # 타이머 집어 넣기
    # 경과 시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
    # 경과 시간(ms)을 1000으로 나누어서 초(s) 단위로 표

    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255, 255, 255))
    # 출력할 글자, True, 글자 색상
    screen.blit(timer, (10, 10))

    # 만약 시간이 0 이하이면 게임 종료
    if total_time - elapsed_time <= 0:
        print("타임아웃")
        running = False

    pygame.display.update()  # 게임화면을 다시 그리기!

# 잠시 대기
pygame.time.delay(2000)  # 2초 정도 대기(ms)

# pygame 종료
pygame.quit()