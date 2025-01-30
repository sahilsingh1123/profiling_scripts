from memory_profiler import profile
import time

@profile
def memory_intensive_function():
    time.sleep(1)
    data = [i ** 2 for i in range(100000)]  # Large list consuming memory
    time.sleep(1)
    return sum(data)

if __name__ == "__main__":
    memory_intensive_function()
