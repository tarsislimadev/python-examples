import pygame
import COLORS
import sys

width, height, squares = 600, 600, 8
selected = []
table = [
  ['T' , 'H' , 'B' , 'Q' , 'K' , 'B' , 'H' , 'T' ],
  ['P' , 'P' , 'P' , 'P' , 'P' , 'P' , 'P' , 'P' ],
  [None, None, None, None, None, None, None, None],
  [None, None, None, None, None, None, None, None],
  [None, None, None, None, None, None, None, None],
  [None, None, None, None, None, None, None, None],
  ['p' , 'p' , 'p' , 'p' , 'p' , 'p' , 'p' , 'p' ],
  ['t' , 'h' , 'b' , 'q' , 'k' , 'b' , 'h' , 't' ],
]
player = 0

pygame.font.init()
font = pygame.font.SysFont(None, 48)

def draw_squares():
  x, y = width / squares, height / squares
  for i in range(squares):
    for j in range(squares):
      color = COLORS.YELLOW_2 if (i + j) % 2 == 0 else COLORS.GREEN_2
      color = list(map(lambda x: x * 0.75, color)) if len(selected) == 2 and selected[0] == i and selected[1] == j else color
      pygame.draw.rect(scene, color, (i * x, j * y, x, y))

def draw_toys():
  global selected
  x, y = width / squares, height / squares
  for i in range(squares):
    for j in range(squares):
      color = COLORS.WHITE_1 if len(selected) == 2 and selected[0] == i and selected[1] == j else COLORS.BLACK_1
      text = font.render(table[i][j], True, color)
      scene.blit(text, (i * x + 25, j * y + 20))

def get_mouse_pos():
  x, y = pygame.mouse.get_pos()
  return x // (width // squares), y // (height // squares)

def is_letter_uppper(letter = ''): return letter == letter.upper() if letter is not None else False

def moveA(orig, dest, reverse = False): pass

def moveP(orig, dest, reverse = False):
  ox, oy = orig
  orig_letter = table[ox][oy]
  dx, dy = dest
  dest_letter = table[dx][dy]
  if (ox - dx if reverse else dx - ox) == 1:
    if (oy - dy if reverse else dy - oy) == 0:
      return True
  if (ox == 1 or ox == 6): # second or half-last
    if (ox - dx if reverse else dx - ox) == 2:
      if (oy - dy if reverse else dy - oy) == 0:
        return True
    elif (oy - dy if reverse else dy - oy) == 1:
      if dest_letter is not None:
        if (is_letter_uppper(orig_letter) != is_letter_uppper(dest_letter)):
          return True

  return False

def move(letter, orig, dest):
  global player
  if (player % 2 == 0 and not is_letter_uppper(letter)): return False
  if (player % 2 == 1 and is_letter_uppper(letter)): return False
  match letter:
    case 'A': return moveA(orig, dest)
    case 'P': return moveP(orig, dest)
    case 'a': return moveA(orig, dest, True)
    case 'p': return moveP(orig, dest, True)
  return False

def handle_events():
  global selected, player
  for event in pygame.event.get():
    if event.type == pygame.MOUSEBUTTONDOWN:
      line, column = get_mouse_pos()
      if len(selected) == 0:
        selected = [line, column]
      else:
        x, y = selected
        letter = table[x][y]
        if move(letter, (x, y), (line, column)):
          if table[line][column] is None:
            table[line][column] = letter
            table[x][y] = None
            player += 1
          else:
            print(f'Square ({line}, {column}) is not None')
        else:
          print(f'Cant move from ({x}, {y}) to ({line}, {column})')
        selected = []

def main():
  try:
    while True:
      scene.fill(COLORS.WHITE_1)
      draw_squares()
      draw_toys()
      handle_events()
      pygame.display.update()
  except KeyboardInterrupt:
    pass
  except Exception as e:
    print('Error!', e)

pygame.init()
scene = pygame.display.set_mode((width, height))
rect = scene.get_rect()
main()
pygame.quit()
sys.exit()
