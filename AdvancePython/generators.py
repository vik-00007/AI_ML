
# Generators
'''Generators are a simpler way to create iterators. They use the yield keyword to produce a series of values lazily, 
   which means they generate values on the fly and do not store them in memory.
   
 Iterators and generators are powerful tools in Python for creating and handling sequences of data efficiently.
 Iterators provide a way to access elements sequentially, while generators allow you to generate items on the fly,
 making them particularly useful for handling large datasets and infinite sequences.
 Understanding these concepts will enable you to write more efficient and memory-conscious Python programs.
   '''

def square_generator(n):
    num = 1
    while num <= n:
        yield num ** 2
        num += 1

# Using the generator to print square numbers up to 20
sq_gen = square_generator(20)
for sq in sq_gen:
    print(sq)


def evenNumber(n):
    i=1
    while n:
        yield 2*i
        i+=1
        n-=1
it = evenNumber(20)
even=[]

while True:
    try:
        even.append(next(it))
    except StopIteration:
        break



















