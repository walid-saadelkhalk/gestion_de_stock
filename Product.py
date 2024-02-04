from Db import Db
from tabulate import tabulate


class Product:
    def __init__(self):
        self.table = "product"
        self.db = Db(host="localhost", user="root", password="", database="store")

    #create product
    def create(self, name, description, price, quantity, id_category):
        query = f"INSERT INTO {self.table} (name, description, price, quantity, id_category) VALUES (%s, %s, %s, %s, %s)"
        values = (name, description, price, quantity, id_category)
        self.db.executeQuery(query, values)




    #read all productsa
    def read (self):
        query = f"SELECT * FROM {self.table}"
        return self.db.fetch(query)

    def render_product_data(self, font, screen):
        y_position = 5
        data = self.read()

        headers = ["ID", "Name", "Description", "Price", "Quantity", "Category ID"]
        header_text = "   |   ".join(headers)
        header_surface = font.render(header_text, True, (0, 0, 0))
        screen.blit(header_surface, (10, y_position))
        y_position += 30

        for row in data:
            product_text = "   |   ".join([str(item) for item in row])
            text_surface = font.render(product_text, True, (0, 0, 0))
            screen.blit(text_surface, (10, y_position))
            y_position += 30
    #end of read all products

        
    def update(self, id, name, description, price, quantity, id_category):
        query = f"UPDATE {self.table} SET name = %s, description = %s, price = %s, id_category = %s, quantity = %s WHERE id = %s"
        values = (name, description, price, quantity, id_category, id)
        self.db.executeQuery(query, values)



    def delete(self, id):
        query = f"DELETE FROM {self.table} WHERE id = %s"
        values = (id,)
        self.db.executeQuery(query, values)





product = Product()
# print(product.read())
    

    