'''
Generators
--> This grnerator  is a special function that returns the itertor. 
instead of returning  all the values at once...
--> Here we are going to use the yield keyword
it will  ot give conti us values in output we need to call using next we need to print every time
but in normal function if we call or return  it gives  all values at a time
--> It is also known as lazy evualotion
because it is passed if we call then only it continous

eg:-

def some():
    yield 1
    yield 2
    yield 3
so = some()
print(next(so))
print(next(so))
print(next(so))

working og generator
--------------------
-->When a function is called
-->It does not execute the function immediately...
-->It will rn the function returns the generator object
-->The the function will pauses at each yield...
-->When the next() is called  again, execution resumes from where it stoped
eg:-
def demo():
    print("Start")
    yield 1

    print('Middle')
    yield 2

    print('End')
    yield 3
how = demo()
print(next(how))
print(next(how))

eg1:- With Generator

def how(so):
    for i in range(so):
        yield i*i
any_ = how(5)
print(next(any_))
print(next(any_))
print(next(any_))
print(next(any_))
print(next(any_))

eg2:- Without generator

def Sqt(n):
    for j in range(n):
        print(j*j)
Sqt(5)
-------------------------------------------
Difference b/w function and generator

function
-------------
--> return
-->return complete result
--> Function will end after the return the values
--> More memory usage
-->This function never resume

generator
--------------
--> yield
--> Return only value at once
--> pauses after every yield
-->less memory usage
-->REsumes after next()

------------------------------------
yield keyword
--> This will produces the value
--> But the yield pauses the function
--> And yield will save the functions current state
--> yield will continues where it stoped...
-->It will know the current  state of the function
-----------------------------------
next() keyword
--> The next() function is used to retrieve the next value from a generator
ex:-
for yield and next same example which is given above in the satarting
----------------------------------
StopIteration
--> Calling next function after all values retrive then it will raise 
StopIteration (error) exception

ex:-
def how(so):
    for i in range(so):
        yield i*i
any_ = how(5)
print(next(any_))
print(next(any_))
print(next(any_))
print(next(any_))
print(next(any_))
print(next(any_))

--------------------------
Generator  expression
--> The generator expression is similar to a list comprehension but uses
parenthesis () instead of []
 it will give same as yelid function  without yield
eg:-
gen = (x*x for x in range(5))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

'''
def how(so):
    for i in range(so):
        yield i*i
any_ = how(5)
print(next(any_))
print(next(any_))
print(next(any_))
print(next(any_))
print(next(any_))
print(next(any_))
