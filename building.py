from settings import *
from floor import *
from elevator import *
import math

class Building:

    def __init__(self):
        # Create an array of floors based on the number of floors
        self.floors = [floor(i) for i in range(NUMBER_FLOORS)] 
        # Create an array of elevators based on the number of elevators
        self.elevators = [elevator(i) for i in range(NUMBER_ELEVATORS)] 

    def draw_building(self, screen):
        distance_between_elevators = BUILDING_POSITION_WIDTH + FLOOR_WIDTH + 3 - FLOOR_HEIGHT
        # Draw each floor and its components
        for floor in self.floors:
            floor.draw_floor(screen)       # Draw the floor itself
            floor.draw_button(screen)      # Draw the call button on the floor
            floor.drew_number(screen)      # Draw the floor number
            floor.draw_timer(screen)       # Draw the timer display
        # Draw each elevator at their respective positions
        for elevator in self.elevators:
            elevator.draw_elevator(screen, distance_between_elevators + FLOOR_HEIGHT)
            distance_between_elevators += FLOOR_HEIGHT  # Update the distance for the next elevator

    def button_pressed(self, x, y):  
        # Detect button press
        # Check if the click is within the button's horizontal range
        if BUILDING_POSITION_WIDTH + FLOOR_WIDTH // 2 - (BUTTON_WIDTH // 2) < x < BUILDING_POSITION_WIDTH + FLOOR_WIDTH // 2 - (BUTTON_WIDTH // 2) + BUTTON_WIDTH:
            # Calculate and return the floor number based on the y-coordinate of the click
            return math.ceil((SCREEN_HEIGHT - y) / FLOOR_HEIGHT) - 1
        return None

    def order_elevator(self, x, y):
        # Find the minimum time to arrival given a floor
        order_floor = self.button_pressed(x, y)
        if order_floor is None:
            return
        # Update the floor availability
        floor_available = self.floors[order_floor].update_floor_availability()
        if not floor_available:
            return
        best_time = float('inf')  # Initialize the best time with infinity
        selected_elevator = None  # Initialize the selected elevator
        # Find the elevator with the minimum travel time to the requested floor
        for elevator in self.elevators:
            time, current_floor = elevator.availability()  # Get the current availability of the elevator
            travel_time = abs(current_floor - order_floor) * TIME_PASS_FLOOR + time  # Calculate travel time
            if travel_time < best_time:  # If this elevator is faster, select it
                best_time = travel_time
                selected_elevator = elevator
        # If an elevator was found, assign it to manage the request
        if selected_elevator:
            selected_elevator.manager(order_floor, best_time)
            # Update the floor to show the expected arrival time
            self.floors[order_floor].start_timer(best_time)

    def update(self):
        # Update the state of each elevator
        for elevator in self.elevators:
            elevator.update()
