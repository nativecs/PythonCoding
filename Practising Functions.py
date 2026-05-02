# today we are learning about functions in python.
# A function is a block of code that performs a specific task.
# It can take input, process it, and return an output. Functions help to organize code and make it reusable.

#def is called a function definition. It defines a function named welcome that takes no parameters and prints a welcome message.
# The function is then called by using its name followed by parentheses. When the function is called, the code inside the function is executed.
# we need parameters to make our functions more flexible and reusable.
# Parameters are placeholders for values that can be passed to the function when it is called.


def welcome():
    print("Welcome to the Python programming language!")

welcome()
def greet(name):
    name = input("What is your name? ")
    print(f"Hello, {name}!")
greet("")

def add_numbers(num1, num2):
    sum = num1 + num2
    return sum

# here are are putting the values 5 and 10 as arguments when calling the add_numbers function.
# The function will return the sum of these two numbers, which is then stored in the variable result and printed.
# this is reusable because we can call the add_numbers function with different arguments to get the sum of any two numbers without having to rewrite the code for addition each time.

result = add_numbers(5, 10)
print(result)

