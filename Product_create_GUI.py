import tkinter as tk
from tkinter import Entry, Label, Button
from Product import Product

class Product_create_GUI:
    def __init__(self, product):
        self.product = product
        self.root = tk.Tk()
        self.root.title("Product Management")


        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

    
        x = (screen_width - 400) // 2  
        y = (screen_height - 300) // 2 

        self.root.geometry(f"400x300+{x}+{y}")

        self.create_widgets_product()

    def create_widgets_product(self):
        tk.Label(self.root, text="Name:").pack()
        self.name_entry = Entry(self.root, width=40)
        self.name_entry.pack()

        tk.Label(self.root, text="Description:").pack()
        self.description_entry = Entry(self.root, width=40)
        self.description_entry.pack()

        tk.Label(self.root, text="Price:").pack()
        self.price_entry = Entry(self.root, width=40)
        self.price_entry.pack()

        tk.Label(self.root, text="Quantity:").pack()
        self.quantity_entry = Entry(self.root, width=40)
        self.quantity_entry.pack()

        tk.Label(self.root, text="Category ID:").pack()
        self.category_id_entry = Entry(self.root, width=40)
        self.category_id_entry.pack()

        self.create_product_button = Button(self.root, text="Create Product", command=self.create_product)
        self.create_product_button.pack()

    def create_product(self):
        name = self.name_entry.get()
        description = self.description_entry.get()
        price = float(self.price_entry.get())
        quantity = int(self.quantity_entry.get())
        category_id = int(self.category_id_entry.get())

        self.product.create(name, description, price, quantity, category_id)
        self.root.destroy()


