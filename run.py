import pygame
# from pygame.locals import QUIT, MOUSEBUTTONDOWN
from attributes import *
from buttons_screen import button
from Product import product
from Category import category
from render_read import render_read_product, render_read_category
from Product_create_GUI import *
from Product_update_GUI import *
from Product_delete_GUI import *
from Category_create_GUI import *
from Category_update_GUI import *
from Category_delete_GUI import *
    
    
def run(event):
    if event.type == pygame.MOUSEBUTTONDOWN:
        if button_create_rect.collidepoint(event.pos):
            gui = Product_create_GUI(product)
            gui.root.mainloop()
            render_read_product()
        
        elif button_read_rect.collidepoint(event.pos):
            render_read_product()
            
            
        elif button_update_rect.collidepoint(event.pos):
            gui = Product_update_GUI(product)
            gui.show_product_data()
            gui.root.mainloop()
            render_read_product()
        
        
        elif button_delete_rect.collidepoint(event.pos):
            gui = Product_delete_GUI(product)
            gui.show_product_data()
            gui.root.mainloop()
            render_read_product()


        elif button_create_category_rect.collidepoint(event.pos):
            gui = Category_create_GUI(category)
            gui.root.mainloop()
            render_read_category()
        

        elif button_read_category_rect.collidepoint(event.pos):
            render_read_category()
            
                        
        elif button_update_category_rect.collidepoint(event.pos):
            gui = Category_update_GUI(category)
            gui.show_category_data()
            gui.root.mainloop()
            render_read_category()
        

        elif button_delete_category_rect.collidepoint(event.pos):
            gui = Category_delete_GUI(category)
            gui.show_category_data()
            gui.root.mainloop()
            render_read_category()