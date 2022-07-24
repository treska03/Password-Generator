import tkinter as tk

from generator import generate_password
from utils import copy_to_clipboard


class UnsafePassword(Exception):
    pass

class MyApp:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Random password generator")
        self.root.geometry('350x60')
        self.root.resizable(False, False)
        self.main_frame = tk.Frame(self.root)
        self.copy_icon = tk.PhotoImage(file="photos/copy.png")
        self.refresh_icon = tk.PhotoImage(file="photos/refresh.png")
        self.entry_window()
    
    def entry_window(self):
        label = tk.Label(self.main_frame, text="Length:")
        label.grid(column=0, row=0)

        self.length_entry = tk.Entry(self.main_frame,width=4)
        self.length_entry.grid(column=1, row=0)

        self.special = tk.BooleanVar()
        special_checkbox = tk.Checkbutton(self.main_frame, text='Special characters', variable=self.special)
        special_checkbox.grid(column=2, row=0, padx=20)

        generate_button = tk.Button(self.main_frame, text="Generate password", command=self.fetch_data)
        generate_button.grid(column=3, row=0)

        self.main_frame.grid(column=0, row=0, pady=0)
    
    def generate_error_label(self, content):
        error_label = tk.Label(self.root, text=content)
        error_label.grid(column=0, row=1, pady=5, sticky="w")

    def password_window(self, length, special_characters, password):
        password_label = tk.Label(self.root, text=password,width=31, anchor="w")
        password_label.grid(column=0, row=0)
        copy_button = tk.Button(self.root, image=self.copy_icon, command=lambda : copy_to_clipboard(password))
        copy_button.grid(column=1, row=0)
        refresh_button = tk.Button(self.root, image=self.refresh_icon, command=lambda : self.generate_and_display_password(length, special_characters))
        refresh_button.grid(column=2, row=0)
        exit_button = tk.Button(self.root, text="Press to exit", command=self.root.destroy)
        exit_button.grid(column=3,row=0)


    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def generate_and_display_password(self, length, special_characters):
        password = generate_password(length, special_characters)
        
        self.clear_frame()
        self.password_window(length, special_characters, password)

    def fetch_data(self):
        length = self.length_entry.get()
        if not length or not length.isdigit():
            self.generate_error_label("Please pass a correct number")
            raise TypeError("Please pass a correct number")
        length = int(length)
        if length < 8:
            self.generate_error_label("The length must be at least 8 characters")
            raise UnsafePassword("The length must be at least 8 characters")
        
        special_characters = self.special.get()

        self.generate_and_display_password(length, special_characters)


