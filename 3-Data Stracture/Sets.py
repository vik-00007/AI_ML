
#***SETS***
'''Sets are a built-in data type in python used to store collections of unique items.
 They are unordered, meaning that the elements do not follow a spefic order, and they do not allow duplicate elements.
 Sets are useful for membership tests, eliminating duplicate entries, and performing mathematical set operations like union, intersection, difference,
 and symmetric difference.

'''

# Create a set
my_set={1,2,3,4,5}
print(my_set)  # {1, 2, 3, 4, 5}
print(type(my_set))  # <class 'set'>

my_empty_set=set()
print(type(my_empty_set))  # <class 'set'>

my_set=set([1,2,3,4,5,6])
print(my_set)  # {1, 2, 3, 4, 5, 6}

my_empty_set=set([1,2,3,4,5,6])
print(my_empty_set)  # {1, 2, 3, 4, 5, 6}

# Basic Sets Operation
# Adding and Removing Elements
my_set.add(7)
print(my_set)  # {1, 2, 3, 4, 5, 6, 7}

my_set.remove(4)
print(my_set)  # {1, 2, 3, 5, 6, 7}

my_set.discard(5)
print(my_set)  # {1, 2, 3, 6, 7}

# Pop method
removeElement=my_set.pop()
print(removeElement)  # 1 (or another element, as sets are unordered)
print(my_set)  # {2, 3, 6, 7} (or without the removed element)

# Clear all the elements
my_set.clear()
print(my_set)  # set()

# Set Membership test
my_set={1,2,3,4,5,6}
print(3 in my_set)  # True
print(10 in my_set)  # False

# Mathematical Operator
set1={1,2,3,4,5,6}
set2={4,5,6,7,8,9}

# Union
unionSet=set1.union(set2)
print(unionSet)  # {1, 2, 3, 4, 5, 6, 7, 8, 9}

# Intersection
intersectionSet=set1.intersection(set2)
print(intersectionSet)  # {4, 5, 6}

set1.intersection_update(set2)
print(set1)  # {4, 5, 6}

set1={1,2,3,4,5,6}
set2={4,5,6,7,8,9}

# Difference
print(set1.difference(set2))  # {1, 2, 3}
print(set2.difference(set1))  # {8, 9, 7}

# Symmetric Difference
print(set1.symmetric_difference(set2))  # {1, 2, 3, 7, 8, 9}

# Sets Methods
set1={1,2,3,4,5}
set2={3,4,5}

# is subset
print(set1.issubset(set2))  # False
print(set2.issubset(set1))  # True

# is superset
print(set1.issuperset(set2))  # True
print(set2.issuperset(set1))  # False

lst=[1,2,2,3,4,4,5]
print(set(lst))  # {1, 2, 3, 4, 5}

# Counting Unique words in text

text="In this tutorial we are discussing about sets"
words=text.split()

# convert list of words to set to get unique words
unique_words=set(words)
print(unique_words)  # {'are', 'this', 'about', 'tutorial', 'sets', 'we', 'In', 'discussing'}
print(len(unique_words))  # 8


