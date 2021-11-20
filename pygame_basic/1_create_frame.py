import pygame

pygame.init()  # 초기화(반드시 필요)

# 화면 크기 설정
screen_width = 480  # 가로 길이
screen_height = 640  # 세로 길이
pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Nado game")  # 게임 이름 설정

# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# pygame 종료
pygame.quit()