'''
statements
-->3 types
conditional ----> if,if-else,elief,nested if(in inside if)
control---> break,continue,pass
loop---> for,while
 first oka if condition raste ventane daniki else raseyali so that it will be easy and not miss any else
 isted of that use pass like
 if num % 2 == 0:
 pass (here we will write code or other if)
 else:
 print("odd number")
1.conditional statements
if
--> used to check a condition true or not
eg:-
num=10
if num % 2 ==0:
    print(f"{num} is a even number")
eg2:-
num=9
if num % 2 ==0:
    print(f"{num} is a even number")
it will not show any output besacuse the condition  is failed the it goes to else statement
and insead of space use tab it gives correct indentation

if-else
--> else is a fall back statement  in case the if condition is false then this else will be executed
eg:-
num=9
if num % 2 ==0:
    print(f"{num} is a even number")
else:
    print (f"{num} is a odd number")

example of if-else:

teja_ICIC_details = {"ATM PIN":'6600'}
pin_ = input("Enter your 4 digit ATM PIN:")
if pin_ in teja_ICIC_details['ATM PIN']:#if 1234  in 6600 :false
    print("Welcome to ICIC ATM")
else:
    print("You have entered incorrect pin")

nested if
-->if inside if
--->if inside the another if is called nested if
eg:-
teja_ICIC_details = {"ATM PIN":'6600'}
pin_ = input("Enter your 4 digit ATM PIN:")
if len(pin_) ==4:
    
    if pin_ in teja_ICIC_details['ATM PIN']:
        print("Welcome to ICIC ATM")
    else:
        print("You have entered incorrect pin")
else:
    print("pls entered only 4 digit pin")


elif
---> allows to check condition multiple times(for multiple if conditions only one else)
eg:-
marks_ = int(input("Enter your marks: "))
if marks_ is >= 90:
    print("A+")
elif marks_ >= 80:
    print("A")
elif marks_ > 70:
    print("B+")
else:
    print("Failed")
----------------------------------------------------------------------
2. loop statements
 1.for
 --> A for loop is used to itterate over a sequence,list,tuple,dictionaries
 (itterate means getting inside values one by one)
 -->to iterate over a sequence of strings,lists,tuple,dictionaries
 the variable used after for is called instance variable.(it it only defined at that runtime)
eg:-
any_ = "python is a language"
for j in any_:
    print(j)
eg2:-    
any_ = [1,2,3,4,5]
for j in any_:
    print(j)
    
eg3:-
any_ = (1,2,3,4,5)
for j in any_:
    print(j)
 eg4:- for dictionaries
 
any_ = {"Name" : "Teja",
        "Role": "Mentor"}
for key in any_.keys():
    print(key)
    
any_ = {"Name" : "Teja",
        "Role": "Mentor"}
for key in any_.values():
    print(key)

-----------------------
else in for loop
--> the else block will be executed after the for loop ,but incase the loop
is breaked then it will never enterd in the else block 
eg1:-
any_ = [1,2,3,4,5]
for val in any_:
    print(val)
else:
    print("Program ended")
eg2:-
any_ = [1,2,3,4,5]
for j in any_:
    print(j)
    if j == 3:
        break
else:
    print("Entered")
eg3:- takes from 0
 all_ = [1,2,3,4,5]
for j in range(20):
    print(j)
-------------------------------------
range in for loop:
---> it will not give last number
--> range is a inbuilt function that is used to generate a sequence upto a limit

syntax:- range(start ,end,step)#step is optional
eg:-
all_ = [1,2,3,4,5]
for j in range(1,50):
    print(j)
eg2:- used step
all_ = [1,2,3,4,5]
for j in range(1,50,2):
    print(j)
---------------------------------
 2.while
 ---> the while loop will execute until the condition becomes true........ 
---> it is a combination of if and for
---> it will run continuesly until the condition is true # until it meets the condition
eg:- here it runs continously until the condition is true 
i = 1
while i < 5:
    print(i)
    
eg2:-
i = 1
while i < 5:
    print(i)
    i += 1

------------------------------
3.control statements
1. break
--> the break statement is used to exit from the loop
eg:-
any_ = [1,2,3,4,5]
for j in any_:
    print(j)
    if j == 3:
        break
else:
    print("Entered")
2. continue
--> the continue will skip the current itteration
eg:-
any_ = [1,2,3,4,5]
for j in any_:
    if j == 2: 
        continue
    print(j)
else:
    print("Entered")
    

3.pass
--> it is a space holder( it will throw error when statement is incomplete)
--> instead of not getting error we will use pass
eg:-
any_ = [1,2,3,4,5]
for j in any_:
    pass
----------------------------------
assert keyword
---> it is used to check the condition but it will raise an error incase it is false....

eg:-
num = 10
assert num > 0
print(f"{num} is a positive")
eg2:- we can throw an error
num = 10
assert num < 0 ," has be a positive"
eg3:-
num = int(input("Enter a number:"))
assert num > 0 ," has be a positive"
voter ex:-
age = int(input("Enter your age:"))
assert age >= 18 ," you must have 18 years"
 

'''
