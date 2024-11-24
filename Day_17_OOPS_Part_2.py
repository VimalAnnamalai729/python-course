from abc import ABC, abstractmethod


class BankAccount(ABC):
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self._balance = balance  # Protected attribute for encapsulation

    @abstractmethod
    def deposit(self, amount):
        """Deposit an amount to the account balance"""
        pass

    @abstractmethod
    def withdraw(self, amount):
        """Withdraw an amount from the account balance"""
        pass

    @abstractmethod
    def get_balance(self):
        """Return the current balance of the account"""
        pass


# Concrete class inheriting from abstract BankAccount
class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance=0, interest_rate=0.01):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self._balance

    def apply_interest(self):
        self.deposit(self._balance * self.interest_rate)


class CurrentAccount(BankAccount):
    def __init__(self, account_holder, balance=0, overdraft_limit=500):
        super().__init__(account_holder, balance)
        self.overdraft_limit = overdraft_limit

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self._balance + self.overdraft_limit:
            self._balance -= amount
        else:
            print("Overdraft limit exceeded")

    def get_balance(self):
        return self._balance


class SalaryAccount(BankAccount):
    def __init__(self, account_holder, balance=0):
        super().__init__(account_holder, balance)
        self.account_holder = account_holder
        self._balance = balance

    def withdraw(self, amount):
        pass

    def deposit(self, amount):
        pass

    def get_balance(self):
        pass

    def additional_features(self):
        pass

# Example Usage
savings = SavingsAccount("Alice", 1000, interest_rate=0.02)
current = CurrentAccount("Bob", 1500, overdraft_limit=300)

savings.deposit(200)
current.withdraw(1800)

print(savings.get_balance())
print(current.get_balance())
