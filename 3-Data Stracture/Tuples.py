
#***TUPLES***
## Tuples are ordered collections of items that are immutable. They are similar to lists, but their immutability makes them different.

# Creating a tuple
empty_tuple=()
print(empty_tuple)  # ()
print(type(empty_tuple))  # <class 'tuple'>

lst=list()
print(type(lst))  # <class 'list'>
tpl=tuple()
print(type(tpl))  # <class 'tuple'>

numbers=tuple([1,2,3,4,5,6,7,8])
print(numbers)  # (1, 2, 3, 4, 5, 6, 7, 8)

print(list((1,2,3,4,5,6,7,8)))  # [1, 2, 3, 4, 5, 6, 7, 8]

mixed_tuple=(1,"Hello World",True,3.14)
print(mixed_tuple)  # (1, 'Hello World', True, 3.14)

## Accessing Tuple Elements
numbers = tuple([1,2,3,4,5,6,7,8,9])
print(numbers[2])  # 3
print(numbers[-1])  # 9

print(numbers[0:4])  # (1, 2, 3, 4)
print(numbers[::-1])  # (9, 8, 7, 6, 5, 4, 3, 2, 1)

## Tuple Operations

concatenation_tuple=numbers+mixed_tuple
print(concatenation_tuple)  # (1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 'Hello World', True, 3.14)

print(mixed_tuple * 3)  # (1, 'Hello World', True, 3.14, 1, 'Hello World', True, 3.14, 1, 'Hello World', True, 3.14)

# Immutable Nature of Tuples
## Tuples are immutable, meaning their elements cannot be changed once assigned.

lst=[1,2,3,4,5,6]
print(lst)  # [1, 2, 3, 4, 5, 6]

lst[1]="Souvik"
print(lst)  # [1, 'Souvik', 3, 4, 5, 6]

numbers[1]="Souvik"  # TypeError: 'tuple' object does not support item assignment

#Tuple methods
numbers=(1,2,1,3,4,5,6)
print(numbers.count(1))  # 2
print(numbers.index(3))  # 3

# Packing and unpacking tuple
packed_tuple=1,"Hello",3.14
print(packed_tuple)  # (1, 'Hello', 3.14)

# Unpacking a tuple
a,b,c=packed_tuple
print(a)  # 1
print(b)  # Hello
print(c)  # 3.14

# Unpacking with *
numbers=(1,3,5,7,9)
first,*middle,last=numbers
print(first)  # 1
print(middle)  # [3, 5, 7]
print(last)  # 9

# Nested Tuple
# Nested List
lst=[[1,2,3,4],[5,6,7,8],["Hello",10,11,12]]
print(lst[0][0:3])  # [1, 2, 3]
print(lst[2][0:3])  # ['Hello', 10, 11]

nested_tuple = ((1,2,3,),("a","b","c"),(True,False))
# access the elements inside a tuple
print(nested_tuple[0])  # (1, 2, 3)
print(nested_tuple[1][2])  # c

## Iteration over nested tuples
for sub_tuple in nested_tuple:
    for item in sub_tuple:
        print(item,end="")
    print()    
# 123
# abc
# TrueFalse

