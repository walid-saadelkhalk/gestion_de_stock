import pygame
from pygame.locals import QUIT, MOUSEBUTTONDOWN
from attributes import *
from buttons_screen import button
from Product import product
from Category import category


def render_read_product():
    run = True
    while run:

        for event in pygame.event.get():
            if event.type == QUIT:
                run = False

        screen.fill(white)
        product_data = product.read()
        product.render_product_data(text_font, screen)
        screen.blit(button_back, (850, 550))
        if button_back_rect.collidepoint(pygame.mouse.get_pos()):
            if event.type == MOUSEBUTTONDOWN:
                run = False
        pygame.display.flip()

def render_read_category():
    run = True
    while run:

        for event in pygame.event.get():
            if event.type == QUIT:
                run = False

        screen.fill(white)
        category_data = category.read()
        category.render_category_data(text_font, screen)
        screen.blit(button_back, (850, 550))
        if button_back_rect.collidepoint(pygame.mouse.get_pos()):
            if event.type == MOUSEBUTTONDOWN:
                run = False
        pygame.display.flip()


