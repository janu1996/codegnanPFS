'''
Modules
--> A Module is a python file is nothing but (.py) that contains resuable code
we can use these and write code
1. Variables
2.functions
3.classes
4.objects
5.statements
---------------------------
why we need this modules
--->Instead of writing the same code repeatedly,we can store it in a module
and use it whenever needed...

vere file lo code ichi ee file lo import chestam

-------------
Types of modules

1.user define

eg1:-
import first_module
print(first_module.add(45,7))
print(first_module.sub(45,7))
print(first_module.mul(2,10))
print(first_module.div(10,2))

import specific functions
by using that  func name
this is default  ga ivvali 

from first_module import add,sub
print(add(45,7))
print(sub(45,7))
print(mul(2,10))
print(div(10,2))

ala kakunda nni import cheyali ante we use *
eg:-
from first_module import *
print(add(45,7))
print(sub(45,7))
print(mul(2,10))
print(div(10,2))

to import module with alais name

eg:-
import first_module as m
print(m.sub(45,7))

2.built-in
- math
eg:-
import math
print(math.sqrt(25))
print(math.factorial(5))
print(math.pow(2,5))
print(math.pi)

imp notes
sqrt() ---> squaure  root
factorial() ---> factorial
pow() ---> power
ceil() ---> roundup
floor()--->rounddown
pi ---> pi value

-os
The os module is used to interact with operating system
getcwd() --> current directory
mkdir() --> create a  folder
rmdir() --> remove a folder
rename()--> rename the folder
eg:-
import os
print(os.getcwd()) # to get current directiory
os.mkdir("Tejafile") # to create a folder
os.mkdir("python")
os.rmdir("python") # to remove a folder
os.rename("python","KJ")

okasari create or delete chesina file name tho malli cheyakudadhu
it will raise error

-sys
--> This will provide  the information of the  python interpeter
import sys
print(sys.version)

-random
-->Used to generate random values (like otp)
eg:-
import random
print(random.randint(1000,9999))

specific one

colors = ['Yellow','Red','Blue','Green','pink']
print(random.choice(colors)) # to take from spicific one
 
'''

import random
print(random.randint(1000,9999))

colors = ['Yellow','Red','Blue','Green','pink']
print(random.choice(colors)) # to take from spicific one
 
