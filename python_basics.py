# comments in python
#------------------------------

#Comments can be used to explain Python code.
#Comments can be used to make the code more readable.
#Comments can be used to prevent execution when testing code.

# there are two types of comments in python 
# 1. single-line comment using # sign 
# 2.  multi-line comment also know as doc-string ou can add a 
# multiline string (triple quotes) in your code, and place your comment inside it:


# Example :- Single Line comment 
# this is a single line comment

# Example :- Multi Line comment
'''
This is a 
multi line
comment also 
know as doc-string
'''


# Loops in Python 
#---------------------------------
# 1.(loops are used to execute a block of code certian number times based on some condition 
#i.e., if the condtion is true the block of code execuate else the program  flow comes out of the loop)
# 2. loops are also used to  traverse/iterate over a iterable objects(list,tuple,dict,set)


#there are two types of loops in python
# 1. for loop
# 2. while loop

# for loop is used when we have to execute a block of code fixed number of times

#Example :- traversing over a list of employess
'''
employees = ['ram','shyam','sam','john','harry']

for employee in employees:
	print(employee)

Output :-
ram
shyam
sam
john
harry


'''


# while loop is used when we have to execute a block of code to unspecified number of times
# i.e., based on some conditon , So if the condition if True then the code is executed else
# the flow of execution of code comes out of that block of code

#Example :- printing only 3 employee from the list of 5 employees
'''
i = 0
employees = ['ram','shyam','sam','john','harry']

while(i < 3):
	print(employees[i])
	i += 1

Output :-
ram
shyam
sam



'''

# break,continue keyword
# break is used to exit the loop if a condition satified 
# continue is used to skip the current iteration

# Example :- break

# nums = [1,2,3,4,5,6,7]
# for i in nums:
# 	if i == 5:
# 		break
# 	print(i)

# Output:-
# 1
# 2
# 3
# 4

# Example :- continue

# nums = [1,2,3,4,5,6,7]
# for i in nums:
# 	if i == 5:
# 		continue
# 	print(i)

# Output :-
# 1
# 2
# 3
# 4
# 6
# 7

# pass keyword in python
# the pass keyword is used to execute nothing; it means, when we don't want to execute code, the pass can be used to execute empty
# it can be used when we just have to declare the function without giving its functionality

# Example:-

# def verify_email(email):
# 	pass



#  if,elif,else in python
# if,elif and else if used to execute a block of code in python if a certain condition evalueated to true
# an elif,else must be follwed by an if statement
# we can also have only if statement

# Example:-
# nums = [1,'2',3,4,'2',6,7,True,8,9,10]
# for i in nums:
# 	if type(i) is int:
# 		print(f"{i} is an integer")
# 	elif type(i) is str:
# 		print(f"{i} is an string")
# 	else:
# 		print(f"{i} is a boolean ")

# Output:-
# 1 is an integer
# 2 is an string
# 3 is an integer
# 4 is an integer
# 2 is an string
# 6 is an integer
# 7 is an integer
# True is a boolean 
# 8 is an integer
# 9 is an integer
# 10 is an integer
