

# Iterators
# Iterators are advanced python concepts that allow for efficient looping and memory management.
# Iterators provide a way to access elements of a collection sequentially without exposing the underlying structure.

my_list=[1,2,3,4,5,6]
for i in my_list:
    print(i)


# Iterator
it = iter(my_list)
print(type(it))

while True:
    try:
        print(next(it))
    except StopIteration:
        print("Ther are no elements in the iterator")
        break

# String Iterator

my_string = "Andromeda"
str_it = iter(my_string)
print(next(str_it)) # A
print(next(str_it)) # n
print(next(str_it)) # d




























