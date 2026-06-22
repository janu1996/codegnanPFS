Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
'''
procedural language
--------------------------
--> This follows a step-by-step approach, where code is structure into procedures such as function or routines......
    eg:- C 
------------------------
object oriented language (oop)

--> This is based on concept of object and class...
eg:- python, Java

 examples:
print(89+67)
num = 89
num_2 =69
total_=num+num_2
print(id(num))
print(id(num_2))
print(id(total_))
--------------------------------
python

1.dynamically typed
 ---> Python knows the type of data we are passing  to the variable...
eg: num=12 
    it prints as <class 'int'>
2.interpreter
---> Python execute line-by-line , if any error occurs it will stop execution at that line and before lines will gives the output..
eg:-
num = 89
print(type(num)
num_2 =69
total_=num+num_2
print(id(num))
print(id(num_2))
print(id(total_))

3. High_level
   int num=89
----------------------------------------------
--->Invented in 1991,by Guide Van Russum
 -----------------------
Why use python

1.easy syntax
2.cross-platform
3.wide application
4.huge library support
-------------------------
Applications

web development
gamming
dl
ml
--------------------------
Tokens

keywords
   ---> there are reserved words in python
   eg:- if, for, while, else, is, or

2. Identifiers 
   ---> Names given to variables, function, class
    eg:-
       so= hi
       print(so)
3.Literals
  --->  right side  of variable is literal
...     eg:- 89,"hello",4.56
... 4.operators
...   --->  + ,- ,* , /
... 5.punctuators
...  ---> () , {}, []
... ------------------------------------
... Rules of variables
... 
...  1.can start with  A-Z,a-z,_
...  eg: correct ways
...   num_1=/
...   num=8
...   Num_2=9
... 
... 2.should not have spaces, special character and should not start with number
... eg: wrong ways
... $num =0
... su@m=8
... $ o =89
... 2num=9
... ----------------------------------
... Comments
...   the lines will not execute 
... 1.single line comment               
...   we use #                                        
... 2. multi line comment              
... we use '''   ''' ,"""   """
... 
... ex:  
... num=9
... if num % 2==0: # checking weather the number is even or odd
... print("Even")
... else:
... print("Odd)
... ----------------------------------------
... Boolean
...  
... 1.True
... 2.False
... 
... 
... num = 8
... num_2 =89
... print(num == num_2) 
... 
... 
