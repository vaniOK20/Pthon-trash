##############################################################
# Дякую ChatGPT за допомогу в створенні цієї не-до програми! #
##############################################################
import tkinter as tk # Встановити tkinter до tk (змінти йому ім'я)
from tkinter import messagebox
from tkinter import scrolledtext, Entry, Button, filedialog
import subprocess
import threading
import os

class ServerManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Minecraft Server Manager")

        # Консольне вікно
        self.console = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=20)
        self.console.grid(row=0, column=0, padx=10, pady=10, rowspan=3)

        # Текстове поле для введення команд
        self.command_entry = Entry(root, width=30)
        self.command_entry.grid(row=3, column=0, padx=10, pady=5, sticky="W")

        # Елементи управління
        start_button = Button(root, text="Start Server", command=self.start_server)
        start_button.grid(row=3, column=0, padx=10, pady=5, sticky="E")

        stop_button = Button(root, text="Stop Server", command=self.stop_server)
        stop_button.grid(row=3, column=0, padx=90, pady=5, sticky="E")

        # Об'єкт для зберігання підпроцесу сервера
        self.server_process = None

        # Додаємо подію на клавішу 'Enter'
        self.command_entry.bind("<Return>", self.send_command)

        # Перевірка eula.txt та відображення вікна запитання
        self.check_eula()

    def check_eula(self):
        eula_path = "eula.txt"
        if os.path.isfile(eula_path):
            with open(eula_path, "r") as eula_file:
                eula_content = eula_file.read()
                if "eula=false" in eula_content:
                    self.ask_eula_acceptance()

    def ask_eula_acceptance(self):
        result = messagebox.askquestion("EULA Acceptance", "Do you accept the EULA from Mojang?", icon='warning') # Створення вікна з запитом
        if result == 'yes':
            # Користувач прийняв EULA, оновити файл eula.txt
            self.update_eula_file("eula=true")
            print("EULA accepted.")
        else:
            # Користувач відмовився від EULA, завершити програму
            print("EULA rejected. Exiting.")
            self.root.destroy()

    def update_eula_file(self, new_content):
        eula_path = "eula.txt"
        with open(eula_path, "w") as eula_file:
            eula_file.write(new_content) # Записати в "eula.txt" True

    def start_server(self):
        # Отримання шляху до поточної робочої директорії
        current_directory = os.getcwd()

        # Шукати файли з розширенням .jar в поточній директорії
        jar_files = [f for f in os.listdir(current_directory) if f.endswith(".jar")]

        if not jar_files:
            self.log_to_console("Error: No .jar files found in the current directory.")
            return

        # Вибрати перший знайдений файл .jar (можна змінити за потребою)
        selected_jar_file = jar_files[0]

        # Запуск сервера в окремому потоці з параметром creationflags
        self.server_thread = threading.Thread(target=self.run_server, args=(selected_jar_file,))
        self.server_thread.start()

    def run_server(self, selected_jar_file):
        # Запуск сервера та перенаправлення виводу
        self.server_process = subprocess.Popen(
            ["java", "-Xmx1024M", "-Xms1024M", "-jar", selected_jar_file, "nogui"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1,
            universal_newlines=True,
            creationflags=subprocess.CREATE_NO_WINDOW  # Додано параметр creationflags
        )

        # Читання та виведення рядків в реальному часі
        for output in self.server_process.stdout:
            self.log_to_console(output.strip())

        # Запис останніх рядків, якщо сервер вже завершив роботу
        remaining_output = self.server_process.communicate()[0]
        self.log_to_console(remaining_output.strip())

    def stop_server(self):
        # Зупинка сервера
        if self.server_process:
            self.server_process.terminate()
            self.server_process.wait()
            self.log_to_console("Server stopped.")

    def send_command(self, event):
        # Відправка команди до сервера
        command = self.command_entry.get()
        if self.server_process and command:
            self.server_process.stdin.write(command + "\n")
            self.server_process.stdin.flush()
            self.log_to_console(f">>> {command}")
            # Очищення текстового поля після введення команди
            self.command_entry.delete(0, tk.END)

    def log_to_console(self, message): # Логування
        self.console.insert(tk.END, message + "\n")
        self.console.see(tk.END)

if __name__ == "__main__": # Запуск (потрібно щоб не крашнулась прога)
    root = tk.Tk()
    app = ServerManager(root)
    root.mainloop()
