import threading
import time

# Event for communication
data_ready_event = threading.Event()
shared_data = None  # Shared resource

# Producer thread
def producer():
    global shared_data
    print("Producer: Starting production...")
    time.sleep(2)  # Simulate data production
    shared_data = "Hello Vimal"
    time.sleep(5)
    print("Producer: Data is ready!")
    data_ready_event.set()  # Signal to the consumer

# Consumer thread
def consumer():
    print("Consumer: Waiting for data...")
    data_ready_event.wait()  # Wait until producer signals
    print(f"Consumer: Got the data: {shared_data}")

# Create threads
producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

# Start threads
consumer_thread.start()
producer_thread.start()

# Wait for threads to finish
consumer_thread.join()
producer_thread.join()

print("Thread communication completed.")


