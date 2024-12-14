import queue
import threading
import time

# Shared queue
task_queue = queue.Queue()

def producer():
    for i in range(1, 5):
        print(f"Producer: Adding task {i}")
        task_queue.put(f"Task {i}")
        time.sleep(1)  # Simulate production delay

def consumer():
    while True:
        task = task_queue.get()
        if task:
            print(task) # Block until an item is available
            if task == "STOP":
                break
            print(f"Consumer: Processing {task}")
            time.sleep(2)  # Simulate processing time

producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

producer_thread.start()
consumer_thread.start()

producer_thread.join()
task_queue.put("STOP")  # Signal consumer to stop
consumer_thread.join()
