from sqlalchemy import create_engine , MetaData, Table, Column, Integer, String
engine = create_engine('sqlite:///students.db', echo = True)


'''
To specifically mention DB-API to be used for connection, 
the URL string takes the form as follows −
dialect[+driver]://user:password@host/dbname
'''


# Create a MetaData instance
metadata = MetaData()

# Creating a table
students = Table('students', metadata,
                Column('id', Integer, primary_key = True),
                Column('name', String(50)), 
                Column('major', String(50)),
                Column('gpa', String(50)))

# Create the table in the database
metadata.create_all(engine)


# Inserting data into the table
ins = students.insert().values(name = 'Ram', major = 'CS', gpa = '4.0')
conn = engine.connect()
result = conn.execute(ins)
# Execute the statement
conn = engine.connect()
result = conn.execute(ins)


# Inserting multiple rows
conn.execute(students.insert(), [
    {'name': 'Ram', 'major': 'CS', 'gpa': '4.0'},
    {'name': 'Shyam', 'major': 'CS', 'gpa': '3.5'},
    {'name': 'Mohan', 'major': 'CS', 'gpa': '3.0'}
])


# Fetches all the rows
s = students.select()
result = conn.execute(s)

for row in result:
    print(row)

#with where clause
query = students.select().where(students.c.gpa == '3.5')
result = conn.execute(query)
for row in result:
    print(row)


#updating a record
query = students.update().where(students.c.name == 'Shyam').values(gpa = '6.1')
conn.execute(query)
print("After updating")
s = students.select()
result = conn.execute(s)
for row in result:
    print(row)


# delete a record

query = students.delete().where(students.c.name == 'Ram')
conn.execute(query)
print("After deleting")
s = students.select()
result = conn.execute(s)

for row in result:
    print(row)

