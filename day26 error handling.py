'''
ERROR HANDLING
---------------
1.Syntax Error
--> It comes when the statement is incomplete
ex:-
for j in range(1,10 :
     print(j)
o/p:-
-->SyntaxError
expected ':'

2.indentataion Error
-->It occurs when the indentatation is not correct
ex:-
   a = 20   
for j in range(a)
     print(j)
else:
    print()

o/p:- IndentationError
unexpected indenet

3.Value Error

ex:-
num = int(input("Enter a num:"))
o/p:-
ValueError

ValueError: invalid literal for int()

--------------------------------------------
Exception Handling 
--> Using try,except,esle, finally

1.try
The try block will test the code for error
syntax:- try:

2.Except
This except let us handle the errors in the code
syntax:-  except:
else
finally

ex:-
try:
    print(num)
except:
    print('will get name error')

ex2:- name error
try:
    print(any_)
except NameError:
    print('will get name error')

ex3:- Value error
try:
    num = int(input("Enter a num:"))
except ValueError:
    print('will get value error')

ex4:- 2 exceptions
try:
    num = int(input("Enter a num:"))
    num_2 = int(input("Enter a num:"))
    print(num / num_2)
except ZeroDivisionError:
    print('will get Zerodivision  error')
except ValueError:
    print('Will get value error')

ex5:- using else
try:
    num = int(input("Enter a num:"))
    num_2 = int(input("Enter a num:"))
    print(num / num_2)
except ZeroDivisionError:
    print('will get Zerodivision  error')
except ValueError:
    print('Will get value error')
else:
    print('No Error')

----------------------------
3.else
if the try block does not have any error than the else block will execute
or else it will never get into else block
ex:-
try:
    num = int(input("Enter a num:"))
    num_2 = int(input("Enter a num:"))
    print(num / num_2)
except ZeroDivisionError:
    print('will get Zerodivision  error')
except ValueError:
    print('Will get value error')
else:
    print('No Error')

---------------------------------
4.finally
error tho sambandham undadhu it will run even if the error is there or not
-->The finally block will execute either code contains errors or not
ex:-
try:
    num = int(input("Enter a num:"))
    num_2 = int(input("Enter a num:"))
    print(num / num_2)
except ZeroDivisionError:
    print('will get Zerodivision  error')
except ValueError:
    print('Will get value error')
else:
    print('No Error')
finally:
    print('end')

'''

try:
    num = int(input("Enter a num:"))
    num_2 = int(input("Enter a num:"))
    print(num / num_2)
except ZeroDivisionError:
    print('will get Zerodivision  error')
except ValueError:
    print('Will get value error')
else:
    print('No Error')
finally:
    print('end')
