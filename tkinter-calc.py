import tkinter as tk

text = ''

root = tk.Tk()
root.title('Calc')

font = ('Arial', 16)

lab = tk.Label(
  root,
  font = font
)
lab.pack()

buttons_group = tk.Frame(root)
buttons_group.pack()

def create_button(num, index: int):
  global root
  def add_char():
    global text
    text = text + str(num)
    lab.config(text = str(text)) # FIXME

  tk.Button(
    buttons_group,
    text = str(num),
    command = add_char,
    padx = 1,
    pady = 1,
    width = 4,
    height = 2,
    font = font,
  ).grid(
    row = index // 3,
    column = index % 3,
    sticky = "ew",
    padx = 1,
    pady = 1,
  )

symbols = [1, 2, 3, 4, 5, 6, 7, 8, 9, '=', 0, '<']
for num, signal in enumerate(symbols):
  create_button(signal, num)

root.mainloop()
