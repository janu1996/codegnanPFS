'''
1.palindrome
reverse also same word or meaning eg:- madam
#prirnt(so[:: -1]) it is a inbuilt function dont use it

so = input("Enter a word:")
empty_ = ""
for j in so:
    empty_ = j + empty_
if empty_ == so:
    print(f"{so} is a palindrom")
else:
    print(f"{so} is  not a palindrom")

2.phibanoic series
last 2 digits add upto a limit
swap cheste ayipotadhi
we took a numbers like 0&1 to start the series

num = 0
num_2 = 1
limit_ = int(input("Enter a number:"))
print(num,num_2,end=" ")
for i in range(1,limit_+1):
    all_ = num + num_2
    num = num_2
    num_2 = all_
    print(all_,end = " ")

3.calculator

val_ = int(input("Enter a number:"))
val_2 = int(input("Enter a number:"))
user_in = int(input("enter \n1.add \n2.sub \n3.mul \n4.power \n5.div \n6.modulus \n:"))
if user_in == 1:
    print(val_ + val_2)
elif user_in == 2:
    print(val_ - val_2)
elif user_in == 3:
    print(val_ * val_2)
elif user_in == 4:
    print(val_ ** val_2)
elif user_in == 5:
    print(val_ / val_2)
elif user_in == 6:
    print(val_ % val_2)
else:
    print("exit")

4. print a table

table_ = int(input("Enter  a number:"))
for val in range(1,13):
    print(f"{table_} X {val} = {table_ * val}")
5. perfect number
ex: 6 = 1+2+3
 sum of multiples of a number = given number
 ignore the given number

6. ATM code 
'''
