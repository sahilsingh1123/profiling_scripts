"""
Profiling using py-spy
py-spy record -o profile.svg -- python my_script.py

monitor already running process
py-spy top --pid <PID>
# Record for 10 seconds and save to profile.svg
py-spy record -o profile.svg --pid <PID> --duration 10

# Profile only the main thread
py-spy record --pid <PID> --threads

# Profile subprocesses (e.g., in multiprocessing)
py-spy record --subprocesses -o profile.svg -- python my_script.py

# Profile and save in speedscope format for advance tracking
py-spy record --format speedscope -o profile.json -- python my_script.py

stats:
    %Own: Percentage of time spent in the function itself (excludes children).
    %Total: Includes time spent in child functions.


"""

import math
import sys
import os


def print_pid():
    """Explicitly print the process ID"""
    print(f"Process started with PID: {os.getpid()}")
    sys.stdout.flush()  # Ensure immediate output


def is_prime(n):
    """Check if a number is prime (CPU-intensive for large numbers)."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    w = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += w
        w = 6 - w
    return True


def is_armstrong(num):
    """Check if a number is an Armstrong/narcissistic number."""
    order = len(str(num))
    temp = num
    total = 0
    while temp > 0:
        digit = temp % 10
        total += digit ** order
        temp //= 10
    return num == total


def is_perfect_square(n):
    """Check if a number is a perfect square."""
    root = math.isqrt(n)
    return root * root == n


def is_perfect_number(n):
    """Check if a number is a perfect number (sum of proper divisors)."""
    if n <= 1:
        return False
    total = 1
    sqrt_n = math.isqrt(n)
    for i in range(2, sqrt_n + 1):
        if n % i == 0:
            total += i
            if i != n // i:
                total += n // i
    return total == n


def cpu_intensive_analysis():
    """Continuously analyze numbers with multiple checks"""
    print_pid()
    n = 1
    try:
        print("Running CPU-intensive analysis. Press Ctrl+C to exit...")
        while True:
            # Perform multiple checks (results not stored to maximize CPU usage)
            prime = is_prime(n)
            even = n % 2 == 0
            square = is_perfect_square(n)
            armstrong = is_armstrong(n)
            perfect = is_perfect_number(n)

            # Increment number
            n += 1

            # Reset counter periodically to prevent overflow
            if n > 10 ** 6:
                n = 1

    except KeyboardInterrupt:
        print("\nTerminating after analyzing up to:", n)
        sys.exit(0)


if __name__ == "__main__":
    cpu_intensive_analysis()