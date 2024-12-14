from multiprocessing import Process, Lock, Value


# Function to increment a shared variable
def increment_counter(counter, lock):
    for _ in range(10000):
        # counter.value += 1
        with lock:  # Acquire the lock before modifying the shared variable
            counter.value += 1


if __name__ == "__main__":
    # Shared variable
    counter = Value('i', 0)  # 'i' indicates an integer

    # Lock object
    lock = Lock()

    # Create processes
    processes = [Process(target=increment_counter, args=(counter, lock)) for _ in range(5)]

    # Start processes
    for process in processes:
        process.start()

    # Wait for processes to complete
    for process in processes:
        process.join()

    # Display the final value of the counter
    print(f"Final counter value: {counter.value}")

'''
How It Works:
Shared Resource:

Value: A shared variable that can be accessed and modified by multiple processes.
Value('i', 0) initializes an integer ('i') with a value of 0.
Lock:

A Lock ensures that only one process at a time can modify the shared resource.
The with lock statement acquires and releases the lock automatically.
Processes:

Two processes increment the shared counter 1000 times each.
Without the lock, race conditions could lead to incorrect results.

When to Use Manager vs Value:
============================
    Manager:
        Use for complex data types (list, dict, set).
        Internally manages synchronization for these objects.
    Value:
        Use for primitive types or fixed-size ctypes objects (e.g., int, float, char[]).
'''
