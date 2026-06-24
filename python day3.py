'''
DataTypes

Type of data is storing in variable

1.int --> used for numerics
 ex:- num=8

2.float
  --->decimal point,used for numerics 
 ex:-num_2 = 7.89

num_2 = 7.89
num = 6.89
print(num_2/num)
print(num // 2)--->gives round figure it is called as float division

3.string
sequence of characters [collection ani cheppakudadhu]
anything given in ' '," ",""" """
---> String is sequence of char that are enclosed in ' '," ", """ """. including space,dot ,splchar evrything.
---> Str is immutable
ex:
so = "python"
any_ = ",.@ 9"

4.Concatination
--> same the (+) symbols acts as addition only to interger rest of datatypes it combines 2 strings.
---> Here, the (+) operator acts as to concatinate more than 2 strings....
ex:-
so = "Python"
any_ = " is a language"
print(so + any_)

5.indexing
  to get a exact substring or character in a string  position it includes space and starts from 0
---> This is used to access the particular char in the string by passing indexposition value...
--->it has flexibility or reverse indexing which starts from [-1]
--->Index starts from 0....
--->We have negative indexing to count position from last to first
---> we need to keep the index value in [] between the sqaure braces
ex:
so = "Python is a language"
print(so[12])
print(so[-2])
---------------------------------------------
Methods
. petti ivvali
braces are very imp for methods and functions
1.replace()
---> remove old string into new
---> This method is used to change any substring in that particular string

syntax---> variable_name.replace("old string","new string",count)
count helps to replace particular number of times if not mentioned it replaces every substring
for exam in this string there are 3 a's if i give count as 2 it replaces 1st 2 a's if not it replaces every a in the string.
ex:-
so = "Python is a language"
print(so.replace("Python","Java"))
print(so)
ex for count in replace
so = "Python is a language"
print(so.replace("a","A",2))

2.join()
--->This method used to add a new substring after each character in the string 
syntax--->"string".join(variable_name)
ex:-
so = "Python is a language"
print("-".join(so))
print("$".join(so))

3.split()
---> This method can divide the string into differnt index into list, based on the string passed by us....
okaavela is tho split cheste is  eliminate from that string and indexing ayite divide after " " python is 0 ,is -> 1,a->2 like that
syntax--->variable_name.split("substring")
ex:-
so = "Python is a language"
print(so.split(" "))
print(so.split("is"))

4.count()
--->Used to count the substring in the particular string and also specify the index posistion
(mention cheste akkadi varaku count chestdhi  12 iste  12 is not considered if not mentioned anything count for whole string)
(indexing is optional)
syntax:- variable_name.count("substring",start index,end index)

ex:-
so = "Python is a language"
print(so.count("a",0,12))
----------------------------------------
built in functions in string
String built-in functions

1.len()
include space also
finds the length of string
---> This will find length of the string,which is number char present in that string
ex:-
so = "Python is a language"
print(len(so))

2.max()
---> we will get the max character in the string
ex:-
so = "Python is a language"
print(max(so))

3.min()
---> we will get the min character in the string
it also consider space  as min if space consists in string
ex:-
so = "Python is a language"
print(min(so))
kc = "radhakrishna"
print(min(kc))

--------------------------
 build 24 hr clock


time_ = "16:56"
parts_=time_.split(":")
print("this time",time_,"is convert into this",int(parts_[0]) - 12,":",parts_[1],"pm")
 
'''

time_ = "16:56"
parts_=time_.split(":")
print("this time",time_,"is convert into this",int(parts_[0]) - 12,":",parts_[1],"pm")

