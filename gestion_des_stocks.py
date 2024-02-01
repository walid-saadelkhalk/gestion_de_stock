import mysql.connector

class Sneakers_store:
    def __init__(self, host, user, password, database):
        self.db = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.db.cursor()
    #Shoes
    def create_shoes(self, name, description, price, id_category):
        query = "Insert INTO product (name, description, price, id_category) VALUES (%s, %s, %s, %s)"
        values = (name, description, price, id_category)
        self.cursor.execute(query, values)
        self.db.commit()
        return f"Shoes {name} ajouté avec succès."

    def delete_shoes(self, id):
        query = "DELETE FROM product WHERE id = %s"
        values = (id,)
        self.cursor.execute(query, values)
        self.db.commit()
        return f"Shoes {id} supprimé avec succès."
    
    def read_shoes(self):
        query = "SELECT * FROM product"
        self.cursor.execute(query)
        return self.cursor.fetchall()
    
    #Category
    def create_category(self, name):
        query = "Insert INTO category (name) VALUES (%s)"
        values = (name,)
        self.cursor.execute(query, values)
        self.db.commit()
        return f"Category {name} ajouté avec succès."

    def delete_category(self, id):
        query = "DELETE FROM category WHERE id = %s"
        values = (id,)
        self.cursor.execute(query, values)
        self.db.commit()
        return f"Category {id} supprimée avec succès."

    def read_category(self):
        query = "SELECT * FROM category"
        self.cursor.execute(query)
        return self.cursor.fetchall()



footlocker = Sneakers_store(host="localhost", user="root", password="", database="store")

# print(footlocker.create_shoes("Air Force 1", "La Nike Air Force 1 est une chaussure de basket-ball conçue par Nike. Elle est la première chaussure de basket-ball à utiliser la technologie Nike Air. ", 100, 1))
print(footlocker.read_shoes())
print(footlocker.read_category())
footlocker.cursor.close()
footlocker.db.close()