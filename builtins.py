# 1. Map
# map() is a built-in Python function that takes in two or more arguments:
# a function and one or more iterables, in the form:

# Example :-
lst_of_str_ints = ['1','2','3','4','5','6','7','8','9','10']
print("list of str ints :- ",lst_of_str_ints)

lst_of_ints = list(map(int, lst_of_str_ints))
print("list of ints :- ",lst_of_ints)

# Output :-
# list of str ints :-  ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
# list of ints :-  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# Example 2 :- using lambda function
lst_of_str_ints = ['1','2','3','4','5','6','7','8','9','10']
print("list of str ints :- ",lst_of_str_ints)

lst_of_ints = list(map(lambda x:int(x), lst_of_str_ints))
print("list of ints :- ",lst_of_ints)

# Output :-
# list of str ints :-  ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
# list of ints :-  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Example 3 :- temperature conversion
temps_in_celsius = [0, 22.5, 40, 100]
print("temprature in celsius :-",temps_in_celsius)

temps_in_fahrenheit = list(map(lambda celsius : (9/5)*celsius + 32, temps_in_celsius))
print("temprature in fahrenheit :-",temps_in_fahrenheit)

# Output :-
# temprature in celsius :- [0, 22.5, 40, 100]
# temprature in fahrenheit :- [32.0, 72.5, 104.0, 212.0]


# ================================


# 2. Filter
# filter(function, iterable)( offers a efficient way to filter out all the elements of an
# iterable,based on if a condition evaluates to true

# Example 1:- fitler ints from a list of object of various type
lst = [12, 43.42, 'hello', [1,3,4], 54,92, (1,2), 12.22, 9]
print("Orignal list of object without filteration :- ",lst)

lst_of_ints = list(filter(lambda x:type(x)== int, lst))
print("Updated list of ints  :- ",lst_of_ints)

# Output :-
# Orignal list of object without filteration :-  [12, 43.42, 'hello', [1, 3, 4], 54, 92, (1, 2), 12.22, 9]
# Updated list of ints  :-  [12, 54, 92, 9]


# Example 2 :- filter even integer from a list of integers
list_of_ints = [1,2,3,4,5,6,7,8,9,10]

print("Orignal list of ints :- ",list_of_ints)

list_of_even_ints = list(filter(lambda x: x % 2 ==0, list_of_ints))
print("Updated list of only even ints  :- ",list_of_even_ints)

# Output :- 
# Orignal list of ints :-  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Updated list of only even ints  :-  [2, 4, 6, 8, 10]    


# =========================================

# 3. Reduce
# The function reduce(function, sequence) continually applies the function to
# the sequence. It then returns a single value.

# Example 1 :- reduce a list of int to a single integer using + operator
from functools import reduce

lst =[47,11,42,13]
print("Original list :- ",lst)
print("reduced value :- ",reduce(lambda x,y: x+y,lst))

# Output :-
# Original list :-  [47, 11, 42, 13]
# reduced value :-  113

#Example 2 :- reduce a list of int to a single integer using * operator
from functools import reduce

lst =[47,11,42,13]
print("Original list :- ",lst)
print("reduced value :- ",reduce(lambda x,y: x*y,lst))

# Output :-
# Original list :-  [47, 11, 42, 13]
# reduced value :-  282282


# ======================================
# 4. zip    
# The function zip() makes an iterator that combines elements from each of the iterables.

# Example 1 :- we will combine user firstname,lastname,hometown using zip() function

first_names = ['ram','shyam','ajay','bipin','manoj','alex']
print("list of first names :- ", first_names,"\n")

last_names = ['gupta','tiwari','yadav','rawat','desai','khan','raven']
print("list of first names :- ", last_names,"\n")

home_towns = ['ayodhya','vrindavan','bihar','jhnasi','boston','delhi','lanka']
print("list of hometowns :-" , home_towns,"\n")


persons_info = list(zip(first_names,last_names,home_towns))
print("data after using zip() function :-",persons_info)

# Output :-
# list of first names :-  ['ram', 'shyam', 'ajay', 'bipin', 'manoj', 'alex'] 

# list of first names :-  ['gupta', 'tiwari', 'yadav', 'rawat', 'desai', 'khan', 'raven'] 

# list of hometowns :- ['ayodhya', 'vrindavan', 'bihar', 'jhnasi', 'boston', 'delhi', 'lanka'] 

# data after using zip() function :- [('ram', 'gupta', 'ayodhya'), ('shyam', 'tiwari', 'vrindavan'), ('ajay', 'yadav', 'bihar'), ('bipin', 'rawat', 'jhnasi'), ('manoj', 'desai', 'boston'), ('alex', 'khan', 'delhi')]


# ======================================

# 5. enumerate
# The function enumerate() return an iterates to a list of tuples ,
#  where first element of each tuple is it's corresponding index 
# by default is 0) and second element is the value at store at the index

# Example 1 :- without start argument
names = ['ram','shyam','ajay','bipin','manoj','alex']

names_with_indexes = list(enumerate(names))
for name in names_with_indexes:
  print(name)

# Output :-
# (0, 'ram')
# (1, 'shyam')
# (2, 'ajay')
# (3, 'bipin')
# (4, 'manoj')
# (5, 'alex')

# Example 2 :- with start argument
names = ['ram','shyam','ajay','bipin','manoj','alex']

names_with_indexes = list(enumerate(names, 4))
for name in names_with_indexes:
  print(name)

# Output :-
# (4, 'ram')
# (5, 'shyam')
# (6, 'ajay')
# (7, 'bipin')
# (8, 'manoj')
# (9, 'alex')

# =========================================

#  6. all()
# all() are built-in functions that allow us to conveniently 
# check for boolean matching in an iterable.

# Example 1:    
lst = [True,True,False,True]
print(all(lst))

# Output :-
# False

#Example 2:
lst = [True,True,True,True]
print(all(lst))

# Output :-
# True

# =========================================

# 7. any()
# any() are built-in functions that allow us to conveniently 
# check for boolean matching in an iterable.

# Example 1:
lst = [True,False,False,False]
print(any(lst))

# Output :-
# True


# Example 2:
lst = [False,False,False,False]
print(any(lst))

# Output :-
# False