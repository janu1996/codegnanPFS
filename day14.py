'''
# NOTE : reduce() is a module
lambda function
---> This is alaso called as annonymous function..
---> A lambda function can take n number of agruments
but having only one expession
we cant write big codes it supports only small codes
syntax:-
---> lambda arguments : expression
eg:-
some = lambda an : an + 5
print(some(10))
eg2:-
some = lambda an,so : an + so
print(some(10,8))
we can pass any arrgument but only one expression should be there
we can use multiple arthemetic operations in single expression
then it will actiavte bodmas rule
eg:-
some = lambda an,so,why : an + so * why
print(some(10,8,2))
----------------------------
filter()
----> The filter() function is a built-in function used to filter elements
-->from an itterables such as list,tuple and set based on condition
-->This filter function returns filter object so we can convert that  only into list,tuple and set
--> it works only for mathematical expressions

syntax:- filter(function,itterable)

eg1:- even number using filter
nums = [1,2,3,4,5]
rev = filter(lambda a: a%2 ==0,nums)
print(tuple(rev))

#this creates a object and we need to give the type we want 
nums = [1,2,3,4,5]
rev = filter(lambda a: a%2 ==0,nums)
print(rev)

eg2:- odd num using filter
nums = [1,2,3,4,5]
rev = filter(lambda a: a%2 !=0,nums)
print(tuple(rev))
-------------------------------------------
List Comprehension
--> from old to new list
--> This offers a shorter syntax when we want to create a new list from the old list

syntax:- -->variable_name = [expression loop condition]# condition is optional

eg:-
old_ = [1,2,3,4,5,6]
new_ = [j for j in old_]
print(new_)
eg1:- with condition
old_ = [1,2,3,4,5,6]
new_ = [j for j in old_ if j % 2 == 0]
print(new_)
---------------------------------------------
Dictionary Comprehension
 --> This offers a shoter syntax when we want to create a new dict from the old dict
if we want condition same as list comprehension but in dict we need to take only numericals to use condition in dict
syntax:- --> variable_name = [expression loop]

eg:-
old_dict = {1:2, 3:7, 5:6}
new_dict = {i:j for (i,j) in old_dict.items()}
print (new_dict)

eg1:- with condition
old_dict = {1:2, 3:7, 5:6}
new_dict = {i:j for (i,j) in old_dict.items() if j % 2 == 0}
print (new_dict)

'''
old_dict = {1:2, 3:7, 5:6}
new_dict = {i:j for (i,j) in old_dict.items() if j % 2 == 0}
print (new_dict)



