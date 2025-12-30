# https://www.instagram.com/p/DSw-kxQjcOO/

import turtle as t

colors = ["red", "yellow", "cyan", "magenta", "white"]
t.speed(0)
t.bgcolor("black")
t.ht()
for r in range(36):
  t.color(colors[r%5])
  t.circle(120)
  t.left(10)
t.up()
t.goto(0, -10)
t.color("white")
t.write("MANDALA ART", font=("Arial", 18, "bold"))
t.done()
