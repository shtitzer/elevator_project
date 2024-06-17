

# Screen Dimensions
SCREEN_WIDTH = 1225
SCREEN_HEIGHT = 700

# Building Configuration
NUMBER_FLOORS = 20
NUMBER_ELEVATORS = 10

# Floor Dimensions
FLOOR_HEIGHT = SCREEN_HEIGHT // NUMBER_FLOORS
FLOOR_WIDTH = 100

# Button Dimensions
BUTTON_WIDTH = FLOOR_WIDTH // 4
BUTTON_HEIGHT = (FLOOR_HEIGHT + 20) // 2
BUTTOM_SPACE = 7

# Button Colors
BUTTON_COLOR = (0, 205, 0)               # Green color for buttons
BUTTON_PRESSED_COLOR = (255, 0, 0)       # Red color for pressed buttons


# Elevator Dimensions
ELEVATOR_H = FLOOR_HEIGHT - BUTTOM_SPACE
ELEVATOR_W = ELEVATOR_H

# Building Position on Screen
BUILDING_POSITION_WIDTH = SCREEN_WIDTH // 25
BUILDING_POSITION_HEIGHT = 0

# Font Size
FONT_SIZE = 12  # Font size in pixels

# Time Constants
TIME_PASS_FLOOR = 0.5    # Time to pass one floor (in seconds)
TIME_STOP_FLOOR = 2      # Time to stop at a floor (in seconds)
