from settings import * 
from timer import * # type: ignore
from stopwatch import *
import pygame

class elevator:

    def __init__(self, i):
        self.array_order = []  # List of requested floors
        self.availability_floor = 0  # Floor where the elevator will be available
        self.pixels_travel = 0  # Pixels traveled for animation
        self.availability_time = 0  # Time when the elevator will be available
        self.sum_availability_time = 0  # Sum of availability times
        self.current_floor = 0  # Current floor of the elevator
        self.prevous_floor = 0  # Previous floor where the elevator was
        self.travel = 0  # Time for travel between floors
        self.time_past = 0  # Time passed
        self.time_waiting = 0  # Waiting time on a floor
        self.current_time = 0  # Current time in the journey
        self.display_current_floor = (1 + self.current_floor) * FLOOR_HEIGHT  # Display position of the elevator
        self.num_elv = i  # Elevator number
        self.tt = StopWatch()  # Stopwatch for timing
        self.img = pygame.image.load('elv.png')  # Loading elevator image
        self.img = pygame.transform.scale(self.img, (FLOOR_HEIGHT, FLOOR_HEIGHT))  # Resizing image to floor height
        self.and_delay_on_floor = 0  # Timer for delay on a floor

    def manager(self, floor, availabil_time):
        self.array_order.append(floor)  # Adding floor request to the list
        self.sum_availability_time = availabil_time + TIME_STOP_FLOOR  # Calculating total time until elevator is available
        self.availability_time = availabil_time  # Setting availability time
        self.availability_floor = floor  # Setting available floor
        self.and_delay_on_floor = Timer(self.availability_time + TIME_STOP_FLOOR)  # type: ignore # Setting timer for delay on a floor

    def availability(self):
        return self.sum_availability_time, self.availability_floor  # Returning availability time and floor

    def update(self):
        if self.sum_availability_time != 0: # Which means the evelvator is not free
            self.sum_availability_time = self.and_delay_on_floor.time_remaining()  # Updating availability time
        if self.array_order and self.time_waiting == 0:
            self.prevous_floor = self.current_floor  # Saving previous floor
            self.current_floor = self.array_order.pop(0)  # Getting next floor from the queue
            self.current_time = StopWatch()  # Starting stopwatch for journey
            self.travel = abs(self.current_floor - self.prevous_floor) * TIME_PASS_FLOOR  # Calculating travel time
            self.time_waiting = TIME_STOP_FLOOR  # Setting waiting time on a floor
        if self.travel != 0:
            t = self.current_time.get_elapsed_time()  # Getting elapsed time
            if self.current_floor > self.prevous_floor:
                self.pixels_travel = -FLOOR_HEIGHT / TIME_PASS_FLOOR * t  # Calculating pixel movement for animation
            else:
                self.pixels_travel = FLOOR_HEIGHT / TIME_PASS_FLOOR * t
            if t >= self.travel:
                self.travel = 0  # Ending travel
                self.pixels_travel = 0  # Resetting pixel movement
                self.display_current_floor = (1 + self.current_floor) * FLOOR_HEIGHT  # Updating display position
                pygame.mixer.Sound('ding.mp3').play()  # Playing arrival sound
                self.tt = StopWatch()  # Resetting stopwatch
        if self.travel == 0:
            t2 = self.tt.get_elapsed_time()  # Getting elapsed time
            if t2 >= self.time_waiting:
                self.time_waiting = 0  # Resetting waiting time

    def draw_elevator(self, screen, x):
        screen.blit(self.img, (x, SCREEN_HEIGHT - self.display_current_floor + self.pixels_travel))  # Drawing elevator on the screen
