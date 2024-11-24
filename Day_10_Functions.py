"""
def <func_name>(arguments/parameters/function_input):
    # code logic
    pass
"""
"""
1) Declare functions
2) Return values
3) Functions with arguments
4) Functions with 
            posistional arguments,
            keywords argument, 
            default argument, 
            variable length argument, keyword variable lenght argument
5) scope of variable # global , local, nonlocal # Done
6. Docstrings # Done
7. Closure Functions # Done
8. First Class Functions # Done
9. Functions as Decorators # Done # Doubt discussion pending
10. lambda functions # Done
11.  Recursive Functions.# Done
12. Generator Functions  # Done
"""

'''
# called by caller
def find_vowels_count(input_string):
    vowels = 'aeiou'

    count = 0
    for char in input_string:
        if char in vowels:
            count += 1

    return count


# caller
# result = find_vowels_count('vimal')
# print(result)


def divide(num, den=2):
    """
    This function will divide given two numbers

    :param num: integer value
    :param den: integer value
    :return: interger
    """
    print(f'num value is {num}')
    print(f'den value is {den}')
    return num / den


# print(help(divide))
# result = divide(5, 6)  # positional argument
# print(result)
#
# result = divide(den=6, num=7)  # Keyword argument
# print(result)

# result = divide(5, 4)  # default argument
# print(result)


def addition(*args, **kwargs):  # variable length argument
    print(f"args : {args}")
    print(f"kwargs : {kwargs}")
    # return sum(args)


# value = addition(4, 10, a=34, b=45)
# print(value)
#
# value = addition(c=56)
# print(value)
# #
# value = addition(i=56, a=4, b=23, d=67, c=89)
# print(value)


def check():
    print('Hello are you calling me')


# first class functions
# def parent(func):
#     num = 20
#     func()
#     print('parent function num: ', num)
#
# object1 = parent
# object1(check)

def validate(func):
    print('STEP 1')
    def check(num, den):
        if den == 0:
            print('denominator must be greater than zero')
            return
        return func(num, den)
    return check

@validate
def division(num, den):
    return num / den


print(division(6, 2))


# Before executing certain function, i need to perform certain logic
# Incase you don't wnat re-write or modify the existing function code
# but still you need to validation or additonal logic before that.

"""
In Python, the global, local, and nonlocal keywords are used to define the scope of variables, which determines where a variable is accessible within the code. Here’s a quick breakdown of each:

1. Local Variables
Definition: A variable defined inside a function and accessible only within that function.

Scope: Only within the function where it's defined.

Example:
"""
def my_function():
    x = 10  # Local variable
    print(x)  # Outputs: 10

my_function()
# print(x)  # Error: x is not defined outside of the function

"""
2. Global Keyword
Definition: Used to declare a variable as global inside a function, giving access to a variable that’s defined at the module level (outside any function).

Scope: Accessible both inside and outside functions.

Purpose: Allows modification of a global variable inside a function.

Example:
"""

x = 20  # Global variable

def my_function():
    global x
    x = 10  # Modifies the global x
    print(x)  # Outputs: 10

my_function()
print(x)  # Outputs: 10, because x was modified in the function


"""
3. Nonlocal Keyword
Definition: Used inside nested functions to declare a variable from the enclosing (non-global) scope.

Scope: Gives access to variables in the nearest enclosing scope that is not global.

Purpose: Allows modification of a variable in the outer function from within an inner (nested) function.

Example:
"""

def outer_function():
    x = 5  # Enclosing variable

    def inner_function():
        nonlocal x
        x = 10  # Modifies the x in outer_function
        print("Inner x:", x)  # Outputs: 10

    inner_function()
    print("Outer x:", x)  # Outputs: 10 because inner_function modified it

outer_function()


""


"""
RECURSIVE FUNCTIONS
Example: Sum of Numbers
"""
def sum_of_numbers(n):
    # Base case: if n is 0, the sum is 0
    if n == 0:
        return 0
    # Recursive case: n + sum of numbers up to (n - 1)
    else: # 5 + func_cal(4)
        return n + sum_of_numbers(n - 1)

# Example usage
output = sum_of_numbers(0)  # Output: 15 (because 5 + 4 + 3 + 2 + 1 + 0 = 15)
print(output)
'''



# Normal Function
def send_numbers(num):
    result = []
    for i in range(num):
        result.append(i)
    return result


# print(send_numbers(5))

# Generator Functions

def send_numbers2(num):
    for i in range(num):
        yield i


result = send_numbers2(5)
for i in result:
    print(i)
