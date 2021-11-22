import pygame

pygame.init()  # 초기화(반드시 필요)

# 화면 크기 설정
screen_width = 1200  # 가로 길이
screen_height = 960  # 세로 길이
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("first game")  # 게임 이름 설정

# FPS(frame_per_second)
clock = pygame.time.Clock()

# 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 폰트 등)

running = True
while running:
    dt = clock.tick(30) # 게임화면의 초당 프레임 수를 설정

    # 캐릭터가 1초 동안에 100만큼 이동을 해야할때, 즉 프레임별로 이동거리가 달라져야 같은 동작을 할 수 있다.
    # 10 fps : 1초 동안에 10번 동작 -> 1번에 10만큼이동
    # 20 fps : 1초 동안에 20번 동작 -> 1번에 5만큼이동

    # fps 체크
    # print("fps : " + str(clock.get_fps()))

    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get():    # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT:   # 창이 닫히는 이벤트가 발생하였는가?
            running = False # 게임이 진행중이 아님

    # 3. 게임 캐릭터 위치 정의


    # 4. 충돌 처리


    # 5. 화면 그리기

    pygame.display.update()  # 게임화면을 다시 그리기!

# pygame 종료
pygame.quit()