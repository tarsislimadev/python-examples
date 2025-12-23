# https://www.instagram.com/p/DSl-Y9FjkTB/

import tkinter as tk

root = tk.Tk()

tk.Label(root, text = 'Your name?').pack()

entry = tk.Entry(root)
entry.pack()

lab = tk.Label(root, font = ('Arial', 16))
lab.pack()

ok = lambda: lab.config(text = f'Hello {entry.get()}')

tk.Button(root, text = 'Wish', command = ok).pack()

root.mainloop()
