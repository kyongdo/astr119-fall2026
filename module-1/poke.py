import requests
import time


url = input("Enter a URL: ")

start_time = time.time()
response = requests.get(url)
end_time = time.time()

nbytes = len(response.content)
elapsed_time = end_time - start_time

megabytes = nbytes / 1_000_000
rate =  megabytes / elapsed_time 

print(f"{nbytes} bytes read from {url}")
print(f"download took {elapsed_time:.3f} seconds")
print(f"Rate: {rate:.3f} MB/s")
