import pygame
import sys
import COLORS

pygame.init()

width = 600
height = 600
weight = 15

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Tic Tac Toe')

table = [[None, None, None], [None, None, None], [None, None, None]]
cur_player = 'x'
font_size = 100
font = pygame.font.SysFont(None, font_size)
game_over = False

def draw_table():
    screen.fill(COLORS.WHITE_1)
    pygame.draw.line(screen, COLORS.BLACK_1, (width//3, 0), (width//3, height), weight)
    pygame.draw.line(screen, COLORS.BLACK_1, (width//3*2, 0), (width//3*2, height), weight)
    pygame.draw.line(screen, COLORS.BLACK_1, (0, height//3), (height, height//3), weight)
    pygame.draw.line(screen, COLORS.BLACK_1, (0, height//3*2), (height, height//3*2), weight)

def draw_symbols():
    for line in range(3):
        for column in range(3):
            if table[line][column] != None:
                text = font.render(table[line][column], True, COLORS.BLUE_1)
                screen.blit(text, (column * (width//3) + (width//4), line * (height//3) + (height//30)))

def check_winner():
    for line in range(3):
        if table[line][0] != None and table[line][0] == table[line][1] == table[line][2]:
            return table[line][0]
    for col in range(3):
        if table[0][col] != None and table[0][col] == table[1][col] == table[2][col]:
            return table[0][col]
    if table[0][0] != None and table[0][0] == table[1][1] == table[2][2]:
        return table[0][0]
    if table[0][2] != None and table[0][2] == table[1][1] == table[2][0]:
        return table[0][2]
    return None

def play(line, column):
    global game_over, cur_player

    if table[line][column] is None:
        table[line][column] = cur_player
        winner = check_winner()

        if winner != None:
            print('Player', winner, 'wins!')
            game_over = True

        cur_player = 'o' if cur_player == 'x' else 'x'

def handle_quit():
    pygame.quit()
    sys.exit()

def handle_mouse_click():
    x, y = pygame.mouse.get_pos()
    line = y // (height // 3)
    column = x // (width // 3)
    play(line, column)

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            handle_quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            handle_mouse_click()

while game_over != True:
    draw_table()
    draw_symbols()
    handle_events()
    pygame.display.update()

pygame.quit()
