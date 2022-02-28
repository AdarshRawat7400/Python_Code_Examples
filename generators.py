# Generator are the special function which returns an traversal
#  object which used to iterate over a collection of values, it is 
# also used to create iterators.

# It is can also be expressed in a way which is simiar to list compreshension

# Just like iterator next() method we can also iterate over generator
#  using generator.next() to iterate over the generator.


# Example 1:- Differnce b/w normal function and generator function
# Normal function
def func():
    letters = ['a', 'b', 'c', 'd', 'e']
    for c in letters:
        return c

# Generator function
def generator_func():
    letters = ['a', 'b', 'c', 'd', 'e']
    for c in letters:
        yield c

print("Normal function :-")
print(func())

print("\nGenerator function :-")
print(generator_func())

print("\nIterating over generator using next() method")
gen = generator_func()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

# Output :-


# Normal function :-
# a

# Generator function :-
# <generator object generator_func at 0x00000180318F9A10>

# Iterating over generator using next() method
# a
# b
# c
# d



# Example 2:- Iterativing over generator using for loopfor i in generator_func():
for i in generator_func():
    print(i)

# Output :-
# a
# b
# c
# d
# e


# Example 3:- Generator with multiple yield statements
def generator_func2():
    numbers = [1, 2, '3', '4', 5, 6, '7', 8, 9, '10']
    for num in numbers:
        if type(num) == int:
            yield f"{num} is an integer form"
        elif type(num) == str:
            yield f"{num} is an string form"



for i in generator_func2():
    print(i)


# Output :-
# 1 is an integer form
# 2 is an integer form
# 3 is an string form
# 4 is an string form
# 5 is an integer form
# 6 is an integer form
# 7 is an string form
# 8 is an integer form
# 9 is an integer form
# 10 is an string form


# Example 4. :- we use ( ) to create a generator 

# numbers_generator = (i for i in range(10))
# print(type(numbers_generator))

# for num in numbers_generator:
#     print(num)

# Output :-
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9

# Example 5. :- implement our own range() function with the help of generators.

# def range(start = 0,stop = 0,stepby = 1):
#     yield start
#     while(start < stop):
#         yield start+stepby
#         start += stepby

# print("range() function implementation :-")
# print(type(range(0,10)))


# for i in range(0,10):
#     print(i)

# print("\n---------\n")

# for i in range(0,10,2):
#     print(i)

# Output :-
# range() function implementation :-
# <class 'generator'>
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10

# ---------

# 0
# 2
# 4
# 6
# 8
# 10



