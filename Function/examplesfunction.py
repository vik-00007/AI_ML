
# Example 1: Temperature Conversion

def convertTemperature(temp, unit):
    """This function converts temperature between Celsius and Fahrenheit"""
    if unit == 'C':
        return temp * 9 / 5 + 32
    elif unit == 'F':
        return (temp - 32) * 5 / 9
    else:
        return None
    
print(convertTemperature(30, 'C'))  # Output: 86.0
print(convertTemperature(80, 'F'))  # Output: 26.666666666666668

# Example 2: Password Strength Checker

def is_strong_password(password):
    """This function checks if the password is strong or not"""
    if len(password) < 8:
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char in '!@#$%^&*()_+' for char in password):
        return False
    return True

## calling the function
print(is_strong_password("QwertY"))  # Output: False
print(is_strong_password("AaBc895%^@^55"))  # Output: True

# Example 3: Calculate Total Cost of Items in a Shopping Cart

def calculateTotalCost(cart):
    total = 0
    for item in cart:
        total += item['price'] * item['quantity']
    return total
    
cart = [
    {'name': 'Apple', 'price': 30, 'quantity': 4},
    {'name': 'Banana', 'price': 10, 'quantity': 6},
    {'name': 'Orange', 'price': 12, 'quantity': 3}
]

totalCost = calculateTotalCost(cart)
print(totalCost)  # Output: 198

# Example 4: Check if a String is Palindrome

def isPalindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

print(isPalindrome("A man a plan a canal Panama"))  # Output: True
print(isPalindrome("Souvik"))  # Output: False

# Example 5: Factorial using recursion

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
print(factorial(5))  # Output: 120

# Example 6: A function to read a file and count the frequency of each word

def count_word_frequency(file_path):
    word_count = {}
    with open(file_path, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                word = word.lower().strip('.,!?;:"\'')
                word_count[word] = word_count.get(word, 0) + 1
    
    return word_count

filepath = 'sample.txt'
word_frequency = count_word_frequency(filepath)
print(word_frequency)  # Output: (Depends on the contents of 'sample.txt')

# Example: Valid email address

import re

# Email validation function
def is_valid_email(email):
    """This function checks if the email is valid."""
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email) is not None

# Calling the function
print(is_valid_email("test@example.com"))  # Output: True
print(is_valid_email("invalid-email"))  # Output: False
