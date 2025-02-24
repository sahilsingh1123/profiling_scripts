import concurrent.futures
import requests
import time
import threading
from queue import Queue
from datetime import datetime
import json
from line_profiler import profile


number_times = 1
urls = [
        "https://example.com/file1",
        "https://example.com/file2",
        # "https://example.com/file3",
        # "https://example.com/file4",
        # "https://example.com/file5",
        # "https://example.com/file6",
        # "https://example.com/file7",
    ] * number_times  # Repeat to simulate more work
# urls = [url_domain] * 16


def log(message):
    """Helper function to print logs with a timestamp and thread id."""
    current_time = time.strftime("%Y-%m-%d %H:%M:%S.%2f")
    now = datetime.now()
    current_time = f"{now:%Y-%m-%d %H:%M:%S}.{now.microsecond // 1000:03d}"
    thread_id = threading.get_ident()
    print(f"[{current_time}] [Thread-{thread_id}] {message}")


def heavy_cpu_task():
    """
    Simulate a heavy CPU task.
    """
    total = 0
    # Increase the iteration count for a heavier CPU load.
    for i in range(10**8):
        total += i % 3
    return total


def process_result(result):
    """
    CPU processing performed on the API response.
    For demonstration, it parses the JSON and extracts the 'origin' field.
    """
    log("Processing result")
    data = result
    # data = json.loads(result)
    # origin = data.get("origin", "unknown")
    cpu_result = heavy_cpu_task()
    log("Done processing result")
    return data, cpu_result


# @profile
def io_task(url, result_queue):
    """
    Performs an IO-bound operation (API call) only.
    The API response is put into a queue so that CPU processing can be done later in the main thread.
    """
    try:
        log("Making api call - io")
        response = requests.get(url)
        log("Done with api call")
        result_queue.put(response.text)
    except Exception as e:
        result_queue.put(f"Error: {e}")


# @profile
def io_cpu_task(url):
    """
    Performs both IO-bound operation (API call) and CPU processing (parsing JSON)
    within the same thread.
    """
    try:
        log("Making api call - cpu")
        response = requests.get(url)
        log("Done with api call")
        # CPU processing is done inside the thread.
        origin, _ = process_result(response.text)
        # print("io_cpu_task processed origin:", origin)
    except Exception as e:
        print("Exception in io_cpu_task:", e)


# @profile
def io_bound_example():
    print("Starting IO-bound tasks (CPU processing in main thread)...")
    # urls = ["https://httpbin.org/get"] * number_times
    result_queue = Queue()

    # Use ThreadPoolExecutor with 16 threads to perform only the IO operations.
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        futures = [executor.submit(io_task, url, result_queue) for url in urls]
        concurrent.futures.wait(futures)

    # Main thread performs the CPU processing (parsing the response).
    while not result_queue.empty():
        result = result_queue.get()
        origin, _ = process_result(result)
        # print("Main thread processed origin:", origin)
    print("IO-bound tasks completed.\n")


# @profile
def io_cpu_bound_example():
    print("Starting IO-CPU-bound tasks (CPU processing inside threads)...")
    # urls = ["https://httpbin.org/get"] * number_times

    # Use ThreadPoolExecutor with 16 threads to perform both IO and CPU operations.
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        futures = [executor.submit(io_cpu_task, url) for url in urls]
        # Ensure any exceptions in the threads are propagated.
        for future in concurrent.futures.as_completed(futures):
            future.result()

    print("IO-CPU-bound tasks completed.\n")


if __name__ == "__main__":
    # Measure time for IO-bound tasks (CPU processing in main thread)
    start_time = time.time()
    io_bound_example()
    io_bound_time = time.time() - start_time
    print(f"Time taken for IO-bound example: {io_bound_time:.2f} seconds\n")

    # Measure time for IO-CPU-bound tasks (CPU processing inside threads)
    start_time = time.time()
    io_cpu_bound_example()
    io_cpu_bound_time = time.time() - start_time
    print(f"Time taken for IO-CPU-bound example: {io_cpu_bound_time:.2f} seconds\n")

    print("Completed.")
