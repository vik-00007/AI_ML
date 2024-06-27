
#***DICTIONARIES***
'''Dictionaries are unordered collections of items.
 They store data in key-value pairs. Keys must be unique and immutable (e.g. strings, numbers or tuple), which values can be of any type.
'''

## Creating Dictionaries
empty_dict={}
print(type(empty_dict))  # <class 'dict'>

empty_dict=dict()
print(empty_dict)  # {}

student={"name":"Souvik","age":19,"grade":24}
print(student)  # {'name': 'Souvik', 'age': 32, 'grade': 24}
print(type(student))  # <class 'dict'>

# Single key is always used
student={"name":"Souvik","age":32,"name":24}
print(student)  # {'name': 24, 'age': 32}

## accessing Dictionary Elements
student={"name":"Souvik","age":32,"grade":'A'}
print(student)  # {'name': 'Souvik', 'age': 32, 'grade': 'A'}

## Accessing Dictionary elements
print(student['grade'])  # 'A'
print(student['age'])  # 32

## Accessing using get() method
print(student.get('grade'))  # 'A'
print(student.get('last_name'))  # None
print(student.get('last_name',"Not Available"))  # 'Not Available'

## Modifying Dictionary Elements
## Dictionary are mutable, so you can add, update or delete elements
print(student)  # {'name': 'Souvik', 'age': 32, 'grade': 'A'}

student["age"]=19  ##update value for the key
print(student)  # {'name': 'Souvik', 'age': 19, 'grade': 'A'}
student["address"]="India" ## added a new key and value
print(student)  # {'name': 'Souvik', 'age': 19, 'grade': 'A', 'address': 'India'}

del student['grade'] ## delete key and value pair
print(student)  # {'name': 'Souvik', 'age': 19, 'address': 'India'}

## Dictionary methods

keys=student.keys() ##get all the keys
print(keys)  # dict_keys(['name', 'age', 'address'])
values=student.values() ##get all values
print(values)  # dict_values(['Souvik', 19, 'India'])

items=student.items() ##get all key value pairs
print(items)  # dict_items([('name', 'Souvik'), ('age', 19), ('address', 'India')])

## shallow copy
student_copy=student
print(student)  # {'name': 'Souvik', 'age': 19, 'address': 'India'}
print(student_copy)  # {'name': 'Souvik', 'age': 19, 'address': 'India'}

student["name"]="Souvik2"
print(student)  # {'name': 'Souvik2', 'age': 19, 'address': 'India'}
print(student_copy)  # {'name': 'Souvik2', 'age': 19, 'address': 'India'}

student_copy1=student.copy() ## shallow copy
print(student_copy1)  # {'name': 'Souvik2', 'age': 19, 'address': 'India'}
print(student)  # {'name': 'Souvik2', 'age': 19, 'address': 'India'}

student["name"]="Souvik3"
print(student_copy1)  # {'name': 'Souvik2', 'age': 19, 'address': 'India'}
print(student)  # {'name': 'Souvik3', 'age': 19, 'address': 'India'}

### Iterating Over Dictionaries
## You can use loops to iterate over dictionaries, keys, values, or items

## Iterating over keys
for key in student.keys():
    print(key)
# name
# age
# address

## Iterate over values
for value in student.values():
    print(value)
# Souvik3
# 19
# India

## Iterate over key value pairs
for key, value in student.items():
    print(f"{key}:{value}")
# name:Souvik3
# age:19
# address:India

## Nested Dictionaries
students={
    "student1":{"name":"Souvik","age":32},
    "student2":{"name":"Peter","age":35}
}
print(students)  # {'student1': {'name': 'Souvik', 'age': 32}, 'student2': {'name': 'Peter', 'age': 35}}

## Access nested dictionaries elements
print(students["student2"]["name"])  # 'Peter'
print(students["student2"]["age"])  # 35

print(students.items())  # dict_items([('student1', {'name': 'Souvik', 'age': 32}), ('student2', {'name': 'Peter', 'age': 35})])

## Iterating over nested dictionaries
for student_id, student_info in students.items():
    print(f"{student_id}:{student_info}")
    for key, value in student_info.items():
        print(f"{key}:{value}")
# student1:{'name': 'Souvik', 'age': 32}
# name:Souvik
# age:32
# student2:{'name': 'Peter', 'age': 35}
# name:Peter
# age:35

## Dictionary Comprehension
squares={x:x**2 for x in range(5)}
print(squares)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

## Condition dictionary comprehension
evens={x:x**2 for x in range(10) if x%2==0}
print(evens)  # {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

## Practical Examples

## Use a dictionary to count the frequency of elements in list

numbers=[1,2,2,3,3,3,4,4,4,4]
frequency={}

for number in numbers:
    if number in frequency:
        frequency[number]+=1
    else:
        frequency[number]=1
print(frequency)  # {1: 1, 2: 2, 3: 3, 4: 4}

## Merge 2 dictionaries into one

dict1={"a":1,"b":2}
dict2={"b":3,"c":4}
merged_dict={**dict1,**dict2}
print(merged_dict)  # {'a': 1, 'b': 3, 'c': 4}










