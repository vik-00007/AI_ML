
# THE FILTER FUNCTION

'''The filter() function constructs an iterator from elements of an iterable for which a function returns true.
    It is used to filter out items from a list(or any other iterable) based on a condition.'''


def even(num):
    if num % 2 == 0:
        return True

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

list(filter(even, lst))  # Output: [2, 4, 6, 8, 10, 12]

## filter with a Lambda Function
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
greater_than_five = list(filter(lambda x: x > 5, numbers))
print(greater_than_five)  # Output: [6, 7, 8, 9]

## Filter with a lambda function and multiple conditions
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_and_greater_than_five = list(filter(lambda x: x > 5 and x % 2 == 0, numbers))
print(even_and_greater_than_five)  # Output: [6, 8]

## Filter() to check if the age is greater than 25 in dictionaries
people = [
    {'name': 'Vik', 'age': 20},
    {'name': 'Jack', 'age': 33},
    {'name': 'John', 'age': 26}
]

def age_greater_than_25(person):
    return person['age'] > 25

list(filter(age_greater_than_25, people))  # Output: [{'name': 'Jack', 'age': 33}, {'name': 'John', 'age': 26}]






