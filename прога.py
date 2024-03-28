import os
import shutil
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from zipfile import ZipFile

class ModTransferApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Скачування сторонніх модів")

        # Лейбли та поле введення
        self.version_label = tk.Label(self.master, text="Оберіть мод-пак:")
        self.version_label.pack()

        self.error_label = tk.Label(self.master, text="", fg="red")
        self.error_label.pack()

        self.success_label = tk.Label(self.master, text="", fg="green")
        self.success_label.pack()

        # Список модпаків у вигляді Treeview
        self.treeview = ttk.Treeview(self.master, height=10)
        self.treeview.pack(side=tk.LEFT, fill=tk.Y)

        vsb = ttk.Scrollbar(self.master, orient="vertical", command=self.treeview.yview)
        vsb.pack(side=tk.RIGHT, fill=tk.Y)
        self.treeview.configure(yscrollcommand=vsb.set)

        # Додавання модпаків до Treeview
        versions = [folder for folder in os.listdir(os.path.join(os.getenv('APPDATA'), '.minecraft', 'versions')) if os.path.isdir(os.path.join(os.getenv('APPDATA'), '.minecraft', 'versions', folder))]

        for version in versions:
            self.treeview.insert("", "end", text=version)

        # Додавання події для вибору елемента
        self.treeview.bind("<Double-1>", self.create_version)

    def create_version(self, event):
        selected_item = self.treeview.selection()[0]
        version_name = self.treeview.item(selected_item, 'text')

        version_path = os.path.join(os.getenv('APPDATA'), '.minecraft', 'versions', version_name)

        if not os.path.exists(version_path):
            self.error_label.config(text="Цієї збірки не існує.")
            return

        mods_path = os.path.join(version_path, 'mods')
        files_path = os.path.join(mods_path, 'files')

        if not os.path.exists(files_path):
            os.makedirs(files_path)

        mod_file = filedialog.askopenfilename(title=f"Виберіть мод або збірку для {version_name}", filetypes=[("Моди", "*.jar;*.zip")])
        if not mod_file:
            return

        try:
            self.move_mods(mod_file, mods_path)
            self.success_label.config(text="Збірка\\мод були успішно перенесені!")
        except Exception as e:
            self.error_label.config(text=f"Помилка: {str(e)}")

    def move_mods(source, destination):
        if not os.path.exists(destination):
            os.makedirs(destination)

        mods_zip_path = os.path.join(destination, 'mods.zip')

        # Копіюємо zip-файл в каталог 'mods'
        shutil.copy(source, mods_zip_path)

        # Перевіряємо тип файлу
        _, file_extension = os.path.splitext(source)

        if file_extension.lower() == '.zip':
            # Розпаковуємо вміст zip-файлу безпосередньо в каталог 'mods'
            with ZipFile(mods_zip_path, 'r') as mods_zip:
                mods_zip.extractall(os.path.join(destination, 'mods'))

            # Видаляємо zip-файл після розархівування
            os.remove(mods_zip_path)
        else:
            # Якщо це не .zip файл, можливо вам потрібно виконати інші дії
            pass

        # Копіюємо файли з каталогу 'files'
        files_folder_path = os.path.join(destination, 'mods', 'files')
        if os.path.exists(files_folder_path):
            with open(os.path.join(files_folder_path, 'file.txt'), 'r') as file_path_file:
                target_directory = file_path_file.readline().strip()

                # Забезпечення існування цільової директорії
                target_directory_path = os.path.join(destination, target_directory)
                if not os.path.exists(target_directory_path):
                    os.makedirs(target_directory_path)

                # Переміщення файлів відповідно до шляху в 'file.txt'
                for root, _, files in os.walk(files_folder_path):
                    for file in files:
                        file_path = os.path.join(root, file)
                        relative_path = os.path.relpath(file_path, files_folder_path)
                        destination_path = os.path.join(destination, relative_path)
                        shutil.move(file_path, destination_path)

                # Видаляємо тимчасово розпакований каталог 'mods'
                shutil.rmtree(os.path.join(destination, 'mods'))

                # Видалення папки 'files', якщо вона порожня
                if not os.listdir(files_folder_path):
                    os.rmdir(files_folder_path)

        # Видалення тимчасової розархівованої папки
        shutil.rmtree(os.path.join(destination, 'mods'))

# Створення головного вікна
root = tk.Tk()
app = ModTransferApp(root)

# Запуск головного циклу
root.mainloop()