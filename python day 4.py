'''
Lis is a collection of different dattypes

List datatypes
---> List is a collection of different datatypes that are enclosed(represented)in []
seperated by commas(,)
---> list is muttable
ex:-
all_type=[1,'python',[1,2])

immutable ->the change we done will not stay(change)

so="python is a language"
prtint(so.replace('python','java'))
prtint(so.replace('python','c'))
prtint(so)

muttable -> the change we done will be stay(modify)

any_ = [1,2,3,4]
print(any_)
any_.append(5)
print(any_)
any_.append(10)
print(any_)
----------------
Differnce b/w muttable and immutable

muttable                                         immuttable
-----------                                  ---------------------
-> the datatype can be mofify                -->can't be modified
eg:- List                                       eg:- string                         
any_ = [1,2,3,4]                                    so="python is a language"
print(any_)                                         prtint(so.replace('python','java'))
any_.append(5)                                      prtint(so.replace('python','c'))
print(any_)                                         prtint(so)
any_.append(10)
print(any_)                                     
-------------------------------------------------------------------------------                                                 
                                                                                              
methods in list

1.append()
---> This is used to add a new item into list but it will add in the last index position
we can only add one item
ela iste ala add chestadhi(gives in on eindex value)
eg:-
any_ = [1,2,3,4]
print(any_)
any_.append(5)
print(any_)
any_.append(10)
print(any_)
any_.append('python')
print(any_)
----------------
2.extend()
--> This is also add aitem in the last index position,but it will give each value in the
    each index position
---> It will take only  list ,tuple and string  
each character ki seperate index posistion istadhi(gives seperate index to each character)
ex:-
any_ = [1,2,3,4]
any_.extend([23,90])
any_.extend('python')
print(any_)
print(len(any_))
------------------------------
indexing in list
any_ = [1,2,'python is a language',[45,78,"Java is a language",[1,23],90],'Hello']
print(any_[3][3][1])
-----------------------------------------------------
3.pop()
-->uses index value to delete
--> used to delete the item from the list,but it will delete based on index position
syntax:- variable_name.pop(index posistion)
eg:-
any_ = [1,2,45,78,23,90]
any_.pop(2)
print(any_)
-------------------------------------------
4.remove()
-->uses direct value to delete
-->used to delete the item from the list,but it will delete direct value from list
syntax:- variable_name.remove(value need to be delete)
eg:-
any_ = [1,2,45,78,23,90]
any_.remove(1)
print(any_)
-----------------------------------------
5.insert()
-->we can insert item  where we want  at the particular index
syntax:- variable_name.insert(index,element)
eg:-
any_ = [1,2,45,78,23,90]
any_.insert(3,12)
print(any_)
-----------
6.sort()
sorts permently
eg:-
any_=[78,45,34,1]
any_.sort()
print(any_)
any_.append(10)
print(any_)

7.sorted()
sorts only on runtime
eg:-
any_=[78,45,34,1]
print(sorted(any_))
-------------------------------

Tuple
---> tuple is a collection of different datatypes representd in () and seperated by comma(,)
it is immuttable
ex:-
how = (1,2,3,4,"python",[4,5],(90,78))
print(how)
methos
1. index()
how = (1,2,3,4,"python",[4,5],(90,78))
print(how.index('python'))
2.count()
how = (1,2,3,4,"python",[4,5],(90,78))
print(how.count('python'))

'''



'''
Task:- 1)write 2 examples for each method --> count,index,insert
2)[56,[1,2],['python','java',['python is a language',153,90],[78,6],'I know c']] just find know using indexing and 153 also seperatly
-----------------------
'''

