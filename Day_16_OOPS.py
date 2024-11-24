"""
class
    self,
    constructor
    destructor
    class variable
    instance variable
objects
    gettattr(), settattr(), delattr(), hasattr()
Abstraction
Inheritance
    single inheritance
    Multiple inheritance
    Multilevel inheritance
    Hybrid inheritance
    hierarchical inheritance
Encapsulation
    Private
    Public
    Protected
Polymorphism
    Method Overloading
    Method Overriding

@classmethod
@staticmethod
@property


# SOLID Principles
"""


class Arithemetic:

    info = 'I will perform arithemetic operations'

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def print_msg(self):
        print("Showing how self works here")

    def add(self):
        self.print_msg()
        return self.num1 + self.num2

    def sub(self):
        # pass
        return self.num1 - self.num2

    def mul(self):
        return self.num1 * self.num2

    def div(self):
        return self.num1 / self.num2

    # def __del__(self):
    #     pass


vic_obj = Arithemetic(5, 6)
yog_obj = Arithemetic(10, 20)


vic_obj.add()
