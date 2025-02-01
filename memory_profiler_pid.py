import time
import psutil
from memory_profiler import memory_usage
import argparse


def monitor_process(pid):
    """ Monitors memory usage of a running process by PID """
    print(f"pid = {pid}")
    try:
        while psutil.pid_exists(pid):
            mem_usage = memory_usage(proc=pid, interval=1, timeout=1)
            print(f"Memory Usage of PID {pid}: {mem_usage[0]} MB")
            time.sleep(1)
    except psutil.NoSuchProcess:
        print(f"Process {pid} has terminated.")

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("pid", type=int)
    args = parser.parse_args()

    monitor_process(args.pid)
