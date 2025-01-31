from memory_profiler import profile
import numpy as np

class DataProcessor:
    def __init__(self):
        self.cache = []

    @profile
    def process(self, data):
        result = np.sum(data)
        self.cache.append(result)  # Leak: cache grows indefinitely
        return result

processor = DataProcessor()
for _ in range(1000):
    processor.process(np.random.rand(1000))