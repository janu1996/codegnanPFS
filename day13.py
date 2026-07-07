'''
passing by value
variable lekaunda values ni datatype tho pass chestam
 eg:-
 def some(a):
    print(a+9)
some(8) # here we can pass any datatype
eg2:-
def some (a):
    for j in a:
        print(j)
some([1,2,3])
------------
passing by reference
variable tho kakunda vidiga reference tho pass chesam
eg:-
a=(1,2,3)
def some (a):
    for j in a:
        print(j)
some(a)
-------------------
return keyword
--> in a function a return is executed then it will exit from the function
with certain return values
we can call it multiple times
eg:-
def myfunc_(b):
    return 5 +b
a = myfunc_(10)
print(a)
eg1:-
def myfunc_(b):
    return 5 +b
a = myfunc_(10)
c = myfunc_(100)
print(a)
print(c)
----------------------------
built in functions in python
total 148
eg:-
import builtins

builtin_functions = [
    name for name in dir (builtins)
    if callable(getattr(builtins,name))]
print(builtin_functions)
print(f"Total built-in functions are {len(builtin_functions)}")
-----------------------
Recursive function
---> Recursive function that calls itself repeatedly until a specified
condition is met..
syntax
def func_name(parameter):
    if condition: # it is called as base case
        return statement
    else:
        return statement
print(func_name(arguments))
eg:-
def func_name(num):
    if num == 1: 
        return 1
    else:
        return num * func_name(num-1)
num = 10
print(func_name(num))
eg2:-
def func_name(num):
    if num == 1: # if condion lo change cheste dani kind aunna return lo kuda change chestam
        return 1
    else:
        return num * func_name(num-1)
num = 1
print(func_name(num))
'''
def func_name(num):
    if num == 1: 
        return 1
    else:
        return num * func_name(num-1)
num = 10
print(func_name(num))
