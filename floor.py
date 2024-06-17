from settings import *
from timer import * # type: ignore
import pygame

class floor:

    def __init__(self, i):
        self.timer = Timer(0)  # type: ignore # Initialize timer with 0
        self.num_floor = i  # Floor number
        self.floor_available = True  # Flag indicating floor availability

    def draw_floor(self, screen):
        # Calculate the vertical position to draw each floor
        h = SCREEN_HEIGHT - (self.num_floor + 1) * FLOOR_HEIGHT
        # Load the floor image
        image = pygame.image.load("brucks.jpg").convert()
        # Draw the floor image at the specified position
        screen.blit(image, (BUILDING_POSITION_WIDTH, h), (0, 0, FLOOR_WIDTH, FLOOR_HEIGHT))
        # Draw a separating line between floors
        pygame.draw.line(screen, (0, 0, 0), (BUILDING_POSITION_WIDTH, h + 3), (BUILDING_POSITION_WIDTH + FLOOR_WIDTH - 1, h + 3), 7)

    def draw_button(self, screen):
        # Determine button color based on timer state
        if self.timer.time_remaining() > 0:
            COLOR = BUTTON_PRESSED_COLOR  # Button pressed color
        else:
            COLOR = BUTTON_COLOR  # Default button color
        # Draw a circular button
        pygame.draw.circle(screen, COLOR, 
                           ((BUILDING_POSITION_WIDTH + FLOOR_WIDTH // 2), 
                            SCREEN_HEIGHT - (self.num_floor + 1) * FLOOR_HEIGHT + ((FLOOR_HEIGHT + BUTTOM_SPACE) / 2)), 10)

    def drew_number(self, screen):
        # Calculate vertical position for the number display
        y = (SCREEN_HEIGHT - (self.num_floor + 1) * FLOOR_HEIGHT + ((FLOOR_HEIGHT + BUTTOM_SPACE) / 2))
        number = str(self.num_floor)
        font = pygame.font.SysFont('arial', FONT_SIZE)
        text = font.render(number, True, (0, 0, 255), None)
        text_react = text.get_rect()
        text_react.center = (BUILDING_POSITION_WIDTH + FLOOR_WIDTH // 2, y)
        # Draw the floor number centered above the button
        screen.blit(text, text_react)

    def draw_timer(self, screen):
        # Calculate vertical position for the timer display
        y = (SCREEN_HEIGHT - (self.num_floor + 1) * FLOOR_HEIGHT + ((FLOOR_HEIGHT + BUTTOM_SPACE) / 2))
        time_remaining = self.timer.time_remaining()
        if time_remaining > 0:
            timer_str = f'{time_remaining:.2f}'
            font = pygame.font.SysFont('arial', FONT_SIZE)
            text = font.render(timer_str, True, (0, 0, 255), (255, 255, 255))
            text_react = text.get_rect()
            text_react.bottomleft = (BUILDING_POSITION_WIDTH + 4, y + FONT_SIZE / 2)
            # Draw the remaining time on the floor
            screen.blit(text, text_react)

    def start_timer(self, time):
        # Set the timer for elevator arrival and sound
        self.timer = Timer(time) # type: ignore
        #pygame.mixer.Sound('ding.mp3').play()  # Play arrival sound

    def update_floor_availability(self):
        if self.timer.time_remaining() > 0:
            self.floor_available = False  # Floor is busy if timer is active
        else:
            self.floor_available = True  # Floor is available if timer is expired
        return self.floor_available  # Return floor availability status

    def play_sound(self):
        pygame.mixer.Sound('ding.mp3').play()  # Play sound effect






