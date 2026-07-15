'''
OOPS
-Object -oriented Programming system (OOPs), This will be organizes the
code using classes and objects...

Use
----
-Code reusable
-Easy maintance
-Clear understanding
-Better Security

Classes
--------
Class is a blueprint or a template used to create an object....

class Batch_4:
    pass

Object
-------
Object is a instance of the class


eg:-
class student:
    studn = 'Teja'
st_ = student() #it is a class attribute
print(st_)

eg1:-
class student:
    studn = 'Teja'
st_ = student() #it is a class attribute
print(st_.studn)# this will give output

------------------
Attributes
-Attributes are the variable that belongs to an object or the class

eg:-
class how:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def nam(self):
        print(self.name)
s1 = how('Teja',67)
print(s1.nam())

eg1:-
class how:
    def details(self,name,age):
        self.name = name
        self.age = age
  
        
s1 = how()
s1.details('Teja',67)
print(s1.name)
------------------

Methods
-------
-Methods are nothing but the functions inside the class

eg:-
class calculator:
    def add(self,num,num_2): # this is method
        print(num + num_2)
cal = calculator()
print(cal.add(45,6))

eg1:- in output none will not come
class calculator:
    def add(self,num,num_2): # this is method
        print(num + num_2)
cal = calculator()
cal.add(45,6)

eg2:-

class calculator:
    def add(self,num,num_2): # this is method
        print(num + num_2)
        
    def sub(self,num,num_2):
        print(num - num_2)
cal = calculator()
cal.sub(78,9)

#__init__ is a constructor
'''


class calculator:
    def add(self,num,num_2): # this is method
        print(num + num_2)
        
    def sub(self,num,num_2):
        print(num - num_2)
cal = calculator()
cal.sub(78,9)
