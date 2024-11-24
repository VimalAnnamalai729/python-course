"""
1. Calculated Properties (Computed Attributes)
Scenario: When an attribute is derived from other attributes and does not need to be explicitly stored.
Example: Calculating the area of a rectangle dynamically.
"""


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height


rect = Rectangle(5, 10)
print(rect.area)  # Output: 50

"""
2. Encapsulation with Controlled Access
Scenario: To provide getter functionality without exposing the internal implementation.
Example: Accessing a private attribute indirectly.
"""


class Employee:
    def __init__(self, name):
        self._name = name  # Private variable

    @property
    def name(self):
        return self._name.title()


emp = Employee("john doe")
print(emp.name)  # Output: John Doe

"""
3. Validation on Setting Attributes
Scenario: To enforce rules when setting values to private/ protected attributes using @property and @<name>.setter.
Example: Validating a bank account balance.
"""


class BankAccount:
    def __init__(self, balance=0):
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, amount):
        if amount < 0:
            raise ValueError("Balance cannot be negative.")
        self._balance = amount


account = BankAccount()
account.balance = 100  # Valid
# account.balance = -50  # Raises ValueError
print(account.balance)  # Output: 100

"""
4: Ensuring Consistency Across Attributes
Scenario: Ensuring Consistency Across Account Balances in Different Currencies
Imagine a bank account where you can access your balance in USD or EUR. When you set the balance in one currency, 
the balance in the other currency should adjust automatically based on the exchange rate.
"""
class BankAccount:
    exchange_rate = 0.85  # 1 USD = 0.85 EUR (example rate)

    def __init__(self, balance_usd):
        self._balance_usd = balance_usd
        self._balance_eur = balance_usd * BankAccount.exchange_rate

    @property
    def balance_usd(self):
        return self._balance_usd

    @balance_usd.setter
    def balance_usd(self, value):
        if value < 0:
            raise ValueError("Balance cannot be negative.")
        self._balance_usd += value
        self._balance_eur = self._balance_usd * BankAccount.exchange_rate  # Update EUR balance

    @property
    def balance_eur(self):
        return self._balance_eur

    @balance_eur.setter
    def balance_eur(self, value):
        if value < 0:
            raise ValueError("Balance cannot be negative.")
        self._balance_eur += value
        self._balance_usd = self._balance_eur / BankAccount.exchange_rate  # Update USD balance

    def __str__(self):
        return f"Balance: ${self.balance_usd:.2f} (USD), €{self.balance_eur:.2f} (EUR)"

# Example Usage
account = BankAccount(100)  # Initial balance in USD
print(account)  # Output: Balance: $100.00 (USD), €85.00 (EUR)

# Update balance in USD
account.balance_usd = 200
print(account)  # Output: Balance: $200.00 (USD), €170.00 (EUR)

# Update balance in EUR
account.balance_eur = 255
print(account)  # Output: Balance: $300.00 (USD), €255.00 (EUR)


class Rectangle:

    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width


obj1 = Rectangle(4, 5)
print(obj1.width)
