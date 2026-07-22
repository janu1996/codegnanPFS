'''
File Handling
--------------
-->File handler is an object that gives more options like creating, updating

We have two ways to open the file...\

1.open()
--------
syntax:- we need to close it manually
do = open('file_name','mode')
----------
-----
---
close()

ex:-
do = open('demo.txt.txt','r')
print(do.read())

2.with(keyword)
---------------
syntax:- no need to use close function
with open('file_name','mode') as do:
    print(do.read())

eg:-
with open('demo.txt.txt','r') as do:
    print(do.read())

===============================
Modes
-----
1.r-->read
--> used to read the file, incase if the file is not present it will
       raise error
eg:-
with open('demo.txt.txt','r') as do:
    print(do.read())
    
2.w-->write
--> used to write the text inside the file and it will override the text
        inside file, incase if the file is not present it will create a new
        file with the name given...
(okavela file lekapotey aa file create chesi  text ni add chestadhi)
eg:-
with open('demo.txt.txt','w') as do:
    print(do.write('this is python class'))
eg2:-(it will create a new file and add this text incase if the file is not exists)
with open('dem.txt.txt','w') as do:
    print(do.write('this is python class'))

3.a--> append
-->This is used to add the text at last position inside the file

eg:-
with open('demo.txt','a') as do:
    print(do.write('we are use file handling'))

4.x -->create a file
-->this is used to create a new file by adding a text inside the file,incase if the file
   is present  it will raise an error......
eg:-
with open('hello.txt','x') as do:
    print(do.write('we are use file handling'))

==============================
Functionalities
---------------
1.write() 
--------
-->This function is used to add the text inside a file or update a file
with new text.....
eg1:-
with open('dem.txt.txt','w') as do:
    print(do.write('this is python class'))

eg2:-
with open('demo.txt','a') as do:
    print(do.write('we are use file handling'))

2.read()
--------
--> used to read a file and this read() will read file chunk by chunk...(line by line)
    we can also specify the size
eg:-
with open('demo.txt','r') as do:
    print(do.read(5))

3.readline()
------------ 
--> This readline() function will read only one line at a time...
eg:-
with open('demo.txt','r') as do:
    print(do.readline())

4.readlines()
------------
--> this function will read whole file and give it in a list each lines is
one index in that list........
eg:
with open('demo.txt','r') as do:
    print(do.readlines())
eg1:
with open('demo.txt','r') as do:
    print(do.readlines(9))


'''
with open('demo.txt','r') as do:
    print(do.readlines(9))
