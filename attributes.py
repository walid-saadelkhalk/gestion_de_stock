import pygame
from Product import Product
width, height = 1000, 600

pygame.init()
text_font = pygame.font.Font("font/Kanit-Black.ttf", 15)
bouton_font = pygame.font.Font("font/Kanit-Black.ttf", 30)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Footlocker")
background = pygame.image.load("images/background.png")
image_width, image_height = background.get_size()
x = (width - image_width) // 2
y = height - image_height

# Boutons pour les produits
button_create = bouton_font.render("AJOUTER MODELE", True, (255, 255, 255))
button_read = bouton_font.render("LIRE STOCK", True, (255, 255, 255))
button_update = bouton_font.render("MODIFIER PAIRE", True, (255, 255, 255))
button_delete = bouton_font.render("SUPPRIMER PAIRE", True, (255, 255, 255))
# Rectangle pour les boutons
button_create_rect = button_create.get_rect(topleft=(width // 5 - 150, height // 2 - 250))
button_read_rect = button_read.get_rect(topleft=(width // 5 - 150, height // 2 - 120))
button_update_rect = button_update.get_rect(topleft=(width // 5 - 150, height // 2 + 10))
button_delete_rect = button_delete.get_rect(topleft=(width // 5 - 150, height // 2 + 140))

# Boutons pour les catégories
button_create_category = bouton_font.render("AJOUTER MARQUE", True, (255, 255, 255))
button_read_category = bouton_font.render("LIRE MARQUES", True, (255, 255, 255))
button_update_category = bouton_font.render("MODIFIER MARQUE", True, (255, 255, 255))
button_delete_category = bouton_font.render("SUPPRIMER MARQUE", True, (255, 255, 255))
# Rectangle pour les boutons
button_create_category_rect = button_create_category.get_rect(topleft=(width - 320, height // 2 - 250))
button_read_category_rect = button_read_category.get_rect(topleft=(width - 270, height // 2 - 120))
button_update_category_rect = button_update_category.get_rect(topleft=(width - 330, height // 2 + 10))
button_delete_category_rect = button_delete_category.get_rect(topleft=(width - 350, height // 2 + 140))

button_back = bouton_font.render("RETOUR", True, (255, 0, 0))
button_back_rect = button_back.get_rect(topleft=(850, 550))

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
