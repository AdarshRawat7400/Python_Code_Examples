# Example 1:- csv writing 

import csv

f1 = open("emps.csv", "w")
csvreader = csv.writer(f1)

csvreader.writerow(["name","dept","loc"])
csvreader.writerow(["arun","sales","indore"])
csvreader.writerow(["ravi","purch","indore"])
csvreader.writerow(["chet","accts","bhopal"])
f1.close()

# file content:

# name	dept	loc
# arun	sales	indore
# ravi	purch	indore
# chet	accts	bhopal


# Example 2:- csv reading using reader
import csv

f1 = open("emps.csv", "r")
csvreader = csv.reader(f1)

for elem in csvreader:
   print(elem)

f1.close()

# Output :-

import csv

['name', 'dept', 'loc']
['arun', 'sales', 'indore']
['ravi', 'purch', 'indore']
['chet', 'accts', 'bhopal']


# Example 3:- csv reading using DictReader
import csv

f1 = open("emps.csv", "r")
csvreader = csv.DictReader(f1)

for elem in csvreader:
   print(elem)

f1.close()

# Output :-
{'name': 'arun', 'dept': 'sales', 'loc': 'indore'}
{'name': 'ravi', 'dept': 'purch', 'loc': 'indore'}
{'name': 'chet', 'dept': 'accts', 'loc': 'bhopal'}

