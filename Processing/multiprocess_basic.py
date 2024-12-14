from multiprocessing import Process
import time

# Function to calculate the square of a number
def calculate_square(number):
    time.sleep(20)
    print(f"Square of {number}: {number * number}")


if __name__ == "__main__":
    # List of numbers
    numbers = [1, 2, 3, 4, 5]

    # List to hold process objects
    processes = []

    # Create and start a process for each number
    for num in numbers:
        process = Process(target=calculate_square, args=(num,))
        processes.append(process)
        process.start()

    # Wait for all processes to complete
    for process in processes:
        process.join()

    print("All processes completed.")

'''
Advantages of Multiprocessing:
    1) Effective for CPU-bound tasks (e.g., mathematical computations, image processing).
    2) Takes advantage of multiple CPU cores for parallel execution.
'''