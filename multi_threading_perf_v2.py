import concurrent.futures
import requests
import time
import threading
from datetime import datetime


def log(message):
    """Helper function to print logs with a timestamp (with 3-digit microseconds) and thread id."""
    now = datetime.now()
    current_time = f"{now:%Y-%m-%d %H:%M:%S}.{now.microsecond // 1000:03d}"
    thread_id = threading.get_ident()
    print(f"[{current_time}] [Thread-{thread_id}] {message}")


def heavy_cpu_task():
    """Simulate a heavy CPU task."""
    total = 0
    # Simulate heavy CPU work: sum up a large number of operations.
    for i in range(10 ** 8):
        total += i % 3
    return total


def fetch_and_process(url):
    """Fetch a URL and process the result (simulate CPU work)."""
    log(f"Fetching URL: {url}")
    response = requests.get(url)
    log(f"Received response for URL: {url}")
    cpu_result = heavy_cpu_task()
    log(f"Processed URL: {url} with CPU result: {cpu_result}")
    return response.text


def sequential_method(urls):
    """Process each URL sequentially in the main thread."""
    log("Starting sequential processing")
    results = []
    start_time = time.time()
    for url in urls:
        result = fetch_and_process(url)
        results.append(result)
    elapsed = time.time() - start_time
    log(f"Sequential processing completed in {elapsed:.2f} seconds")
    return results


def multi_threaded_method(urls):
    """Process URLs concurrently using a ThreadPoolExecutor."""
    log("Starting multi-threaded processing")
    results = []
    start_time = time.time()
    # Using a pool of 5 threads (adjust max_workers as needed).
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(fetch_and_process, url) for url in urls]
        for future in concurrent.futures.as_completed(futures):
            results.append(future.result())
    elapsed = time.time() - start_time
    log(f"Multi-threaded processing completed in {elapsed:.2f} seconds")
    return results


if __name__ == "__main__":
    # We'll use a URL that delays for 1 second to simulate an IO-bound operation.
    urls = ["https://httpbin.org/delay/1"] * 5

    log("=== Running sequential method ===")
    sequential_method(urls)

    log("=== Running multi-threaded method ===")
    multi_threaded_method(urls)
