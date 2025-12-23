import pygame
import sys
import time
import COLORS

pygame.init()

width = 600
height = 600
weight = 15

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tic Tac Toe")

table = [[None] * 3] * 3
print(f'Table: {table}')
cur_player = "x"
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
            if table[line][column] is not None:
                text = font.render(table[line][column], True, COLORS.BLUE_1)
                screen.blit(text, (column * (width//3) + 25, line * (height//3) + 10 ))

def check_winner():
    # horizontal
    for line in table:
        if line.count(line[0]) == 3 and line[0] is not None:
            return line[0]
    # vertical
    for col in range(3):
        if table[0][col] == table[1][col] == table[2][col] and table[0][col] is not None:
            return table[0][col]
    # diagonal
    if table[0][0] == table[1][1] == table[2][2] and table[0][0] is not None:
        return table[0][0]
    if table[0][2] == table[1][1] == table[2][0] and table[0][2] is not None:
        return table[0][2]
    return None

while game_over is not True:
    draw_table()
    draw_symbols()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            column = x // (width // 3)
            line = y // (height // 3)

            print(f'x: {x}, y: {y}; column: {column}, line: {line}')

            if table[line][column] is None:
                table[line][column] = cur_player
                winner = check_winner()

                print(f'winner: {winner}')
                
                if winner is not None:
                    print("Player", winner, "wins!")
                    game_over = True

                cur_player = "o" if cur_player == "x" else "x"
                
    pygame.display.update()

pygame.quit()
