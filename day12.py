'''
Functions
--> Function is a block of code that can be reusable
--> Function can avoid  the repeated line of code.......
fuctions are of two types
1.built in
eg:- print(),max(),type(),min(),sum()
2. user define
--> this function starts with a keyword (def)
 syntax: def func_name(parameters):#defenation function
             -------------
             -------------
             -----
         fun_name(arguments)#caling function with same name
             use tab sapce if not it throws ana error
ex:-
def add():
    print("Helli!")
add()
--------------------    
types of arguments

we have 4 types
1. Requered arguments
-->  we have to pass same number of arguments with defination of the function
we are using or not it is no matter but it should  have all the exact values
eg:- need to use like this
def add(a,b):
    print(a+b)
add(2,6)
eg:- not to use like this
def add(a,b):
    print(a)
add(2)

2. Default
--> When we access global variables it will takes like this
eg:-
def add(a,b):
    print(a)
add(b=9,a=6)
eg2:-
num = 7
num_2 = 9
num_3 = 8
def add(a,b,c):
    print(a)
    print(b)
    print(c)
add(num,num_2,num_3)
3. Keyword
--> We can pass as a pair like (variable = datatype)
eg:-
def add(a,b):
    print(a+b)
add(a=2,b=6)

eg2:-
a=4
b=9
def add(a,b):
    print(a+b)
add(a,b)
4. Variable length
-->we can assign n number of values to single by using star (*) it will come in tuple this is for args
and access them using indexing 
---> can pass n number  aruguments and just use args in the oaramenters, we will
receive tuple of arguments
---> we can use (**)asterisk is called  and receive it as a dictionary
eg1:- example for args
num = 7
num_2 = 9
num_3 = 8
num_4 = 10
def add(*a):
    print(a)
add(num,num_2,num_3,num_4)
eg2:- accesing
num = 7
num_2 = 9
num_3 = 8
num_4 = 10
def add(*a):
    print(a[2])
add(num,num_2,num_3,num_4)
eg:3
num_2 = 9
num_3 = 8
num_4 = "Python"
def add(*a):
    print(a[3])
    print(a)
add(num,num_2,num_3,num_4)
eg4:- example for dictionary
def all_(**Any):
    print(Any['Age'])
all_ (Name = "Teja" ,Age = 14)
-----------------------------------------
Scope of variables
1.Global variable: we can use outside the function
this gloabal variable can be used throughout the program
eg:-
num = 9
def func_():
    print(num)
func_()
---> to change the value of global variable we  need to use keyword called global
it changes permentatly
---> to change the global variable by using keyword (global)that can be changed
completly inside and outside of the function
ex:-
num = 9
def func_():
    global num
    num = 89
    print(num)
func_()
if we gives like this it will get 2 values
num = 9
def func_():
    
    num = 89
    print(num)
func_()
print(num)

2.local variable: we cannot use outside the function
inside is local variable i cannot access the outside the  function
eg:-
def func_():
    num = 9
    print(num)
func_()
print(num)

'''
num = 9
def func_():
    
    num = 89
    print(num)
func_()
print(num)
