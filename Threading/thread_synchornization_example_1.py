# https://www.youtube.com/watch?v=u25j0bl3Ecw


import threading
import time

# Shared resource
shared_list = [1, 2, 3, 4, 5]
lock = threading.Lock()  # Lock for synchronization


def pop_from_list_no_lock(thread_name):
    while len(shared_list) > 0:
        time.sleep(0.1)
        value = shared_list.pop()
        print(f"{thread_name} popped {value}. Remaining list: {shared_list}")


# Function to pop elements from the list
# def pop_from_list_context_manager_lock(thread_name):
#     while True:
#         with lock:  # Acquire lock
#             if shared_list:  # Check if list is not empty
#                 value = shared_list.pop()
#                 print(f"{thread_name} popped {value}. Remaining list: {shared_list}")
#             else:
#                 print(f"{thread_name} found the list empty!")
#                 break  # Exit the loop if list is empty
#         # time.sleep(0.1)  # Simulate some processing delay

def pop_from_list_using_lock(thread_name):
    lock.acquire()
    while len(shared_list) > 0:
        # lock.acquire()
        time.sleep(0.1)
        value = shared_list.pop()
        # lock.release()
        print(f"{thread_name} popped {value}. Remaining list: {shared_list}")
    lock.release()

# Create two threads
thread1 = threading.Thread(target=pop_from_list_using_lock, args=("Thread-1",))
thread2 = threading.Thread(target=pop_from_list_using_lock, args=("Thread-2",))

# Start threads
thread1.start()
thread2.start()

# Wait for both threads to finish
thread1.join()
thread2.join()

print("Both threads completed!")

pop_from_list_no_lock()
pop_from_list_no_lock()