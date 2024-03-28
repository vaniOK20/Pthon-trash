import tkinter as tk
from tkinter import messagebox
import random as ran
import os

def confirm():
	random_num=ran.randint(0, 10)
	print(int(str_s.get()), random_num)
	if not int(str_s.get())==random_num:
		res=messagebox.askquestion("Warning", "Do you want to delete the \"System32\"?", icon='warning')
		#os.system('del /q C:/Windows/system32')
		print(res)

window=tk.Tk()
str_s=tk.StringVar()

label=tk.Label(window, text='Input number 0-10')
label.pack()

edit=tk.Entry(window, textvariable=str_s)
edit.pack()

confirm=tk.Button(window, text='Confirm', command=confirm)
confirm.pack()

window.mainloop()