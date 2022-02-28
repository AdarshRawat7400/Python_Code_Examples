import pymongo

#Create a MongoClient to the running mongod instance
client = pymongo.MongoClient("mongodb://127.0.0.1:27017/")


#Create a database called "students"
db = client["mydatabase"]
students_collection = db["students"]

##########################################################################################


## Insert Operations

#Insert a document into the "students" collection
students_collection.insert_one(
    {
        "firstname": "Ram",
        "lastname": "Kumar",
        "age": 23,
        "city": "Indore",
        "state": "MP"
    })


#Insert multiple documents into the "students" collection
students_collection.insert_many(
    [
        {
            "firstname": "Shyam",
            "lastname": "Kumar",
            "age": 25,
            "city": "Gwalior",
            "state": "MP"
        },
        {
            "firstname": "Ravi",
            "lastname": "Kumar",
            "age": 27,
            "city": "Bhopal",
            "state": "MP"
        }
        ,
        {
            "firstname": "Suresh",
            "lastname": "Kumar",
            "age": 29,
            "city": "Gwalior",
            "state": "MP"
        },
        {
            "firstname": "Ramesh",
            "lastname": "Kumar",
            "age": 31,
            "city": "Indore",
            "state": "MP"
        }
        ,
        {
            "firstname": "Rajesh",
            "lastname": "Kumar",
            "age": 21,
            "city": "Indore",
            "state": "MP"
        },
        {
            "firstname": "Harsh",  
            "lastname": "Kumar",
            "age": 17,
            "city": "Indore",
            "state": "MP"
        }
        ,
        {
            "firstname": "Rajesh",
            "lastname": "Kumar",
            "age": 18,
            "city": "Indore",
            "state": "MP"
        }


        

    ]
)

##########################################################################################

# View Operations
#Find all documents in the "students" collection (Retrive all documents)
print("All Documents:")
for student in students_collection.find():
    print(student)

# Find limited number of documents in the "students" collection (Retrive limited number of documents) using limit function
print("\nLimited Documents:")
for student in students_collection.find().limit(3):
    print(student)


##########################################################################################


# Update Operations

# Update one  document in the "students" collection
print("\nUpdate one document:")
students_collection.update_one(
    {"firstname": "Ram"},
    {"$set": {"city": "Chhatarpur", "age": 27}}
)

# Update multiple documents in the "students" collection
print("\nUpdate multiple documents:")
students_collection.update_many(
    {"city": "Indore"},
    {"$set": {"city": "Banglore", "state": "Karnaataka"}}
)


# Find all documents in the "students" collection 


# List of the db names
for db in client.list_database_names():
    print(db)

##########################################################################################

# Delete Operations
print("Single Document Deleted:")
# Delete single document in the "students" collection
students_collection.delete_one({"firstname": "Ram"})


print("Multiple Documents Deleted:")
# Delete multiple documents in the "students" collection
students_collection.delete_many({"city": "Banglore"})

##########################################################################################


# Filter Operations
print("Filtered Documents: based on city")
# students which belong to indore
for student in students_collection.find({"city": "Gwalior"}):
    print(student)



# Sorting Operations
print("Sorted Documents:")
# Sort the documents in the "students" collection based on age
for student in students_collection.find().sort("age"):
    print(student)



##########################################################################################


# Delete student collection
students_collection.drop()


