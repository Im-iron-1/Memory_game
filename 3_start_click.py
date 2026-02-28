import pygame

def display_game_screen():
    print("게임 화면 표시")
def display_start_screen():
    pygame.draw.circle(screen, WHITE,start_button.center, 60, 7)
    
def check_buttons(pos):
    global start
    if start_button.collidepoint(pos):
        start = True
        print("게임시작!")
        
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

#게임 시작 여부
start = False

running = True
while running:
    click_pos = None
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            click_pos = pygame.mouse.get_pos()
            print(click_pos)
    screen.fill(BLACK)

    if start:
        display_game_screen()
    else:
        display_start_screen()
    
    if click_pos:
        check_buttons(click_pos)
    
    pygame.display.update()
pygame.quit()