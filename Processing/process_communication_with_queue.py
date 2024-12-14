"""
PROCESS COMMUNICATION USING A QUEUE:
The Queue object is a thread- and process-safe way to exchange information between processes.

EXPLANATION:
===========
    Queue:
        * Acts as a shared data structure between processes.
        * queue.put(item) adds an item to the queue.
        * queue.get() retrieves an item from the queue.
    Producer-Consumer Model:

        * The producer generates data and puts it into the queue.
        * The consumer retrieves and processes the data from the queue.
    Process Synchronization:

        * The join() method ensures that the main process waits for child processes to finish.

WHEN TO USE QUEUE:
==================
    * Multiple Producers or Consumers:

        If you need multiple processes to simultaneously produce or consume data, a Queue is a better choice as it supports multiple writers and readers.
        Example: A pool of worker processes fetching tasks from a shared task queue.

    *Task Scheduling and Load Balancing:

        When you have a producer-consumer model where one process generates tasks and multiple workers consume them.
        Example: Web scraping with a pool of worker processes retrieving URLs from a shared queue.

    * Buffered Communication:

        The Queue acts as a buffer and doesn't require direct synchronization between producer and consumer processes.
        Example: Streaming data from sensors where consumers process the data asynchronously.

    * Ease of Use:

     Built-in methods like put() and get() simplify interaction, and it internally handles synchronization and safety.


"""

from multiprocessing import Process, Queue

# Function to write data into the queue
def producer(queue):
    for i in range(5):
        queue.put(f"Message {i}")
        print(f"Produced: Message {i}")

# Function to read data from the queue
def consumer(queue):
    while not queue.empty():
        message = queue.get()
        print(f"Consumed: {message}")

if __name__ == "__main__":
    # Create a shared queue
    shared_queue = Queue()

    # Create producer and consumer processes
    producer_process = Process(target=producer, args=(shared_queue,))
    consumer_process = Process(target=consumer, args=(shared_queue,))

    # Start the processes
    producer_process.start()
    producer_process.join()  # Wait for the producer to finish

    consumer_process.start()
    consumer_process.join()  # Wait for the consumer to finish

