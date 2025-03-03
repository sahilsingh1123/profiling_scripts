"""
Get performance stats from each line of code segment

How to run
kernprof -l -v line_profiler.py
"""


from line_profiler import profile, LineProfiler


@profile
def process_data():
    data = [i ** 2 for i in range(100000)]
    total = 0
    for num in data:
        total += num
    return total


@profile
def process_data_efficiently():
    data = (i ** 2 for i in range(100000))  # generator
    total = sum(data)
    return total


# Can be used with decorators
print(process_data())
print(process_data_efficiently())

if __name__ == "__main__":
    '''
    # If we use below logic then no need to use decorator @profile on methods
    '''
    # # Initialize the profiler
    # lp = LineProfiler()
    #
    # # Add the functions to profile
    # lp.add_function(process_data)
    # lp.add_function(process_data_efficiently)
    #
    # # Wrap the functions with profiling
    # profiled_process_data = lp(process_data)
    # profiled_process_efficiently = lp(process_data_efficiently)
    #
    # # Run the profiled functions
    # print(profiled_process_data())
    # print(profiled_process_efficiently())
    #
    # # Print the profiling results
    # lp.print_stats()
    # # Directly write stats to a file
    # with open("line_profile_stats.txt", "w") as f:
    #     lp.print_stats(stream=f)

"""
Time - Total time spent on the line (microseconds)
Per Hit - Avg time per execution of the line (Time/Hits)
Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    11                                           @profile
    12                                           def process_data():
    13         1       1688.0   1688.0     54.6      data = [i ** 2 for i in range(10000)]
    14         1          0.0      0.0      0.0      total = 0
    15     10001        678.0      0.1     21.9      for num in data:
    16     10000        724.0      0.1     23.4          total += num
    17         1          0.0      0.0      0.0      return total


"""