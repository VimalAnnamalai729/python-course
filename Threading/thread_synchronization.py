import threading
import time

class BankAccount:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self, amount):
        with self.lock:  # Ensure only one thread modifies the balance at a time
            temp_balance = self.balance
            temp_balance += amount
            time.sleep(1)  # Simulate a delay
            self.balance = temp_balance
            print(f"Deposited {amount}, New Balance: {self.balance}")

# Shared resource
account = BankAccount()

# Multiple threads trying to access the shared resource
def transaction(amount):
    account.deposit(amount)

threads = [threading.Thread(target=transaction, args=(100,)) for _ in range(3)]

for t in threads:
    t.start()

for t in threads:
    t.join()
