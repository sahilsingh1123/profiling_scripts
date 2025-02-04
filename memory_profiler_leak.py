"""
Cache will keep on increasing
"""


from memory_profiler import profile
import numpy as np
import sys
import os


def print_pid():
    """Explicitly print the process ID"""
    print(f"Process started with PID: {os.getpid()}")
    sys.stdout.flush()  # Ensure immediate output

class DataProcessor:
    def __init__(self):
        self.cache = []

    # @profile
    def process(self, data):
        result = np.sum(data)
        self.cache.append(result)  # Leak: cache grows indefinitely
        return result
    

    # @profile
    def process_clear_cache(self, data):
        result = np.sum(data)
        self.cache.append(result)  # Leak: cache grows indefinitely
        self.cache.clear()
        return result


if __name__=="__main__":
    processor = DataProcessor()
    print_pid()
    while True:
        for _ in range(1000):
            # processor.process_clear_cache(np.random.rand(1000))
            processor.process(np.random.rand(1000))
