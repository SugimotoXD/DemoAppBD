import pyodbc
import tkinter as tk
from PIL import Image, ImageTk


class ClientInfoApp(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.geometry("500x500")
        self.pack()

        # Connect to database
        self.conn = pyodbc.connect('Driver={SQL Server};'
                                   'Server=SAICHI-SAMA\SQLEXPRESS;'
                                   'Database=BasePy;'
                                   'Trusted_Connection=yes;')
        self.cursor = self.conn.cursor()

        # Get all clients
        self.cursor.execute('SELECT * FROM Client')
        self.clients = self.cursor.fetchall()
        self.current_client_index = 0

        # Create widgets
        self.client_info_label = tk.Label(self, text="")
        self.client_photo_label = tk.Label(self)
        self.prev_button = tk.Button(self, text="Предыдущий", command=self.prev_client)
        self.next_button = tk.Button(self, text="Следующий", command=self.next_client)
        self.page_number_label = tk.Label(self, text="")

        # Display widgets
        self.client_info_label.pack(side="bottom", padx=34, pady=10)
        self.client_photo_label.pack(side="bottom", padx=34, pady=10)
        self.prev_button.pack(side="left")
        self.next_button.pack(side="right")

        # Update display
        self.update_display()

    def update_display(self):
        # Get current client
        current_client = self.clients[self.current_client_index]

        # Display client information
        self.client_info_label.config(text=f"ID клиента: {current_client[0]}\n"
                                            f"ФИО: {current_client[1]} {current_client[2]} {current_client[3]}\n"
                                            f"Пол: {current_client[4]}\n"
                                            f"Дата рождения: {current_client[7]}\n"
                                            f"Дата регистрации: {current_client[9]}\n"
                                            f"Email: {current_client[8]}", justify="center", padx=100, pady=10)
        self.client_info_label.config(font=("Arial", 14))

        # Display client photo
        image_path = current_client[6]
        if image_path:
            image = Image.open(image_path)
            image = image.resize((200, 200), Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(image)
            self.client_photo_label.configure(image=photo)
            self.client_photo_label.image = photo
        else:
            self.client_photo_label.configure(image=None)

    def prev_client(self):
        # Go to previous client
        if self.current_client_index > 0:
            self.current_client_index -= 1
            self.update_display()

    def next_client(self):
        # Go to next client
        if self.current_client_index < len(self.clients) - 1:
            self.current_client_index += 1
            self.update_display()


root = tk.Tk()
app = ClientInfoApp(master=root)
app.mainloop()