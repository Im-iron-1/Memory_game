import pygame
import random

pygame.init()

def setup(level):
    global display_time
    display_time = 16-level
    display_time = max(display_time,10)
    print(display_time)
    number_count = level + 5
    shuffle_grid(number_count)
    
def shuffle_grid(number_count):
    rows = 6
    cols = 8
    cell_size = 120
    button_size = 100
    grid = []
    
    grid = [[0 for _ in range(cols)] for i in range(rows)]
    
    number = 1

    while number <= number_count:
        pos_x = random.randrange(0,rows)
        pos_y = random.randrange(0,cols)
        if grid[pos_x][pos_y] == 0:
            grid[pos_x][pos_y] = number
            number += 1
            
            center_x = cell_size * (0.5+pos_y)
            center_y = cell_size * (0.5+pos_x)
            button = pygame.Rect(0,0,button_size,button_size)
            button.center = (center_x,center_y)
            
            number_buttons.append(button)
            
    print(grid) 
       
def display_game_screen():
    global hidden
    if not hidden:
        elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
        if elapsed_time > display_time :
            hidden = True
    
    for idx,rect in enumerate(number_buttons,start = 1):
        if hidden:
            pygame.draw.rect(screen,GRAY,rect)
        else:
            cell_text = game_font.render(str(idx),True,WHITE)
            text_rect = cell_text.get_rect(center=rect.center)
            screen.blit(cell_text,text_rect)
            
font = pygame.font.SysFont(None, 100)

def display_start_screen():
    pygame.draw.circle(screen, WHITE,start_button.center, 60, 7) # level 나오게 font
    text = font.render(str(current_level), True, WHITE)
    text_center = text.get_rect(center=start_button.center)
    screen.blit(text, text_center)
    
def check_buttons(pos):
    global start
    global start_ticks
    if start:
        check_number_buttons(pos)
    elif start_button.collidepoint(pos):
        start = True
        print("게임시작!")
        
    start_ticks = pygame.time.get_ticks()
        
def check_number_buttons(pos):
    global hidden
    global start
    global current_level
    for button in number_buttons:
        if button.collidepoint(pos):
            if button == number_buttons[0]:
                del number_buttons[0]
                print("correct")
                if not hidden:
                    hidden = True
            else:
                print("worng")
                game_over()
    if number_buttons == []:
        current_level += 1
        setup(current_level)
        start = False
        hidden = False

def game_over():
    global running
    running = False
    msg = game_font.render(f"Your level is {current_level}",True, WHITE)
    msg_rect = msg.get_rect(center = (screen_width/2,screen_height/2))
    screen.fill(BLACK)
    screen.blit(msg,msg_rect)
pygame.init()
#화면 크기 설정
screen_width = 960
screen_height = 720
game_font = pygame.font.Font(None,120)

BLACK = (0,0,0)
WHITE = (255,255,255)
GRAY = (50,50,50)

number_buttons = []

current_level = 1

display_time = None

start_ticks = None

screen = pygame.display.set_mode((screen_width,screen_height))

#시작 버튼
start_button = pygame.Rect(0,0,120,120)
start_button.center = (120,screen_height - 120)

#게임 시작 여부
start = False

#숫자 숨기기
hidden = False

setup(current_level)

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
pygame.time.delay(1500)
pygame.quit()