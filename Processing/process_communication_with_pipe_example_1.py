"""
ALTERNATIVE COMMUNICATION USING PIPE
The Pipe object provides a two-way communication channel between two processes.

WHEN TO USE PIPE:
=================
    * Point-to-Point Communication:

        Use Pipe when there are only two processes that need to communicate directly.
        Example: A process sends commands to a child process and receives responses.
    * Simpler Communication:

        If the communication is straightforward, such as passing a few messages between two processes, Pipe is more efficient than Queue.
        Example: Sending a "start/stop" signal to a worker process.
    * Lower Overhead:

        Pipe is faster and has less overhead than Queue because it doesn’t involve a complex data structure.
        Example: Lightweight communication for high-speed message passing between two processes.
    * Two-Way Communication:

        The Pipe can act as a full-duplex channel where both processes can send and receive data.

"""
from multiprocessing import Process, Pipe

def sender(conn):
    for i in range(5):
        conn.send(f"Message {i}")
        print(f"Sent: Message {i}")
    conn.close()

def receiver(conn):
    while True:
        try:
            message = conn.recv()
            print(f"Received: {message}")
        except EOFError:
            break

if __name__ == "__main__":
    # Create a pipe
    parent_conn, child_conn = Pipe()

    # Create sender and receiver processes
    sender_process = Process(target=sender, args=(parent_conn,))
    receiver_process = Process(target=receiver, args=(child_conn,))

    # Start the processes
    sender_process.start()
    receiver_process.start()

    # Wait for processes to finish
    sender_process.join()
    receiver_process.join()
