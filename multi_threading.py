import requests
import time
from concurrent.futures import ThreadPoolExecutor
import yappi

def download_file(url):
    response = requests.get(url)
    print(f"Downloaded {url} ({len(response.content)} bytes)")


def single_threaded(urls):
    for url in urls:
        download_file(url)


def multi_threaded(urls):
    with ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(download_file, urls)


if __name__ == "__main__":
    urls = [
        "https://example.com/file1",
        "https://example.com/file2",
        "https://example.com/file3",
    ] * 2  # Repeat to simulate more work

    # yappi.start()
    start_time = time.time()
    single_threaded(urls)
    multi_threaded(urls)
    print(f"Multi-threaded time: {time.time() - start_time:.2f} seconds")
    # yappi.stop()
    # yappi.get_func_stats().print_all()
