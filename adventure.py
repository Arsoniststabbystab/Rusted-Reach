# A Dystopian Text Based Adventure Game
# Author: Rain Jones/Zrainyday
# Date: 26/6/24

# Setting up imports and creating a screen
import pygame
import pygame_gui
import random
import json

pygame.init()

SCREEN_HEIGHT = 800
SCREEN_WIDTH = 800

display = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))
pygame.display.set_caption("Rust's Reach")
icon = pygame.image.load("rust.png")
pygame.display.set_icon(icon)
# Setting up variables and dicts



# Setting up functions



# Main Routine
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    # Constant display update - This should go below everything
    pygame.display.update()