import pygame
import COLORS
import sys
import random

width, height, steps = 600, 600, 8

size = { 'width': width / steps, 'height': height / steps }

pygame.init()

scene = pygame.display.set_mode((width, height))

state = {
  'food': { 
    'x': width - size['width'], 
    'y': height - size['height'],
  },
  'snake': [
    {
      'x': size['width'],
      'y': size['height'],
    }
  ]
}

def handle_keydown():
  pressed = pygame.key.get_pressed()
  if pressed[pygame.K_DOWN]:
    state['snake'][0]['y'] += size['height']
  elif pressed[pygame.K_UP]:
    state['snake'][0]['y'] -= size['height']
  elif pressed[pygame.K_RIGHT]:
    state['snake'][0]['x'] += size['width']
  elif pressed[pygame.K_LEFT]:
    state['snake'][0]['x'] -= size['width']
  else:
    print('pressed', pressed)

def handle_events():
  for event in pygame.event.get():
    handle_keydown() if event.type == pygame.KEYDOWN else None

def get_snake(ix = 0):
  return pygame.Rect(state['snake'][ix]['x'], state['snake'][ix]['y'], size['width'], size['height'])

def get_food():
  return pygame.Rect(state['food']['x'], state['food']['y'], size['width'], size['height'])

def draw_snake():
  for ix in range(0, len(state['snake'])):
    pygame.draw.rect(scene, COLORS.BLACK_1, get_snake(ix))

def draw_food():
  pygame.draw.rect(scene, COLORS.RED_1, get_food())

def check_collision():
  return get_snake(0).colliderect(get_food())

def set_food():
  state['snake'].append({ 'x': state['food']['x'], 'y': state['food']['y'] })
  state['food']['x'] = width / steps * random.randint(0, steps - 1)
  state['food']['y'] = height / steps * random.randint(0, steps - 1)

try:
  while True:
    scene.fill(COLORS.WHITE_1)
    draw_food()
    draw_snake()
    if check_collision() is True:
      set_food()
    handle_events()
    pygame.display.update()
except Exception as e:
  print('error', e, e.args, e.with_traceback())

pygame.quit()
sys.exit()
