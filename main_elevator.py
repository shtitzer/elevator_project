import pygame
import time
import math
from floor import *
from elevator import *
from building import *
from settings import *

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), vsync=1)  # Initialize Pygame window
Building = Building()  # Create an instance of the Building class
IMAGE = pygame.image.load('city.jpeg').convert()  # Load background image
rect = IMAGE.get_rect()
rect.bottomleft = (0, 700)  # Position the background image

run = True
while run:
    
    screen.fill((255, 255, 255))  # Clear screen
    screen.blit(IMAGE, rect)  # Draw background image

    Building.update()  # Update the state of all elements
    Building.draw_building(screen)  # Draw the entire building layout on the screen

    for event in pygame.event.get():  # Iterate over all events
        if event.type == pygame.QUIT:  # Check if the user clicked the close button
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:  # Check if the user clicked the mouse
            x, y = pygame.mouse.get_pos()  # Get the position of the mouse click
            Building.order_elevator(x, y)  # Handle elevator order based on mouse click

    pygame.display.update()  # Update the display

pygame.quit()  # Quit Pygame
