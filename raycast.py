import tkinter as tk
import math

def intersects(x1, y1, x2, y2, x3, y3, x4, y4):
	def ccw(ax, ay, bx, by, cx, cy):
		return (cy - ay) * (bx - ax) > (by - ay) * (cx - ax)
	return ccw(x1, y1, x3, y3, x4, y4) != ccw(x2, y2, x3, y3, x4, y4) and ccw(x1, y1, x2, y2, x3, y3) != ccw(x1, y1, x2, y2, x4, y4)

def raycasting(event):
	c.delete("ray")
	origin_x, origin_y = 125, 125
	
	for angle in range(0, 180, 1):
		angle_rad = angle * (math.pi / 180.0)
		end_x = origin_x + 100 * math.cos(angle_rad)
		end_y = origin_y + 100 * math.sin(angle_rad)

		intersects_object = intersects(origin_x, origin_y, end_x, end_y, *c.coords(object1))
		
		if intersects_object:
			intersection_point = c.find_withtag("ray")[-1]
			c.coords(intersection_point, origin_x, origin_y, *c.coords(object1))
		
		c.create_line(origin_x, origin_y, end_x, end_y, tags="ray")

window = tk.Tk()

c = tk.Canvas(window, width=250, height=250, bg='white')
c.pack()

object0 = c.create_rectangle(100, 100, 150, 150, fill='blue')
object1 = c.create_rectangle(100, 170, 150, 170+50, fill='red')

window.bind('<space>', raycasting)
window.mainloop()
