# Example 1:-
students = [('Ram',50),('Shyam',67),('Ajay',96),('Bipin',65),('Manoj',45),('Alex',78)]
new_students = list(filter(lambda x: x[1]>=60,students))
print(new_students)

# Output :-
# [('Shyam', 67), ('Ajay', 96), ('Bipin', 65), ('Alex', 78)]

# Example 2:-
nums = [1,2,3,4,5,6,7,8,9,10]
nums_squared = list(map(lambda x: x**2, nums))
print(nums_squared)

# Output :-
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Example 3:-
names = ['Ram','Shyam','Abhiansh','Raven','Marcus']
print("Original list :-",names)

upper_cased_names = list(map(lambda x : x.upper(), names))
print("Upper case name :-",upper_cased_names)

# Output :-
# Original list :- ['Ram', 'Shyam', 'Abhiansh', 'Raven', 'Marcus']
# Upper case name :- ['RAM', 'SHYAM', 'ABHIANSH', 'RAVEN', 'MARCUS']