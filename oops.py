# >> Constructor
# is automaically called when an "OBJECT is created"
# def __init__(self)

# >> Destructor
# is automaically called when an "OBJECT is OUTLIves"
# def __del__(self)
# optional in python classes - since we have GC

## class and object example 1
class Person:
   def set(self,a,b,c):
       self.name = a
       self.dob  = b
       self.loc  = c
   def show(self):
       print(self.name,self.dob,self.loc)
   def convert(self):
       self.name = self.name.upper()


# main program
ravi = Person()   
guru = Person()   

ravi.set("ravi","12/12/2000", "indore")
guru.set("guru","10/11/2001", "chhatarpur")

ravi.convert()

ravi.show()
guru.show()


## class and object example 2
class Student:
  def __init__(self,name,grade,marks):
     self.name = name
     self.grade = grade
     self.marks = marks
     self.total = 0
  def find_total(self):
     self.total = sum(self.marks)
  def show(self):
     print("%s %s %s %s" %(self.name,self.grade,self.marks,self.total))

st1 = Student("ravi","8th",[10,20,30,40])
st2 = Student("manu","10th",[50,60,70,80])

st1.find_total()
st2.find_total()

st1.show()
st2.show()




# Data Hiding using private and protected data members:- 
# =============
# >> self.__datamember  - private datamember
#    self._datamember   - (protected) or
#                         semi private data memebr
#                         used in certain tricks
#    self.datamember    - public datamember

# >>Every class will have two acess specifiers 
#   private - will be acessible only within the CLASS 
#           - if the data member name starts with double underscore
#           - self.__datamember

#   public  - will be acessible in/outside the CLASS
#           - self.datamember


# example private data members in classs:-
# ----------
class Person:
  def __init__(self,name,loc):
     self.__name = name
     self.loc = loc
  
  def show(self):
     print(self.__name,self.loc)


p1 = Person("manju", "blr")
p1.show()

print(p1.loc)    # since its public - we get blr
print(p1.__name) # since its private - ERROR 



# example protected data members in classs:-
# we use underscore ‘_’ symbol to determine 
# the access control of a data member in a class.
class Person:
  def __init__(self,name,loc):
     self._name = name
     self.loc = loc
  
  def show(self):
     print(self._name,self.loc)


p1 = Person("manju", "blr")
p1.show() # this line will run because self._name is protected
        # and is accessable in the class
   

# abstract method example
from abc import ABC, abstractmethod
class Vehicle(ABC):
   @abstractmethod
   def wheels(self,no_of_wheels):
      pass

   @abstractmethod
   def max_speed(self,speed):
      pass

   @abstractmethod
   def milega(self):
      pass
 
#car = Vehicle() # this will throw error
                # Can't instantiate abstract class Vehicle with abstract methods max_speed, milega, wheels
                # this is because we can't instantiate abstract class

class Car(Vehicle):
   def wheels(self):
       return "This has 4 wheels"
   def max_speed(self):
       return "This has max speed 300 kmph"
   def milega(self):
       return "This has 30 kmpl milege"


# Now we can override the abstract class methods in subclass i.e., Car class

car = Car()
print(car.wheels())
print(car.max_speed())
print(car.milega())

class Truck(Vehicle):
   def wheels(self):
       return "This has 24 wheels"
   def max_speed(self):
       return "This has max speed 150 kmph"
   def milega(self):
       return "This has 15 kmpl milege"

truck = Truck()
print(truck.wheels())
print(truck.max_speed())
print(truck.milega())


