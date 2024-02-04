import tkinter as tk
from tkinter import Label, Button, Scrollbar, Text, Entry, INSERT
from Category import Category

class Category_update_GUI:
    def __init__(self, category):
        self.category = category
        self.root = tk.Tk()
        self.root.title("Category Management - Update")

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        x = (screen_width - 400) // 2
        y = (screen_height - 270) // 3

        self.root.geometry(f"400x400+{x}+{y}")

        self.create_widgets_update()

    def create_widgets_update(self):
        # Entry fields and labels for updating an existing category
        tk.Label(self.root, text="Category ID to Update:", font=("Helvetica", 10)).pack()
        self.update_id_entry = Entry(self.root, width=20)
        self.update_id_entry.pack()

        tk.Label(self.root, text="New Name:", font=("Helvetica", 10)).pack()
        self.new_name_entry = Entry(self.root, width=40)
        self.new_name_entry.pack()

        # Button to update an existing category
        self.update_category_button = Button(self.root, text="Update Category", command=self.update_category)
        self.update_category_button.pack()

        # Text widget for displaying category data
        self.text_widget = Text(self.root, wrap="none", width=80, height=20)
        self.scrollbar = Scrollbar(self.root, command=self.text_widget.yview)
        self.text_widget.config(yscrollcommand=self.scrollbar.set)

        self.text_widget.pack(side=tk.LEFT, fill=tk.Y)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    def show_category_data(self):
        self.text_widget.delete(1.0, tk.END)  # Clear previous data
        data = self.category.read()

        headers = ["ID", "Name"]

        # Display headers
        self.text_widget.insert(INSERT, "   |   ".join(headers) + "\n")

        for row in data:
            row_text = "   |   ".join([str(item) for item in row]) + "\n"
            self.text_widget.insert(INSERT, row_text)

    def update_category(self):
        # Récupérer les valeurs des champs d'entrée pour la mise à jour
        update_id = self.update_id_entry.get()
        new_name = self.new_name_entry.get()

        # Mettre à jour la catégorie avec l'ID spécifié
        self.category.update(update_id, new_name)
        self.show_category_data()
        self.root.destroy() 


