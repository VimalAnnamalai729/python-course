import time
import threading
from concurrent.futures import ThreadPoolExecutor

# Function to simulate file download
def download_file(file_name):
    print(f"Starting download for {file_name}...")
    time.sleep(2)  # Simulate download time
    print(f"Finished downloading {file_name}")
    return f"{file_name} downloaded"

# List of files to download
file_list = ["file1.txt", "file2.jpg", "file3.pdf", "file4.mp4"]

# Create a thread pool
with ThreadPoolExecutor(max_workers=3) as executor:
    # Submit tasks to the thread pool
    results = executor.map(download_file, file_list)

# Process results
for result in results:
    print(result)


threads = []
for i in range(1, 4):
    thread = threading.Thread(target=download_file, args=(file_list[i]))
    threads.append(thread)
    thread.start()





'''
ThreadPoolExecutor:
    1) Automatically manages thread creation, reuse, and destruction.
    2) Threads are reused for multiple tasks in the pool, reducing overhead.
    3) Automatically waits for tasks to complete when used with a context manager (with).
Manually Creating Threads:
    1) You must explicitly start (start()) and join (join()) threads to ensure proper synchronization.
    2) Threads are created and destroyed for every task, which can add overhead.
'''
