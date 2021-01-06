import requests
import time

"""
Without Concurrency
"""
def download_site(url):
    response = requests.get(url)
    print(f"Read {len(response.content)} from {url}")


if __name__ == "__main__":
    sites = [
        "https://www.tutorialspoint.com/downloading-files-from-web-using-python",
        "https://en.wikipedia.org/wiki/Porco_Rossoe",
    ] * 10
    start_time = time.time()
    for url in sites:
        download_site(url)
    duration = time.time() - start_time
    print(f"Downloaded {len(sites)} in {duration} seconds")
