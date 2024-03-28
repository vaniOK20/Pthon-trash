import tkinter as tk
import math

window = tk.Tk()

c = tk.Canvas(window, width=250, height=250, bg='white')
c.pack()

angle=90

angle_rad = angle * (math.pi / 180.0)
end_x = 125 + 100 * math.cos(angle_rad)
end_y = 125 + 100 * math.sin(angle_rad)

object0 = c.create_line(125, 125, end_x, end_y, fill='blue')

window.mainloop()