"""
Profiling multiple processes
mprof run --include-children my_script.py
mprof plot

"""


import multiprocessing
from memory_profiler import profile

@profile
def worker():
    data = [i for i in range(10**7)]  # ~76 MiB
    return data

if __name__ == "__main__":
    p = multiprocessing.Process(target=worker)
    p.start()
    p.join()