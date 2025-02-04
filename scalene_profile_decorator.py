"""

if profile is used as decorator
scalene my_script.py [add @profile on functions]

memory-leak
scalene --memory-leak-detector scalene_profile_decorator.py

scalene
 python -m scalene --profile-interval 1 --html --outfile mem_leak.html memory_profiler_leak.py

decorator open issue
https://github.com/plasma-umass/scalene/issues/226

"""


import time

@profile
def fast_function():
    time.sleep(1)
    val = sum([i**2 for i in range(1000000)])
    result = sum(i ** 2 for i in range(10_000000))
    return result

@profile
def slow_function():
    time.sleep(1)
    result = sum([i ** 2 for i in range(10_000000)])
    return result


def run_both_func():
    slow_function()
    fast_function()



if __name__ == "__main__":
    run_both_func()