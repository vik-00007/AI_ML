
# FUNCTION
''' A function is a block of code that performs a specific task.
 Functions help in organizing code, reusing code and improving readability.'''

# ## Syntax
# def functionName(parameters):
#     """Docstring"""
#     #Function body
#     return expression

def even_or_odd(num):
    """This function finds even or odd"""
    if num % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")

# Call this function
even_or_odd(8)  # Output: The number is even

# Function with multiple parameters

def add(a, b):
    return a + b
result = add(10, 5)
print(result)  # Output: 15

# Default parameters

def greet(name):
    print(f"Hello {name}, Welcome")

greet("Souvik")  # Output: Hello Souvik, Welcome

def greet(name="Guest"):
    print(f"Hello {name} welcome")

greet("Neha")  # Output: Hello Neha, Welcome

# Variable length arguments
# Positional and keywords arguments

def printNumber(*args):
    for number in args:
        print(number)

printNumber(1, 2, 3, 4, 5, 6, "Souvik")  
# Output:
# 1
# 2
# 3
# 4
# 5
# 6
# Souvik

# Key word arguments

def printDetails(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}:{value}")

printDetails(name="Souvik", age="20", country="India")
# Output:
# name:Souvik
# age:20
# country:India

def printDetails(*args, **kwargs):
    for val in args:
        print(f"Positional argument: {val}")
    for key, value in kwargs.items():
        print(f"{key}:{value}")

printDetails(1, 2, 3, 4, "Souvik", name="Souvik", age="20", country="India")
# Output:
# Positional argument: 1
# Positional argument: 2
# Positional argument: 3
# Positional argument: 4
# Positional argument: Souvik
# name:Souvik
# age:20
# country:India

# Return Statement

def multiply(a, b):
    return a * b, a

multiply(5, 6)  # Output: (30, 5)
