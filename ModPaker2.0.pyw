import os
import shutil
import json
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def copy_and_rename_version():
    version = version_var.get()
    new_version_name = new_name_var.get()

    if not new_version_name:
        tk.messagebox.showerror("Помилка", "Будь ласка, введіть нову назву версії")
        return

    if new_version_name in versions:
        tk.messagebox.showerror("Помилка", "Така назва версії вже існує")
        return

    old_version_path = os.path.join(versions_dir, version)
    new_version_path = os.path.join(versions_dir, new_version_name)

    shutil.copytree(old_version_path, new_version_path)

    for filename in [".jar", ".jar.bak", ".json"]:
        old_file_path = os.path.join(new_version_path, version + filename)
        new_file_path = os.path.join(new_version_path, new_version_name + filename)
        os.rename(old_file_path, new_file_path)

        if filename == ".json":
            with open(new_file_path, "r+") as json_file:
                data = json.load(json_file)
                data["id"] = new_version_name
                data["jar"] = new_version_name
                data["family"] = new_version_name
                json_file.seek(0)
                json.dump(data, json_file)
                json_file.truncate()

    new_home_path = os.path.join(home_dir, new_version_name)
    os.makedirs(new_home_path, exist_ok=True)
    os.makedirs(os.path.join(new_home_path, "mods"), exist_ok=True)

    tk.messagebox.showinfo("Успіх", f"Версія {version} була перетворена в {new_version_name} модпак")

versions_dir = os.path.expandvars(r"%appdata%\.minecraft\versions")
home_dir = os.path.expandvars(r"%appdata%\.minecraft\home")
versions = os.listdir(versions_dir)


window = tk.Tk()
window.title("Створення модпаку для Minecraft")
window.geometry("400x200")
version_var = tk.StringVar()
new_name_var = tk.StringVar()

label = tk.Label(window, text="Виберіть версію")
label.pack(pady=10)

version_combobox = ttk.Combobox(window, textvariable=version_var, state="readonly")
version_combobox["values"] = versions
version_combobox.current(0)
version_combobox.pack(pady=10)

label2 = tk.Label(window, text="Введіть нову назву версії")
label2.pack(pady=10)

new_name_entry = tk.Entry(window, textvariable=new_name_var)
new_name_entry.pack(pady=10)

button = tk.Button(window, text="Створити модпак", command=copy_and_rename_version)
button.pack(pady=10)

window.mainloop()