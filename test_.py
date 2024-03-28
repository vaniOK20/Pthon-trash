import tkinter as tk

x=0
y=0

def up(event):
	global y
	y=y-50
	c.coords(object0, x, y, x+50, y+50)

def down(event):
	global y
	y=y+50
	c.coords(object0, x, y, x+50, y+50)

def right(event):
	global x
	x=x+50
	c.coords(object0, x, y, x+50, y+50)

def left(event):
	global x
	x=x-50
	c.coords(object0, x, y, x+50, y+50)

window=tk.Tk()

c=tk.Canvas(window, width=500, height=500, bg='white')
c.pack()

object0=c.create_rectangle(x, y, x+50, y+50, fill='black')

window.bind('<Up>', up)
window.bind('<Down>', down)
window.bind('<Right>', right)
window.bind('<Left>', left)
window.mainloop()
