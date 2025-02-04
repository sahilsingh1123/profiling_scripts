"""

Directly profile files
scalene my_script.py

running in cli mode
scalene --cli my_script.py

"""

import time

def fast_function():
    time.sleep(1)
    val = sum([i**2 for i in range(1000000)])
    result = sum(i ** 2 for i in range(10_000000))
    return result

def slow_function():
    time.sleep(1)
    result = sum([i ** 2 for i in range(10_000000)])
    return result


def run_both_func():
    slow_function()
    fast_function()


if __name__ == "__main__":
    run_both_func()
