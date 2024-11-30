import threading
import time

FLAG = True


def test_func():
    count = 0
    while FLAG:
        time.sleep(1)
        count += 1
        print(count)


'''Explain with normal behaviour'''
# test_func()

'''Explain with single thread behaviour'''
threading.Thread(target=test_func, daemon=False).start()

'''Explain with multiple thread behaviour'''
# threads = []
# for i in range(4):  # Download 3 files
#     thread = threading.Thread(target=test_func)
#     threads.append(thread)
#     thread.start()


input("Press Enter")
FLAG = False

"""
In this case:

You explicitly create 3 threads using the threading module.
Task Manager shows 7 threads because:
        => 1 thread is the main thread running your Python program.
        => 3 worker threads from your code.
        => 3 additional threads could be:
            - Internal threads spawned by Python (e.g., for the garbage collector or I/O).
            - OS-level threads supporting Python's runtime.
"""

