from Db import Db

class Category:
    def __init__(self):
        self.table = "category"
        self.db = Db(host="localhost", user="root", password="", database="store")

    def create(self, name):
        query = f"INSERT INTO {self.table} (name) VALUES (%s)"
        values = (name,)
        self.db.executeQuery(query, values)

    def read (self):
        query = f"SELECT * FROM {self.table}"
        return self.db.fetch(query)

    def update(self, id, name):
        query = f"UPDATE {self.table} SET name = %s WHERE id = %s"
        values = (name, id)
        self.db.executeQuery(query, values)

    def delete(self, id):
        query = f"DELETE FROM {self.table} WHERE id = %s"
        values = (id,)
        self.db.executeQuery(query, values)

    def add_product(self, id_category, id_product):
        query = f"UPDATE product SET id_category = %s WHERE id = %s"
        values = (id_category, id_product)
        self.db.executeQuery(query, values)


    def product_count(self, id_category):
        query = f"SELECT COUNT(*) FROM product WHERE id_category = %s"
        values = (id_category,)
        return self.db.fetch(query, values)


    def render_category_data(self, font, screen):
        y_position = 5
        data = self.read()

        headers = ["ID", "Name"]
        header_text = "   |   ".join(headers)
        header_surface = font.render(header_text, True, (0, 0, 0))
        screen.blit(header_surface, (10, y_position))
        y_position += 30

        for row in data:
            category_text = "   |   ".join([str(item) for item in row])
            text_surface = font.render(category_text, True, (0, 0, 0))
            screen.blit(text_surface, (10, y_position))
            y_position += 30

category = Category()
print(category.read())


    