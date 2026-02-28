import pygame

pygame.init()

#화면 크기 설정
screen_width = 1280
screen_height = 720

screen = pygame.display.set_mode((screen_width,screen_height))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()