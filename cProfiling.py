"""
cProfile
python -m cProfile -s time your_script.py
# Run and save stats
python -m cProfile -o profile.stats your_script.py
snakeviz profile.stats


tottime - The total time spent in the given function alone
percall - avg time spent in given func alone
cumtime - time including sub functions calls
percall - avg cum time per call
"""


import time
import cProfile, pstats


def fast_function():
    time.sleep(1)
    result = sum(i ** 2 for i in range(10_00000))
    return result


def slow_function():
    time.sleep(1)
    result = sum([i ** 2 for i in range(10_000000)])
    return result


def run_both_func():
    slow_function()
    fast_function()


def run_terminal():
    run_both_func()
    run_both_func()

def generate_perf_file():
    with cProfile.Profile() as profile:
        run_both_func()
        statsData = pstats.Stats(profile)
        statsData.sort_stats(pstats.SortKey.TIME)
        statsData.print_stats()
        statsData.dump_stats("cProfiling_stats.prof")  # tuna/snakeviz cProfiling_stats.prof

if __name__ == "__main__":
    # run_terminal()
    generate_perf_file()

"""
# It can be done in this manner as well
if __name__ == "__main__":
    pr = cProfile.Profile()
    pr.enable()
    
    slow_function()
    fast_function()
    
    pr.disable()
    pr.print_stats(sort="cumulative")
    pr.dump_stats("stats.prof")
"""
