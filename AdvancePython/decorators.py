
# Decorators
'''Decorators are powerful and fexible feature in Python that allows you to modify the behaviour of a function or class method.
They are commonly used to add functionality to functions or methods without modifying thier actual code. 
This lesson covers the basics of decorators, including how to create and use them.
'''

## function copy
## closures
## decorators

# function copy
def welcome():
    return "Hello World"

welcome()
wel = welcome
print(wel())
del welcome
print(wel())

# Hello World
# Hello World

# Closures functions
def main(msg):
    def sub():
        print("Welcome everyone")
        print(msg)
        print("Hello guys")
    return sub()

main("I love Python")

# Welcome everyone
# I love Python
# Hello guys

def main(func):

    def sub():
        print("I love Python")
        func("I love Machine Learning")
        print("I love AI")
    return sub()

main(print)

# I love Python
# I love Machine Learning
# I love AI

def main(func,lst):
    def sub():
        print("Hello World")
        print(func(lst))
        print("Have a good day")
    return sub()

main(len,[1,2,3,4,5,6])

# Hello World
# 6
# Have a good day

# Decorator
def main_welcome(func):
   
    def sub_welcome_method():
        print("Welcome to the advance python course")
        func()
        print("Please learn these concepts properly")
    return sub_welcome_method()

def coure_introduction():
    print("This is an advanced python course")

main_welcome(coure_introduction)

# Welcome to the advance python course
# This is an advanced python course
# Please learn these concepts properly

@main_welcome
def coure_introduction():
    print("This is an advanced python course")

# Welcome to the advance python course
# This is an advanced python course
# Please learn these concepts properly

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def hello():
    print("Hello World")

hello()

## Decorators WWith arguments
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator


@repeat(3)
def say_hello():
    print("Hello")

    say_hello()

    