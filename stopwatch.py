import time

class StopWatch:
    def __init__(self):
        self.start_time = time.time()  # Record the current time when the stopwatch is initialized

    def get_elapsed_time(self):
        current_time = time.time()  # Get the current time
        elapsed_time = current_time - self.start_time  # Calculate elapsed time since start
        return elapsed_time