import tkinter as tk
from tkinter import Label, Button, Scrollbar, Text, Entry, INSERT
from Category import Category

class Category_create_GUI:
    def __init__(self, category):
        self.category = category
        self.root = tk.Tk()
        self.root.title("Category Management - Create")

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        x = (screen_width - 400) // 2
        y = (screen_height - 300) // 2

        self.root.geometry(f"400x300+{x}+{y}")

        self.create_widgets_category()

    def create_widgets_category(self):
        tk.Label(self.root, text="Category Name:").pack()
        self.name_entry = Entry(self.root, width=40)
        self.name_entry.pack()

        self.create_category_button = Button(self.root, text="Create Category", command=self.create_category)
        self.create_category_button.pack()

    def create_category(self):
        name = self.name_entry.get()
        self.category.create(name)
        self.root.destroy()


