# ***LISTS*** #
# Lists are ordered, mutable collections of items.
# They can contain items of different data types.

lst=[]
print(type(lst))     ##Output -> <class 'list'>

names =["Souvik","Ayan","Sneha",1,2,4,10]
print(names)         ##Output -> ['Souvik', 'Ayan', 'Sneha', 1, 2, 4, 10]

mixed_list=[5,"Hello",3.14,True]
print(mixed_list)    ##Output -> [5, 'Hello', 3.14, True]

## Accessing List Elements

fruits=["apple","banana","cherry","guava"]
print(fruits[0])   ## apple
print(fruits[2])   ## cherry
print(fruits[3])   ## guava
print(fruits[-1])  ## guava

print(fruits[1:])  ##['banana', 'cherry', 'guava']
print(fruits[1:3]) ##['banana', 'cherry']

## Modifying the list elements
fruits[2]="Watermelon"
print(fruits)      ## ['apple', 'banana', 'Watermelon', 'guava']

fruits[1:]="Mango"
print(fruits)      ## ['apple', 'M', 'a', 'n', 'g', 'o']

## List Methods
fruits = ["apple","banana","cherry","guava","mango"]

fruits.append("orange")  
print(fruits)            ## ['apple', 'banana', 'cherry', 'guava', 'mango', 'orange']

fruits.insert(1,"watermelon")
print(fruits)                  ## ['apple', 'watermelon', 'banana', 'cherry', 'guava', 'mango', 'orange']

fruits.remove("apple")
print(fruits)                  ## ['watermelon', 'banana', 'cherry', 'guava', 'mango', 'orange']

## Remove and return the last element
popped_fruits=fruits.pop()
print(popped_fruits)           ## orange
print(fruits)                  ## ['watermelon', 'banana', 'cherry', 'guava', 'mango']

index = fruits.index("cherry")
print(index)                   ## 2

fruits.insert(2,"banana")
print(fruits.count("banana"))  ## 2

fruits = ["apple","banana","cherry","guava","mango"]

print(fruits.sort())

print(fruits.reverse())

print(fruits.clear())

# Slice List

numbers = [1,2,3,4,5,6,7,8,9,10]

print(numbers[2:5])          ## [3, 4, 5]
print(numbers[:5])           ## [1, 2, 3, 4, 5]
print(numbers[5:])           ## [6, 7, 8, 9, 10]
print(numbers[::2])          ## [1, 3, 5, 7, 9]
print(numbers[::-1])         ## [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(numbers[::3])          ## [1, 4, 7, 10]
print(numbers[::-2])         ## [10, 8, 6, 4, 2]

## Iterating over list
numbers = [1,2,3,4,5,6,7,8,9,10]
for number in numbers:
    print(number)

## Iterating with index
numbers = [1,2,3,4,5,6,7,8,9,10]
for index,number in enumerate(numbers):
    print(index,number)
'''
0 1
1 2
2 3
3 4
4 5
5 6
6 7
7 8
8 9
9 10
'''    

## List comprehension
lst=[]
for i in range(10):
    lst.append(i**2)
print(lst)                        ## [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

print([i**2 for i in range(10)])  ## [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

## Basic List Comprhension

numbers = [1,2,3,4,5,6,7,8,9,10]
cube = [num**3 for num in range(11)]
print(cube)                        ## [0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]

## List Comprehension with condition

lst=[]
for i in range(10):
    if i%2==0:
        lst.append(i)

print(lst)          ## [0, 2, 4, 6, 8]

evenNumbers = [num for num in range(10) if num%2==0]
print(evenNumbers)  ## [0, 2, 4, 6, 8]

## Nested List Comphrension

lst1=[1,2,3]
lst2=['a','b','c']
pair=[[i,j] for i in lst1 for j in lst2]

print(pair)        ## [[1, 'a'], [1, 'b'], [1, 'c'], [2, 'a'], [2, 'b'], [2, 'c'], [3, 'a'], [3, 'b'], [3, 'c']]

## List Comprehension with function calls
words = ["hello","world","python","list"]
lengths = [len(word) for word in words]
print(lengths)     ## [5, 5, 6, 4]     
 














