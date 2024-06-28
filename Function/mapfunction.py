
# THE MAP FUNCTION IN PYTHON
'''The map function applies a given function to all items in an input
list (or any other iterable) and returns a map object(an iterator).
This is particularly useful for transforming data in a list comprehensively.'''

def square(x):
    return x * x

square(10)  # Output: 100

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

list(map(square, numbers))  # Output: [1, 4, 9, 16, 25, 36, 49, 64]

## Lambda function with map
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
list(map(lambda x: x * x, numbers))  # Output: [1, 4, 9, 16, 25, 36, 49, 64]

### Map multiple iterables

numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]

added_numbers = list(map(lambda x, y: x + y, numbers1, numbers2))
print(added_numbers)  # Output: [5, 7, 9]

## map() to convert a list of strings to integers
# Use map to convert strings to integers
str_numbers = ['1', '2', '3', '4', '5']
int_numbers = list(map(int, str_numbers))

print(int_numbers)  # Output: [1, 2, 3, 4, 5]

words = ['apple', 'banana', 'cherry']
upper_word = list(map(str.upper, words))
print(upper_word)  # Output: ['APPLE', 'BANANA', 'CHERRY']

def get_name(person):
    return person['name']

people = [
    {'name': 'Souvik', 'age': 20},
    {'name': 'Rohan', 'age': 21}
]
list(map(get_name, people))  # Output: ['Souvik', 'Rohan']
