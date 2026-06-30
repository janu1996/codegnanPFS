'''
Input formating form user
i.Input()
The input function is used to take input from the user....
1. int()
eg:-
num = int(input("Enter a number:"))
num_2 = int(input("Enter a number:"))
print(num + num_2)
2.srting
eg:-
how = input("Enter a chat:")
print(how + 'Teja')
3.float
eg:-
num = float(input("Enter your salary:"))
print(num, "is the monthly salary")
 4. list
 we need to use map
 eg:-
group_ = list(map(int,input().split()))
print(group_)

group_ = list(input().split())
print(group_)


5.tuple
here also we use map
eg:-
group_ = tuple(map(int,input().split()))
print(group_)

some = tuple(input().split())
print(some)

6. eval
we can give any datatype it  will show the output
num = eval(input("Enter: "))
print(type(num))
7. f string or docstring(formatted string,documented string)
to get the value in variable we use {}
eg:-
name_ = input("Enter your name:")
age_ = int(input("Enter your age:"))
print(name_,"your age is ",age_)
print(f"{name_} your age is {age_}")
8.modulus string
%s-->takes string
%d---> takes number
to read those values it shoul consider % symbol before the variable name
eg:-
name_ = input("Enter your name:")
age_ = int(input("Enter your age:"))
print("My name is %s and i'm %d years old" %(name_, age_seperated by comma(,) is normal string
-->seperated by curly braces({}) is f string or doc string
--->seperated by modulus(%) is modulus string
'''
