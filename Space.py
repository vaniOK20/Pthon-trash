import tkinter as tk

y=450
x=30
y_speed=0
fly=False

def update_window(event):
	global y, y_speed, fly
	if event.keysym=='??': fly=False
	c.create_rectangle(0, 0, 510, 510, fill='white')
	c.create_rectangle(150, 100, 230, 310, fill='black')
	c.create_rectangle(x, y, x+450, y+100, fill='blue')
	if not y<=310:
		y_speed=y_speed-1
		y=y+y_speed
	else:
		y=y-y_speed
		y_speed=0

def start(event):
	global y_speed, fly
	fly=True
	y_speed=y_speed+1
	c.create_rectangle(230, 310, 150, 400, fill='yellow')
	c.create_rectangle(210, 310, 170, 370, fill='orange')

window = tk.Tk()

c=tk.Canvas(window, width=500, height=500, bg='white')
c.pack()

window.bind('<w>', start)
window.bind('<Button-1>', update_window)
window.mainloop()
