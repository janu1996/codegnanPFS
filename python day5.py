'''
Dictionary

---> Dict is a key: value pair seperated by collen(:),keys are unique we should not keep dupilicate values
it will not show error but it will not consider
---> in the place of keys we have to use immutable datatype...
left of collen is key and right is value in key we can take only immutable
--->Dict is mutable, we need to keep only in {},curly braces
eg:-
details_={"name":"Teja",
          1:"number",
          (6,7):[1,2]
          (8,9):"tuple"}
print(details_)

ex:-
IcIC_teja_details_={"name":"Teja",
                    "mob":123456789,
                    "Adhar":"1234567890",
                    "Ac num":98765432,
                    "ATM Pin":"7789"}
print("welcome to ATM")
user_pin = input("Enter your 4 digit pin: ")
if user_pin in IcIC_teja_details_['ATM Pin']:
    print("\n1.Deposite \n2.Withdraw")
else:
    print("Your pin is Invalid")
        
----------------------------------------------
methods
1.keys()
used to get all the keys from the dict
syntax--> variable_name.keys()
eg:-
details_={"Name":"Teja",
          "Age":56,
          "Gender":"Male"}
print(details_.keys())

2.values()
used to get all the values from the dict
syntax--> variable_name.values()
eg:-
details_={"Name":"Teja",
          "Age":56,
          "Gender":"Male"}
print(details_.values())

3.items()
used to get both keys and value in a pair
syntax-->variable_name.items()
eg:-
details_={"Name":"Teja",
          "Age":56,
          "Gender":"Male"}
print(details_.items())

4.clear()
it cannot clear one or 2 it deletes everything entier dictionary
-->If we use  the clear method the entire  dictionary will be deleted
syntax:-variable_name.clear()
ex:-
details_={"Name":"Teja",
          "Age":56,
          "Gender":"Male"}
details_.clear()
print(details_)

5.update()
 we can update any value inside the key, if the key is not present it will update it also
 syntax:-variable_name.update()
eg:-
details_={"Name":"Teja",
          "Age":56,
          "Gender":"Male"}
details_.update({"Name":"Garikapati"})
details_.update({"Age":19})
details_.update({"mobile":123456789})
print(details_)

------------------------------------------
any_=[22,45,6,7]
print(any_[0])
details_={"Name":"Teja",
          "Age":56,
          "Gender":"Male"}
print(details_['Name'])# we will be accessing the value  using the key name instead of seperate index value
-------------------------------
indexing can be used like this

details_={"Name":"Teja",
          "Age":56,
          "Gender":"Male",
          "Mobile":9876543}
print(details_['Name'])
print(details_['Mobile'])

------------------------------------------------------------------------------------------
Set
---> set is a collection of unorderd elements that are seperated by comma(,)
---> set is muttable
--->can remove dupilicate value by itself...
--> we use set as  unorderd so we say as elements
 eg:-
go = {1,2,3,4,2}
print(go) 
--------------
methods

1.union()(|)
---> we used to combine the elements from both sests
syntax:- set_1.union(set_2)
eg:-
go = {1,2,3,4}
so = {4,5,6,7}
print(go | so)# uses symbol
print(go.union(so))

2.intersection() (&)
--->shows the common value from  both the sets
--->common element from both sets
syntax:- set_1.intersection(set_2)
ex:-
go = {1,2,3,4}
so = {4,5,6,7}
print(go & so) # uses symbol
print(go.intersection(so))

3.Symmetric difference() (^)
---> all differnt elements from both sets
syntax:- set_1.symmetric_difference(set_2)
ex:-
go = {1,2,3,4}
so = {4,5,6,7}
print(go ^ so) # symbol
print(go.symmetric_difference(so))

 built in

4.add()
used to add new element into set
eg:-
go = {1,2,3,4}
go.add(5)
print(go)

5.remove()
it is used to remove element from set
-->To delete the elements from sets
---> if the given element is not in the list it will throw error
if the element is present it will remove 
eg:-
go = {1,2,3,4}
go.remove(2)
print(go)

6.discard()
 it will also remove element
 ---> if element is not present it will give the set as it is
 ---> if the element is present it will remove
 eg:-
go = {10,1,2,3,4}
go.discard(9)
go.discard(2)
print(go)
 

7.pop()
if we do not give any element it will remove last element
eg:-
go = {10,1,2,3,4}
go.pop()
print(go)




'''

go = {10,1,2,3,4}
go.discard(9)
print(go)
