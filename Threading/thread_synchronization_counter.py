import threading

# Shared global variable
global_counter = 0

# Function to increment the global counter
def increment_counter(thread_name):
    global global_counter
    for _ in range(1000000):
        global_counter += 1  # Increment global variable
    print(f"{thread_name} finished. Counter: {global_counter}")


lock = threading.Lock()  # Lock for synchronization

def increment_counter_with_lock(thread_name):
    global global_counter
    for _ in range(1000000):
        with lock:  # Acquire lock
            global_counter += 1  # Increment global variable
    print(f"{thread_name} finished. Counter: {global_counter}")
# Create two threads
thread1 = threading.Thread(target=increment_counter_with_lock, args=("Thread-1",))
thread2 = threading.Thread(target=increment_counter_with_lock, args=("Thread-2",))

# Start threads
thread1.start()
thread2.start()

# Wait for both threads to finish
thread1.join()
thread2.join()

print(f"Final counter value: {global_counter}")
