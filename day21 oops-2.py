'''
self keyword
-------------
-self refers to current object...

eg:-
class Test:
    def display(self):
        print(self)
te = Test()
print(te)
te.display()

-----------
constructor
--> This constructor initializes the object automatically when it is created...
double underscore init double underscore(__init__)
eg:-
class Batch:
    def __init__(self,name,branch):
        self.name = name
        self.branch = branch
    def display(self):
        print(self.name)
        print(self.branch)
B4 = Batch('Teja','ECE')
B4.display()
----------------

Access Specifiers

1.public varaible:
can access by anyone
emi lekaunda unte adhi public
eg:-outside the class
class Batch:
    def __init__(self,name,branch):
        self._name = name
        self.branch = branch
    def display(self):
        print(self._name)#protected
        print(self.branch)#public  #if double underscore is there it is private
B4 = Batch('Teja','ECE')
B4.display()

eg1:- inside the class
class fam:
    def __init__(self):
        self._name = "Teja"
f = fam()
print(f._name)

2.Private variable:-
need to protect the class using single underscore and then use double underscore to call private variable
eg:- outside the class
class bank:
    def __init__(self):
        self.__pin = '6600' #private
AC = bank()
print(AC._bank__pin) #accessing private

eg1:- inside the class
class Bank:
    def __init__(self):
        self.__pin = '7700'
    def display(self):
        print(self.__pin)
ac = Bank()
ac.display()

3.protected:-
proctect cheyadaniki _ (underscore) use chestam
to  use protected vairable use _ (underscore)

eg:-
class Batch:
    def __init__(self,name,branch):
        self._name = name
        self.branch = branch
    def display(self):
        print(self._name)
        print(self.branch)
B4 = Batch('Teja','ECE')
B4.display()

----------
Encapsulation

binds the data and methods
--> Means wrapping the data and methods into a single unit(class
while controlling the access to the data

oka bag lo 2 diifernt items pettadam one is data and another is methods
eg:-

class atm:
    def __init__(self,balance):
        self._balance = balance
    def deposit(self,amount):
        self._balance += amount
        print(self._balance)
tran = atm(balance = int(input("Enter Amount: ")))
tran.deposit(amount = int(input("Enter Amount: ")))

'''
class Bank:
    def __init__(self):
        self.__pin = '7700'
    def display(self):
        print(self.__pin)
ac = Bank()
ac.display()

