import threading
import time


def test_func(t_name):
    for i in range(1, 11):
        print(f'{t_name} :: HEY PYTHONISTS!!! => {i}')
        time.sleep(1)

'''Explain with normal behaviour'''
# test_func('NO THREAD')

'''Explain with single thread behaviour'''
# threading.Thread(target=test_func, daemon=False, args=(f'Thread-1', )).start()

'''Explain with multiple thread behaviour'''
threads = []
for i in range(1, 3):
    thread = threading.Thread(target=test_func, daemon=True, args=(f'Thread-{i}', ))
    threads.append(thread)
    thread.start()

'''Thread.join() - tell the python script to wait until the threads are finished'''
for t in threads:
    t.join()


"""
TO SEE HOW MANY THREADS CREATED UNDER ONE PROCESS:
--------------------------------------------------

Using Task Manager =>
    Windows Task Manager allows you to see thread activity for each process.

    Steps:
    1) Open Task Manager (Ctrl + Shift + Esc).
    2) Go to the Details tab.
    3) Right-click on the column headers and select Select Columns.
    4) Check Threads and click OK.
    5) Look for your Python process (e.g., python.exe) and check the Threads column to see the total number of active threads in that process.
    This shows the total thread count but does not give details about individual threads.

In this python script:
----------------------

You explicitly create 3 threads using the threading module.
Task Manager shows 7 threads because:
        => 1 thread is the main thread running your Python program.
        => 3 worker threads from your code.
        => 3 additional threads could be:
            - Internal threads spawned by Python (e.g., for the garbage collector or I/O).
            - OS-level threads supporting Python's runtime.
"""























# Reference : https://www.youtube.com/watch?v=A_Z1lgZLSNc
# Daemon Thread: https://www.youtube.com/watch?v=llBPmECcLD4