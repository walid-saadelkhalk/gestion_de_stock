import tkinter as tk
from tkinter import Label, Button, Scrollbar, Text, Entry, INSERT
from Product import Product 

class Product_update_GUI:
    def __init__(self, product):
        self.product = product
        self.root = tk.Tk()
        self.root.title("Product Management")

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

    
        x = (screen_width - 600) // 2 
        y = (screen_height - 270) // 3

        self.root.geometry(f"600x600+{x}+{y}")


        self.create_widgets_update()

    def create_widgets_update(self):
        # Entry fields and labels for updating an existing product
        tk.Label(self.root, text="Product ID to Update:", font=("Helvetica", 10)).pack()
        self.update_id_entry = Entry(self.root, width=20)
        self.update_id_entry.pack()

        tk.Label(self.root, text="New Name:", font=("Helvetica", 10)).pack()
        self.new_name_entry = Entry(self.root, width=40)
        self.new_name_entry.pack()

        tk.Label(self.root, text="New Description:", font=("Helvetica", 10)).pack()
        self.new_description_entry = Entry(self.root, width=40)
        self.new_description_entry.pack()

        tk.Label(self.root, text="New Price:", font=("Helvetica", 10)).pack()
        self.new_price_entry = Entry(self.root, width=40)
        self.new_price_entry.pack()

        tk.Label(self.root, text="New Quantity:", font=("Helvetica", 10)).pack()
        self.new_quantity_entry = Entry(self.root, width=40)
        self.new_quantity_entry.pack()

        tk.Label(self.root, text="New Category ID:", font=("Helvetica", 10)).pack()
        self.new_category_id_entry = Entry(self.root, width=40)
        self.new_category_id_entry.pack()

        # Button to update an existing product
        self.update_product_button = Button(self.root, text="Update Product", command=self.update_product)
        self.update_product_button.pack()

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

    def update_product(self):
        # Récupérer les valeurs des champs d'entrée pour la mise à jour
        update_id = self.update_id_entry.get()
        new_name = self.new_name_entry.get()
        new_description = self.new_description_entry.get()
        new_price = self.new_price_entry.get()
        new_quantity = self.new_quantity_entry.get()
        new_category_id = self.new_category_id_entry.get()

        self.product.update(update_id, new_name, new_description, new_price, new_quantity, new_category_id)
        self.show_product_data()
        self.root.destroy()
