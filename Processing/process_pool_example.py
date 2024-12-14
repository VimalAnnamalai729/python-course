"""

Process Pool in Python
The multiprocessing.Pool class in Python provides a high-level API for parallel processing using a pool of worker processes.
It is particularly useful when you need to perform the same task across multiple data items concurrently.

KEY FEATURES OF PROCESS POOL:
    * Worker Process Management:
        The pool manages a fixed number of worker processes.
        Tasks are distributed to these processes, reusing them for multiple tasks.

    * Simplified Parallelism:

        Reduces the complexity of creating and managing individual processes.
    * Efficient Task Execution:

        Suitable for CPU-bound tasks, such as mathematical computations or data processing, that benefit from parallel execution.
    * Concurrency Control:

        The number of concurrent processes is controlled by the processes parameter.

REAL-WORLD USE CASES:
=====================
    * Data Processing Pipelines:

        Applying the same transformation (e.g., resizing images, cleaning text, or performing computations)
        to a large dataset in parallel.

    * Mathematical Simulations:
        Running multiple iterations of complex simulations (e.g., Monte Carlo simulations) concurrently.

    * Web Scraping:
        Fetching data from multiple URLs simultaneously using a pool of processes to handle HTTP requests.

    * Batch Processing:

        Dividing large workloads (e.g., analyzing log files or training models on subsets of data) into smaller tasks
        distributed among processes.

CORE METHODS OF PROCESS POOL:

    apply():
        Executes a single function call in a worker process and blocks until the result is returned.
        Useful for executing tasks sequentially in the pool.

    * apply_async():
        Executes a single function call asynchronously.
        Returns a AsyncResult object to retrieve the result later.

    * map():
        Distributes a function to multiple data items and collects the results.
        Equivalent to the built-in map() function but processes items in parallel.

    * map_async():
        Asynchronous version of map() that doesn’t block the main process.

    * starmap():
        Similar to map(), but allows functions with multiple arguments.
"""

from multiprocessing import Pool
import time

def calculate_square(n):
    """Function to calculate the square of a number."""
    time.sleep(1)  # Simulate a time-consuming task
    return n * n

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]

    # Create a process pool with 3 workers
    with Pool(processes=3) as pool:
        # Use map to distribute the work among the workers
        results = pool.map(calculate_square, numbers)

    print(f"Input Numbers: {numbers}")
    print(f"Squares: {results}")
