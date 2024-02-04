import tkinter as tk
from tkinter import Label, Button, Scrollbar, Text, Entry, INSERT
from Product import Product

class Product_delete_GUI:
    def __init__(self, product):
        self.product = product
        self.root = tk.Tk()
        self.root.title("Product Management - Delete")

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        x = (screen_width - 400) // 2
        y = (screen_height - 270) // 3

        self.root.geometry(f"400x400+{x}+{y}")

        self.create_widgets_delete()

    def create_widgets_delete(self):
        # Entry field and label for deleting an existing product
        tk.Label(self.root, text="Product ID to Delete:", font=("Helvetica", 10)).pack()
        self.delete_id_entry = Entry(self.root, width=20)
        self.delete_id_entry.pack()

        # Button to delete an existing product
        self.delete_product_button = Button(self.root, text="Delete Product", command=self.delete_product)
        self.delete_product_button.pack()

        # Text widget for displaying data
        self.text_widget = Text(self.root, wrap="none", width=80, height=20)
        self.scrollbar = Scrollbar(self.root, command=self.text_widget.yview)
        self.text_widget.config(yscrollcommand=self.scrollbar.set)

        self.text_widget.pack(side=tk.LEFT, fill=tk.Y)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    def show_product_data(self):
        self.text_widget.delete(1.0, tk.END)  # Clear previous data
        data = self.product.read()

        headers = ["ID", "Name", "Description", "Price", "Quantity", "Category ID"]

        # Display headers
        self.text_widget.insert(INSERT, "   |   ".join(headers) + "\n")

        for row in data:
            row_text = "   |   ".join([str(item) for item in row]) + "\n"
            self.text_widget.insert(INSERT, row_text)

    def delete_product(self):
        # Récupérer la valeur du champ d'entrée pour la suppression
        delete_id = self.delete_id_entry.get()
        self.product.delete(delete_id)
        self.show_product_data()
        self.root.destroy()


