import tkinter as tk
import random

color=['black', 'blue', 'red', 'yellow']

def mouse(event):
	global x, y
	x, y = event.x_root, event.y_root

	win_x=window.winfo_x()
	win_y=window.winfo_y()

	# Вирівнювання позиції мищі від позиції вікна программи
	x=(x-win_x)-25
	y=(y-win_y)-25

	# Створення сітки
	x=(x+20)-(x % 50)
	y=(y-5)-(y % 50)

def spawn(event):
	c.create_rectangle(x, y, x+50, y+50, fill=f'{random.choice(color)}')# Створення кубу

def delate(event):
	c.create_rectangle(x, y, x+50, y+50, fill='white')

window = tk.Tk()

c=tk.Canvas(window, width=500, height=500, bg='white')
c.pack()

window.bind('<Motion>', mouse)
window.bind("<Button-1>", spawn)
window.bind("<Button-3>", delate)
window.mainloop()
