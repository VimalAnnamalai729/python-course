import threading
import time

class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        # No lock used here
        temp_balance = self.balance
        time.sleep(1)  # Simulate a delay
        temp_balance += amount
        self.balance = temp_balance
        print(f"Deposited {amount}, New Balance: {self.balance}")

    def withdraw(self, amount):
        # No lock used here
        if self.balance >= amount:
            temp_balance = self.balance
            time.sleep(1)  # Simulate a delay
            temp_balance -= amount
            self.balance = temp_balance
            print(f"Withdrew {amount}, New Balance: {self.balance}")
        else:
            print(f"Insufficient funds to withdraw {amount}, Current Balance: {self.balance}")

# Shared bank account
account = BankAccount()

# Multiple threads performing deposit and withdrawal
def deposit_task(amount):
    account.deposit(amount)

def withdraw_task(amount):
    account.withdraw(amount)

# Create threads
threads = [
    threading.Thread(target=deposit_task, args=(100,)),
    threading.Thread(target=withdraw_task, args=(50,)),
    threading.Thread(target=withdraw_task, args=(100,)),
]

# Start threads
for t in threads:
    t.start()

# Wait for all threads to finish
for t in threads:
    t.join()

print(f"Final Balance: {account.balance}")

