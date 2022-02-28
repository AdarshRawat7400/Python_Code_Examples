# Datatypes in Python (string, list, tuple, dictionary, datetime)

#1. string
# string :- array of letter(immutable) support all string operation
# concating two string ,iterating of letter in string,reverse the string
# All other builtin function of strings are.capatilize(),.upper(),.lower() and so on

'''
string = "Name is Adarsh Rawat"
print("\n")
print("String = ",string)
print("Some Operration of String :- ")
print("string.capatilize() (capatalize a String) :- ",string.capitalize())
print("string.upper() (change letter to UpperCase in aString) :- ",string.upper())
print("string.lower() (change letter to LowerCase in aString) :- ",string.lower())
print(" + (add two String to Form new String) :- ",string+" and I'm 21 years Old")


Output :-

String =  Name is Adarsh Rawat
Some Operration of String :- 
string.capatilize() (capatalize a String) :-  Name is adarsh rawat
string.upper() (change letter to UpperCase in aString) :-  NAME IS ADARSH RAWAT
string.lower() (change letter to LowerCase in aString) :-  name is adarsh rawat
 + (add two String to Form new String) :-  Name is Adarsh Rawat and I'm 21 years Old



#2. list
# Lists are used to store multiple items in a single variable.
# List is mutable object means we can change it state without creating a new object 
# we can add,delete,merge two list and perform various operation on it 
# some mainly used list methods are (append,clear,remove,reverse,sort,extend,count,pop)
# Example :-

nums = [1,2,3,4,5,6,7,8,9,10]
print(f"List - {nums}")

nums.append(11)
print(f"Adding element to a list using append method :- {nums}")

nums.remove(4)
print(f"Removing the first item with the specified value  using remove method :- {nums}")

nums.reverse()
print(f"Reversing the order of the list using reverse method :- {nums}")

nums.sort()
print(f"Sorting the element of list using sort method :- {nums}")

print(f"Printing the number of elements with the specified value using count method value(3) :- {nums.count(3)}")

nums.pop(2)
print(f"Removing the element at the specified position (2) using pop method :- {nums.pop(2)}")

nums2 = [12,13,15]
nums.extend(nums2)
print(f"Merging two list using extend method :-{nums}")

nums.clear()
print(f"Deleting all element from  a list using clear method :- {nums}")

# Output :-
# List - [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Adding element to a list using append method :- [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# Removing the first item with the specified value  using remove method :- [1, 2, 3, 5, 6, 7, 8, 9, 10, 11]
# Reversing the order of the list using reverse method :- [11, 10, 9, 8, 7, 6, 5, 3, 2, 1]
# Sorting the element of list using sort method :- [1, 2, 3, 5, 6, 7, 8, 9, 10, 11]
# Printing the number of elements with the specified value using count method value(3) :- 1
# Removing the element at the specified position (2) using pop method :- 5
# Merging two list using extend method :-[1, 2, 6, 7, 8, 9, 10, 11, 12, 13, 15]
# Deleting all element from  a list using clear method :- []




3. Dictionary

#Dictionaries are used to store data values in key:value pairs.
#it can only have unique keys
# we can add,delete,sort,print keys,print values, and iterate over dictinary
# we can create dict using curly braces {key:value,key:value} or using dict() method 

# Example :-
points_table = {'ram': 80, 'shyam': 100, 'bharat': 70,'sita': 90}


points_table['sam'] = 120
print(f"Adding new key value pair in dict :-{points_table}")

print(f"Finding value of key 'ram' using [] braces :- {points_table['ram']})")

print(f"Finding value of 'ram' using get method :- {points_table.get('ram')}")

print(f"Deleting key value pair using pop method :- {points_table.pop('ram')}")

print(f"Updating value of key 'sita' using update method :- {points_table.update({'sita':120})}")

print(f"Removing the last key value pair using popitem method :- {points_table.popitem()}")

print(f'Getting all the values of the dict using values method :- {points_table.values()}')

print(f"Getting all the keys of the dict using keys method :- {points_table.keys()}")

print(f"Printing all the key value pairs using items method :- {points_table.items()}")


# Output :-

# Adding new key value pair in dict :-{'ram': 80, 'shyam': 100, 'bharat': 70, 'sita': 90, 'sam': 120}
# Finding value of key 'ram' using [] braces :- 80)
# Finding value of 'ram' using get method :- 80
# Deleting key value pair using pop method :- 80
# Updating value of key 'sita' using update method :- None
# Removing the last key value pair using popitem method :- ('sam', 120)
# Getting all the values of the dict using values method :- dict_values([100, 70, 120])
# Getting all the keys of the dict using keys method :- dict_keys(['shyam', 'bharat', 'sita'])
# Printing all the key value pairs using items method :- dict_items([('shyam', 100), ('bharat', 70), ('sita', 120)])


#4. Tuple
#Tuples are used to store multiple items in a single variable.
#A tuple is a collection which is ordered and unchangeable.
#it is immutable
#it is created using () braces

#Example :-
tple = ("Adarsh",'22','Information Technology','Gammastack')
print(tple)
print(f"access tuple items by referring to the index number, inside square brackets:- {tple[0]}")
print(f"access tuple items by referring to the index number, inside square brackets using negative indexing :- {tple[-1]}")
print(f"deleting element from the tuple using del keyword :- {del tple[1]}")
print(tple)
print(f"counting occurenace of number using count method :- {tple.count("Gammastack")}")

# Output :-
# ('Adarsh', '22', 'Information Technology', 'Gammastack')
# access tuple items by referring to the index number, inside square brackets:- Adarsh
# access tuple items by referring to the index number, inside square brackets using negative indexing :- Gammastack
# counting occurenace of number using count method :- 1





# 5. datetime

# python datetime module have mainly 6 main classes
1. date, 2. time,  3. datetime, 4. timedelta , 5. tzinfo , 6. timezone 

Example :-
from datetime import date

# format year, month, date
my_date = date(2022, 1, 5)
print("Date passed as argument is", my_date)

#get current date
today = date.today()
print(f"today date :- {today}")

#get year,month,day seperately
print(today.day)
print(today.month)
print(today.year)

#get today timestamp
from datetime import datetime
print(datetime.now())

Output :-
today date :- 2022-01-05
Date passed as argument is 2022-01-05
5
1
2022
2022-01-05 13:30:40.183532





'''