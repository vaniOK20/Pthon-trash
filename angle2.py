import tkinter as tk
import math

angle=0

def rot(event):
	global angle
	angle=angle+5
	xpos=125
	c.create_line(xpos, xpos, xpos+100*math.cos(angle*(math.pi/180)), 125+100*math.sin(angle*(math.pi/180)))

window = tk.Tk()

c=tk.Canvas(window, bg='white', width=500, height=500)
c.pack()

window.bind('<space>', rot)
window.mainloop()