'''
OOP --> Object Oriented Programming -->objects (class,objects) 

why not POP -->Procedure Oriented Programing -->Functions

#Chair(object)-->Wood (Materials),Design(Demensions)(class),Person

A Class is a blueprint  of an object

An object is a real world entity Which contains --> Attributes (variables)
                                                --> Methods (Functions)
TO create a class we are having class keyword

Flipkart -->Products-->laptop,mobiles,gadgets.....

Features --> Encapsulation,Inheritance,Polymorphism
Encapsulataion -->Hides

recomended to keep class name as Capital

#function-->house
#class-->power House

syntax:
class ClassName:
     """docstring"""
     #attributes (define the data)
     ......
     ......
     def fname(self): #behaviour #self is like a reference not only self we can use anything
     def __init__(self): # this is recommended rather than functionname (fname)
         statemnet(s)...
         ..............
obj = ClassName()

#Students -->name,age
class Students:
    """Student details"""
    name = "Akash"
    age = 20
    place = "Vizag"

    def details(self):
        print(f'{self.name} is in {self.place} and his age is {self.age} years')
#Creation of objects
st1 = Students()
print(st1)
print(dir(st1))
print(st1.name,st1.age,st1.place)
#print(st1.details()) #TypeError as we dont use self 
print(st1.details()) #NameError as we have thrown self but no reference
#now we pass the reference
print(st1.details())
st2 = Students()
st2.details()

#In above case how many objects u create the result will be same

class Students:
    """Student details for multiple students"""
    def details(self,name,age,place):
        self.name = name
        self.age = age
        self.place = place
    #now to access those details
    def display(self):
        print(f'Student name is {self.name}')
        print(f'Student age is {self.age} and lives in {self.place}')
st1 = Students()
st1.details("Akash",20,"Vizag")
print(st1.name,st1.place)
st1.display()
print(st1.__class__)
print(st1.__doc__)
print(st1.__dict__)
st2 =Students()
st2.details("Sai",25,"Hyderabad")
print(st1.name,st1.place)
st2.display()
print(st2.__doc__)

#In this case we want object to be initialized -->__init__() it is called as constructor
#why we should use because it is a special function and  will automaticlly assigns data intead of calling for multiple times
class Students:
    """Student details for multiple students"""
    def __init__(self,name,age,place): #constructor
        self.name = name #instance variable
        self.age = age
        self.place = place
    #now to access those details
    def display(self): #instance methods
        print(f'Student name is {self.name}')
        print(f'Student age is {self.age} and lives in {self.place}')
st1 = Students("Dileep",25,"Hyd")
st1.display()
print(st1.__dict__)
st2 = Students("Srinu",24,"Vizag")
st2.display()
print(st2.__dict__)

#Create a Cars class with attributes as brand,name, price
#create multiple objects

class Cars:
    """Cars details for multiple brands"""
    def __init__(self,name,price,color,milage):
        self.name = name
        self.price = price
        self.color = color
        self.milage = milage
    def display(self):
        print(f'Car Brand is {self.name} its price is {self.price} with {self.color} colour and giving milage of {self.milage} KMPH')
car1 = Cars("Verna",250000,"WINE",50)
car1.display()

#Encapusualation -->How the methods are attributes are binde to single
#Class,in similar way how we can access the data -->Public,Protected,Private

#Public Attributes -->can be created and modified even outside the class

class Users:
    """usage of Public attributes"""
    def __init__(self,username):
        self.user = username #Public attribute
    def dispaly(self):
        print(f'Username is {self.user}')
u1 = Users("John")
print(u1.user)
u1.user = "Sam" #We can modify theb public attribute
print(u1.user)
u1.dispaly()

#Protected Attribute -->These can also be modified outside the class,its
#mainly useful as a hint/coding  Convention for other used/developers
#to create a protected attribute we use underscore -->_otp
    

class Users:
    """usage of Public attributes"""
    def __init__(self,username,_otp):
        self.user = username #Public attribute
        self._otp = _otp #Protected Attribute
    def dispaly(self):
        print(f'Username is {self.user}')
        print(f'OTP is {self._otp}')
u1 = Users("John",4352)
u1.dispaly()
u1._otp = 5435
u1.dispaly()
'''

#Private Attribute -->restrict the usage and cannot be directly  accessed
#we have the usage or notation asdouble leading unserscore -->__password

class Users:
    """usage of Public attributes"""
    def __init__(self,username,_otp,__password):
        self.user = username #Public attribute
        self._otp = _otp #Protected Attribute
        self.__password = __password #private attribute
    #usage of getter() or get() method for password
    def get_password(self):
        """Getter method for password"""
        #return "******"
        return self.__password
    #Usage of setter() to modify the data
    def set_password(self,new_password):
        if len(new_password) < 6:
            return 'Password length is not matching'
        else:
            self.__password = new_password
            return 'Update password'
u1 = Users("Admin",5432,"orange")
print(u1.get_password())
print(u1.set_password("admin")) # you are  not satisfying password reqmnts
print(u1.set_password("admin123"))# in this case satisfied
print(u1.get_password())
print(u1.__dict__)
