# Example 1:- writing to file
file = open("students.txt",'w')
student_info = { 
    "Name" : "Mike Javen",
    'Age' : 15,
    'City' : 'Minisoda'
}

for field,data in student_info.items():
    file.write(f"{field} : {data}  \n")

file.close()

# students_2.txt file content :-

# Name : Mike Javen  
# Age : 15  
# City : Minisoda  


'''
File Content:-
Name : Ram Kumar
Age  : 13
City : Ajmir

Name : Alice Pen
Age  : 12
City : Boston

Name : Marcus Lee
Age  : 15
City : Tokyo
'''

#Example 2:- appending to file
file = open("students.txt",'a')
students_info = [ { 
    "Name" : "John Lenon",
    'Age' : 14,
    'City' : 'Navi Mumbai'    
 }, 
 { 
    "Name" : "Sam Dune",
    'Age' : 11,
    'City' : 'Boston'    
 }
]

for student_info in students_info:
    file.write("\n")
    for field,data in student_info.items():
        file.write(f"{field} : {data}  \n")

file.close()

# Students.txt file.content :-

# Name : Ram Kumar
# Age  : 13
# City : Ajmir

# Name : Alice Pen
# Age  : 12
# City : Boston

# Name : Marcus Lee
# Age  : 15
# City : Tokyo

# Name : John Lenon  
# Age : 14  
# City : Navi Mumbai  

# Name : Sam Dune  
# Age : 11  
# City : Boston  



# Example 3:- deleting a file

import os

filename = 'students_2.txt'
os.remove(filename)

print(f"successfully deleted file {filename}")

# Output :-
# successfully deleted file students_2.txt


# Example 4:- reading from a file
with open("students.txt",'r') as file:
    for line in file:
        print(line, end="")

# Output :-
# Name : Ram Kumar
# Age  : 13
# City : Ajmir

# Name : Alice Pen
# Age  : 12
# City : Boston

# Name : Marcus Lee
# Age  : 15
# City : Tokyo

# Name : John Lenon
# Age : 14
# City : Navi Mumbai

# Name : Sam Dune
# Age : 11
# City : Boston
