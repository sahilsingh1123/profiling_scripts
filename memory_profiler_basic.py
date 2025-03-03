"""
Memory profiler
python -m memory_profiler my_script.py

# stream output in specific file
@profile(stream=open("memory_profiling.txt", "a+"))

# it creates .dat file
mprof run my_script.py
mprof plot

# garbage collector
gc.collect()
"""

from memory_profiler import profile
import time


@profile
def memory_intensive_function():
    time.sleep(1)
    data = [i ** 2 for i in range(100000)]  # Large list consuming memory
    time.sleep(1)
    return sum(data)


@profile
def memory_intensive_function_free_mem():
    time.sleep(1)
    data = [i ** 2 for i in range(100000)]  # Large list consuming memory
    time.sleep(1)
    del data
    return "test"


if __name__ == "__main__":
    memory_intensive_function()
    memory_intensive_function_free_mem()
