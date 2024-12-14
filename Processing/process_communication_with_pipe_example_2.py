from multiprocessing import Process, Pipe

def worker(conn):
    while True:
        message = conn.recv()
        if message == "STOP":
            break
        print(f"Received: {message}")
        conn.send(f"Processed {message}")

if __name__ == "__main__":
    parent_conn, child_conn = Pipe()
    p = Process(target=worker, args=(child_conn,))
    p.start()

    parent_conn.send("Task 1")
    print(parent_conn.recv())  # Receive processed response

    parent_conn.send("Task 2")
    print(parent_conn.recv())  # Receive processed response

    parent_conn.send("STOP")
    p.join()
