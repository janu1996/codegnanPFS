'''
DAY-2 TASk:
#task-->Store the results of name,weight,height --> BMI into a collection

results = []
number_of_users = int(input("Enter the number of users: "))
for i in range(number_of_users):
    while True:
        try:
            name = input("Enter your name: ")
            weight = float(input("Enter the weight in Kgs: "))
            height = float(input("Enter the height in meters: "))

            if weight > 0 and height > 0:
                break
            else:
                print("Enter only positive values")

        except ValueError:
            print("Enter only numeric values for weight and height")

    bmi = weight / (height ** 2)

    if bmi<18.5:
        print(f'{name} is into Under Weight category and BMI is {bmi}')
    elif  18.5<=bmi<=24.9:
        print(f'{name} is into Normal Weight category and BMI is {bmi}')
    elif 25<=bmi<=29.9:
        print(f'{name} is into Over Weight category and BMI is {bmi}')
    elif bmi>=30:
        print(f'{name} is into Obesity category and BMI is {bmi}')

    result = {
        "name": name,
        "weight": weight,
        "height": height,
        "BMI": bmi,
    }

    results.append(result)

print("\nBMI Results:")

for result in results:
    print(result)

DAY 3:
python project -->pop/oop-->DSA(Logic based -->pattern based -->platform
pop(procedure oriented programing) -->Dividing the entire code into
blocks -->procedures -->functions (def)
Functions -->A reusable block of code (A block of statements which performs
a specific task)

syntax:

def<funcname>(parameters):# func defn
    """Doc String"""
    statements(s)...
    ..........           #body of func 
    return value(s)...
fname(args) # func call

#simple scenario to understand

def add(a,b):
    """Addition function"""
    c = a+b
    return c
print(add(12,21))#addition
c,d ='codegnan','python'
print(add(c,d))#concatination
e,f = map(input("Enter the values:").split(','))
print(add(e,f))
print(add([1,3,4],[4,6,7]))#merging
#print(add(1,2,3,4)) # it comes error type error #positional arguments

#Variable length arguments -->*args We can pass any number of positional arguments
#arguments -->Where the data will be storeed in tuple...()
# manam emi ivvaka pote defalutb ga tuple tesukuntundi

def sample(*a):
    """Demo of Variable lenght arguments"""
    print(a)
    print(type(a)) #default it stores in tuple format
sample()
sample(2,3,4,5)
sample("codegnan",[23,4],'poll',2+5j)

marks =[20,15,25,18]
sample(marks)
sample(*marks)

#* is used to pass multiple values into one argument
a,*b,c = 12,'code','poll',23,4,9
print(a)
print(b)
print(c)
--------------
using membership operator:

def add(*a):
    """Perform addition for numeric values"""
    print(a)
    result = 0
    for  i in a:
        #print(i)
        if type(i) in [int,float]:            
            result = result + i
    return result
print(add(2,3,5))
print(add(2,'hi',3,4))
-----------
using comaprision operator

def add(*a):
    """Perform addition for numeric values"""
    print(a)
    result = 0
    for  i in a:
        #print(i)
        if type(i)== int or type(i)== float:            
            result = result + i
    return result
print(add(2,3,5))
print(add(2,'hi',3,4))

------------------



#keyword arguments -->we can pass the name for the arguments

def batch(age,place,name='Codegnan'):
#def batch(age,place='Vizag',name='Codegnan'):
#def batch(age=1,place,name='Codegnan'): #error -->non default always follows default argument
    """ Keyword arguments usage"""
    print(f'{name} is in {place} and age is {age} years')
batch('Codegnan',1,'Vizag')
batch(place='vizag',name='codeganan',age=1)

#keyword arguments only needs name matching not order
batch(name="Saketh",age=32)
#default arguments can accept a value as defalut

print(4,5)
print(4,5,sep=':')#here keyword  argument is sep and we are changing
#the default value for sep


#keyword variable length arguments (**kwargs) --->we can pass any number of
#keyword argument,data is stored in dictionary

def batch(**a):
    """Keyword variable length arguments usage"""
    print(a)
    print(type(a))
batch()
batch(name='akash',age=21,place="Vizag",branch="CSE")

data={'name':['Akash','praneeth'],
      'place':['Vizag','Rajahmundry']}
batch(**data)
data.update({'batch':'PFS-VSP-007'})
batch(**data)

#Task - create a function with the usage of  *args & **args

def fn(*a,**b):
     .......
     ....... # any scenior based i do vote
fn(*c,**d)

'''
