import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO

number = 1
current_href = ""

def load_image_from_url(url):
    url_with_number = url.replace("%num%", str(number))
    response = requests.get(url_with_number)
    img_data = response.content
    img = Image.open(BytesIO(img_data))
    return img

def open_chr(event):
    global number, current_href
    current_href = href_entry.get()
    print(current_href)
    label.destroy()
    href_entry.destroy()
    number = 1

    image = load_image_from_url(current_href)
    image = image.resize((640-120, 929-120), Image.BICUBIC)
    photo = ImageTk.PhotoImage(image)

    fotoD.config(image=photo)
    fotoD.image = photo

def increment_number(event):
    global number
    number += 1
    update_image()

def decrement_number(event):
    global number
    number -= 1
    update_image()

def update_image():
    print('loading image')
    global current_href
    image = load_image_from_url(current_href)
    image = image.resize((640-120, 929-120), Image.BICUBIC)
    photo = ImageTk.PhotoImage(image)

    fotoD.config(image=photo)
    fotoD.image = photo
    print(current_href,number)

root = tk.Tk()
root.title("Manga See")

label = tk.Label(text='Enter href to manga img')
label.pack()

href_entry = tk.Entry(root, width=30)
href_entry.bind("<Return>", open_chr)
href_entry.pack()

fotoD = tk.Label(root)
fotoD.pack(side=tk.RIGHT)

# Додайте обробник стрілок вправо та вліво
root.bind("<Right>", increment_number)
root.bind("<Left>", decrement_number)

root.mainloop()
