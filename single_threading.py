import requests
import time

def download_file(url):
    response = requests.get(url)
    print(f"Downloaded {url} ({len(response.content)} bytes)")

def single_threaded(urls):
    for url in urls:
        download_file(url)

if __name__ == "__main__":
    urls = [
        "https://example.com/file1",
        "https://example.com/file2",
        "https://example.com/file3",
    ] * 5  # Repeat to simulate more work

    start_time = time.time()
    single_threaded(urls)
    print(f"Single-threaded time: {time.time() - start_time:.2f} seconds")