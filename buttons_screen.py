from attributes import *

def button():
    screen.fill(black)
    screen.blit(background, (x, y)) 
    screen.blit(button_create, (width // 5 - 150, height // 2 - 250))
    screen.blit(button_read, (width // 5 - 150, height // 2 -120))
    screen.blit(button_update, (width // 5 - 150, height // 2 + 10))
    screen.blit(button_delete, (width // 5 - 150, height // 2 + 140))
    screen.blit(button_create_category, (width - 320, height // 2 - 250))
    screen.blit(button_read_category, (width - 270, height // 2 - 120))
    screen.blit(button_update_category, (width - 330, height // 2 + 10))
    screen.blit(button_delete_category, (width - 350, height // 2 + 140))
    