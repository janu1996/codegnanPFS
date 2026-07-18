'''
Ploymorphism
-------------
--> Polymorphism means many form
--> it allows same method,function or operator to perform different
tasks depending on the same object...

types
-----
1.Method Overloading
----------
--> Method overloading means having multiple methods with the same naem
but different parameters
(Same classes lo 2 methods unte recent ga unnadi kakund amundhu dhi load chestadhi)

eg:-
class cal:
    def add(self,num,num_2=0):
        print(num + num_2)
obj = cal()
obj.add(4,7)

eg2:-
class cal:
    def add(self,num,num_2=0):
        print(num + num_2)
obj = cal()
obj.add(9)

eg3:-
class cal:
    def add(self,num,num_2=0):
        print(num + num_2)
    def add(self,num,num_2=0,num_3=0):
        print(num+num_2+num_3)
obj = cal()
obj.add(9,4,7)

eg4:-
class cal:
    def add(self,num,num_2=0):
        print(num + num_2)
    def add(self,a,b):
        print(a + b)
obj = cal()
obj.add(45,67)
obj.add(4,7)
------------------------
2.Method Overriding
(different classes lo unte recent and child class ni output lo istadhi)
--> the method  overriding occurs when a child class provide its own 
implementation of a method already defines in its parent class....

eg:-
class animal:
    def sound(self):
        print("Animals make sounds")
class dog(animal):
    def sound(self):
        print("Dogs barks")
d = dog()
d.sound()

3.Operator Overloading
-->This allows operators (+,-,*) to work differntly for user-defined objects

1.__add__ (+)
2.__sub__(-)
3.__mul__(*)
4.__truediv__(/)
5.__eq__()(==)
6.__It__() (<)

eg:- sub
class student:
    def __init__(self,marks):
        self.marks = marks
    def __add__(self,other):
        return self.marks - other.marks
s1 = student(56)
s2 = student(67)
print(s1 - s2)

eg:- add
class student:
    def __init__(self,marks):
        self.marks = marks
    def __add__(self,other):
        return self.marks + other.marks
s1 = student(56)
s2 = student(67)
print(s1 + s2)

eg:- mul
class student:
    def __init__(self,marks):
        self.marks = marks
    def __mul__(self,other):
        return self.marks * other.marks
s1 = student(56)
s2 = student(67)
print(s1 * s2)

-----------------------------------------------------
Data Abstration

-->Data Abstraction is the process of hiding implementation details and
showing only the essential data to the user (its for security)

ex:-
-ATM
-Car
-Apps

how to use
-----------
from abc import ABC, abstractmethod
class parent:
    
    @abstractmethod
    def dispaly(self):
        pass
        
'''

from abc import ABC, abstractmethod
class bank:
    
    @abstractmethod
    def intrest(self):
        raise NotImplementedError('Subclass must implement intrest()')

class SBI(bank):
    def intrest(self):
        print('SBI interest Rate: 6.5%')
class HDFS(bank):
    def intrest(self):
        print('HDFS intrest Rate: 5.5%')
class ICIC(bank):
    def intrest(self):
        print('ICIC intrest Rate: 6.9%')
        
banks = [SBI(),HDFS(),ICIC()]

for j in banks:
    j.intrest()
