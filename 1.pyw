import os
import tkinter as tk
from PIL import Image, ImageTk
import sys

# def`s
def get_image_files(directory):
    image_files = []
    for filename in os.listdir(directory):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            image_files.append(filename)
    return image_files

def display_image(filename):
    image = Image.open(filename)
    image = image.resize((384, 384), Image.BICUBIC)
    photo = ImageTk.PhotoImage(image)

    fotoD.config(image=photo)
    fotoD.image = photo

def delete_photo():
    global selected_filename
    os.system(f'del "{selected_filename}"')

    image_files.remove(selected_filename)
    listbox.delete(listbox.curselection())

def see_photo():
    global selected_filename
    os.system(f'explorer.exe "{current_directory}"')

    image_files = get_image_files(current_directory)
    listbox.delete(0, tk.END)
    for item in image_files:
        listbox.insert(tk.END, item)

# Global
root = tk.Tk()
root.title("Photo See")

# Foto`s
if getattr(sys, 'frozen', False):
    current_directory = sys._MEIPASS
else:
    current_directory = os.path.dirname(os.path.realpath(__file__))
image_files = get_image_files(current_directory)

# Listbox
listbox = tk.Listbox(root, selectmode=tk.SINGLE, height=25)

for item in image_files:
    listbox.insert(tk.END, item)

def on_select(event):
    global selected_filename
    selected_index = listbox.curselection()
    if selected_index:
        selected_filename = image_files[selected_index[0]]
        display_image(selected_filename)

listbox.bind("<<ListboxSelect>>", on_select)
listbox.pack(side=tk.LEFT)

# Label
fotoD = tk.Label(root)
fotoD.pack(side=tk.RIGHT)

# Buttons
delete_button = tk.Button(root, text="del", command=delete_photo)
delete_button.pack(side=tk.LEFT, pady=10)

see_button = tk.Button(root, text="see", command=see_photo)
see_button.pack(side=tk.LEFT)

# Start
root.mainloop()