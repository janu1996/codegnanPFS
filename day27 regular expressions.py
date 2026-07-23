'''
Regular Expressions(RegEx)
--------------------------
-RegEx is a sequence of character that can searching pattern
- To use the RegEx we have to import re module....
syntax --> import re

functionalities
---------------
1.findall()
------------
-->It will find all the char that are in the string....
output will be in the list form
ex:-
mport re
txt = 'python is a language and also called dynamically typed'
print(re.findall('[a]',txt))
o/p:-['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a']

ex1:-
import re
txt = 'python is a language and also called dynamically typed'
print(re.findall('[an]',txt))
o/p:- ['n', 'a', 'a', 'n', 'a', 'a', 'n', 'a', 'a', 'n', 'a', 'a']

2.search()
----------
-->It will find only the first occurance of the letter
-->The search will find the char ,but it will give only
the first sequence that found in the string....
ex:-
import re
txt = 'python is a language and also called dynamically typed'
print(re.search('[a]',txt))
o/p:- <re.Match object; span=(10, 11), match='a'>

3.split()
---------
--> it splits 
eg:-
import re
txt = 'python is a language and also called dynamically typed'
print(re.split(' ',txt))
o/p:-['python', 'is', 'a', 'language', 'and', 'also', 'called', 'dynamically', 'typed']

4.sub()
-------
same as replace
eg:-
import re
txt = 'python is a language and also called dynamically typed'
print(re.sub(' ','&',txt))

o/p:-python&is&a&language&and&also&called&dynamically&typed

5.fullmatch()
-------------

====================
Metacharacters
Meta char
---------
--> any thing we need to keep in string only
1.[]
eg:- we can also search single char
import re
txt = 'I have 100 Ruppee'
print(re.findall('[a-z]',txt))
print(re.findall('[A-Z]',txt))
print(re.findall('[0-9]',txt))


print(re.search('[a-z]',txt))
print(re.search('[A-Z]',txt))
print(re.search('[0-9]',txt))

2.^
checks weather the first char is matched or not
eg:-
import re
txt = 'I have 100 Ruppee'
print(re.findall('^I have',txt))
print(re.search('^I have',txt))

3.$
checks the endings matches or not
eg:-
import re
some = 'I am going to school'
print(re.findall('school$',some))
print(re.search('school$',some))

4. .(dot)
one dot represents one character
ex:-
import re
any_ = 'Hello! This is teja'
print(re.findall('T..s',any_))

ex1:-
import re
any_ = 'Hello! This is Teja'
print(re.findall('T...',any_))
print(re.search('T...',any_))

5.*
star will take either 0 or n-number of characters
ex:-
import re
how = 'python module will going complete this week '
print(re.findall('p.*n',how))

ex1:-
import re
how = 'python module will going complete this week '
print(re.findall('p.*ython',how))

ex2:-
import re
how = 'python module will going complete this week '
print(re.findall('p.*',how))

eg3:-
import re
how = 'python module will going complete this week '
print(re.findall('p.*',how))
print(re.findall('p.*ython',how))
print(re.findall('p.*n',how))
print(re.search('p.*n',how))

6.+
it will take from 1 char to n-number of characters
eg:-
import re
now = 'python is a language '
print(re.findall('p.+ython',now))
print(re.findall('p.+thon',now))
print(re.findall('p.+',now))
print(re.search('p.+a',now))


7.{}
we can specify specific size then it will find based on indexing
if the size is not there it will give empty string
eg:-
import re
now = 'python is a language '
print(re.findall('p.{10}',now))
print(re.search('p.{5}',now))


'''
import re
now = 'python is a language '
print(re.findall('p.{10}',now))
print(re.search('p.{5}',now))
