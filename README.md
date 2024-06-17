# elevator_project

**Elevator Project** is a Python program designed for managing elevators, simulating their behavior within a building using Pygame.

## Overview

This simulation consists of three main classes:

- **Building**: Represents the building containing floors and elevators.
- **Floor**: Represents a floor in the building with buttons and timers.
- **Elevator**: Represents an elevator with functionality for movement and scheduling.

## Classes

### Building Class

The `Building` class initializes and manages the building structure. It includes methods for updating and drawing the building on the screen.

### Floor Class

The `Floor` class represents a floor in the building. It handles the buttons for calling elevators and timers for indicating elevator arrival times. This class is responsible for user interaction and updating the floor status.

### Elevator Class

The `Elevator` class represents an elevator. It manages its movement, scheduling, and availability. This class updates the elevator position and status based on user input and simulation logic.

## Features

- Multiple elevators with configurable parameters such as speed and capacity.
- Simulation of elevator movement and arrival times.
- User interaction to call elevators and select destinations.

## Structure

The project is organized as follows:

- `config.py`: Configuration file containing parameters such as elevator speed, floor height, and button colors.
- `main.py`: Main script to run the simulation.
- `Building_class.py`: Class definition for the Building.
- `floor_class.py`: Class definition for the Floor.
- `elevator_class.py`: Class definition for the Elevator.
- `stopwatch_class.py`: Class definition for a stopwatch used for timing.
- `timer_class.py`: Class definition for a timer used for scheduling.

## Installation and Usage

### Prerequisites

- Python 3.x
- Pygame library

### Installation

1. Clone the repository:
    git clone https://github.com/yourusername/elevator-simulation.git

2. Install Pygame:
    pip install pygame


### Usage

1. Run the main_elevator.py
    

2. Click on a floor button to call an elevator.

### Configuration

The program can be configured using the `settings.py` file. Parameters such as elevator speed, floor height, and button colors can be adjusted to customize the simulation.

## Walkthrough of the Program

When running the `main_elevator.py` file, a `Building` object is created, which then initializes all other objects in their starting positions.

When a button is pressed, the building will find the best elevator to send to that floor. The `manager()` function is then run on that elevator, which handles the rest.

In each iteration of the Pygame loop, all objects are updated and then displayed on the screen.
