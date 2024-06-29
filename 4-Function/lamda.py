
# LAMBDA FUNCTION IN PYTHON
'''Lambda functions are small anonymous functions defined using the lambda
keyword. They can have any number of arguments but only one expression. They are commonly used for 
short operations or as arguments to higher-order functions.'''

#Syntax

# lambda arguments:expresion

def add(a,b):
    return a+b
add(3,5)  # Output: 8

addition = lambda a,b: a+b
type(addition)  # Output: <class 'function'>
print(addition(10,20))  # Output: 30

def even(num):
    if num%2 == 0:
        return True

even(24)  # Output: True

even1 = lambda num: num%2 == 0
even1(12)  # Output: True

def addition(x, y, z):
    return x + y + z

addition(12, 13, 14)  # Output: 39

addition1 = lambda x, y, z: x + y + z
addition1(12, 13, 14)  # Output: 39

# map() -> applies a function to all items in a list

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def square(number):
    return number**2

square(3)  # Output: 9

list(map(lambda x: x**2, numbers))  # Output: [1, 4, 9, 16, 25, 36, 49, 64, 81]
