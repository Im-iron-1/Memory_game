import pygame

def display_start_screen():
    pygame.draw.circle(screen, WHITE,start_button.center, 60, 7)

pygame.init()

#화면 크기 설정
screen_width = 1280
screen_height = 720

BLACK = (0,0,0)
WHITE = (255,255,255)

screen = pygame.display.set_mode((screen_width,screen_height))

#시작 버튼
start_button = pygame.Rect(0,0,120,120)
start_button.center = (120,screen_height - 120)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(BLACK)

    display_start_screen()
    
    pygame.display.update()
pygame.quit()