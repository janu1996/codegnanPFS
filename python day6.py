'''
Type conversions
-----------------
we use converstion based on the requirement of the program
This is a process of converting one data type  to another...

Int--> string,float
eg:-
num=89
num_2=float(num)
print(num_2)
print(type(num))
so = str(num)
print(type(so))
----
Float--> string,integer
eg:-
num=8.9
how = str(num)
print(how)
print(type(how))
#for j in how:
   # print(j)
num_2 =int(num)
print(num_2)
----
string-->Integer,float,list,tuple
str to integer -->only possible if the string fully consists of numbers or digits
hai = "78"
num = int(hai)
print(num+10)
print(type(num))

str to float-->should consists only float values
hello = "67.89"
num_2 = float(hello)

print(num_2 + num)
 
eg1:-
hai = "78"
num = int(hai)
print(num+10)
print(type(num))
hello = "67.89"
num_2 = float(hello)
print(num_2 + num)
eg2:-
any_="34567"
con_=list(any_)
print(con_)
con2_ = tuple(any_)
print(con2_)
--------
list--> string,tuple,dictionary
list to str
var_ = ['p','y','t','h','o','n']
text_ = "".join(var_)
print(text_)

list to tuple
var_ = ['p','y','t','h','o','n']
some = tuple(var_)
print(some)

var_ = [10,20,30]
some = tuple(var_)
print(some)
list to dict
we need to have idea of every dict output
pyth_ = [('a',1),('b',2)]
conver = dict(pyth_)
print(conver)

tuple-->string;lists
tuple to list
fam = (1,2,3,4)
print(list(fam))
tuple to str
the values should be in strings
fam = ('h','e','l','l','o')
text2_ = "".join(fam)
print(text2_)
----
Built-in functions
we use some built in function to convert
str()
float()
int()
list()
tuple()
dict()
'''
