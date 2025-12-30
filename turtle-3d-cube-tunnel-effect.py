# https://www.instagram.com/p/DSx1gO5gTJy/

import turtle as t
t.speed(0)
t.bgcolor('black')
t.ht()
colors = ['cyan', 'magenta', 'yellow', 'white']
for i in range(180):
  t.color(colors[i%4]); t.up()
  t.goto(-i*2, -i*2); t.down()
  for _ in range(4):
    t.forward(i*4); t.left(90)
t.done()
