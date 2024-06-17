import time

class Timer:
    def __init__(self, set_time):
        self.start_time = time.time()  # Record the current time when the timer is initialized
        self.remaining_time = set_time  # Set the total time duration for the timer

    def time_remaining(self):
        current_time = time.time()  # Get the current time
        elapsed_time = current_time - self.start_time  # Calculate elapsed time since start
        remaining_time = max(0, self.remaining_time - elapsed_time)  # Calculate remaining time
        return remaining_time
