'''
Triple quotes --> Multiline comments-->Doc string

flow
variables-->operators -->Datatypes(Numeric,Collections(Str,List,Tuple,
sets,Dicts)-->Control Block (logic) (if,elis,else,for,while,break,continue,
pass) -->Procedue oriented programming (Functions) -->OOP(class,objects)

3 steps we need to follow  to write a code
we need to know and follow
1. input 
2.output 
3.Logic

string: immutable

name = "Condegnan"
batch = 23
email_id = "saketh@codegnan.com"
print(len(email_id))

#sclicing -->[start:end] ending value is always excluded
print(email_id[7:15])

#lists -->Mutable collection
email_ids =['saketh@codegnan.com','support@codegnan.com',
            'krishna@mvits.com','info@codegnan.com']
print(len(email_ids))
print(email_ids[1])

#last two emailids from the collection
#-1  starts couting from reverse indexing 
print(email_ids[-2:]) #best method
print(type(email_ids[-2]))
print(email_ids[-2:-1])
print(type(email_ids[-2:-1]))

#store 3 more mailids into above at a time
email_ids =['saketh@codegnan.com','support@codegnan.com',
            'krishna@mvits.com','info@codegnan.com']
excess_email = ['rani@codegnan.com','swathi@codegnan.com','ramu@codegnan.com']
email_ids.extend(excess_email)
print(email_ids)

email_ids.exend(['a@yahoo.com','b@icloud.com','e@gmail.com'])
print(email_ids)

#access each mail id one by one --->loops
for mail in email_ids:
    #print(mail)
    print(f'Mail id of a person is {mail}')

email_ids =['saketh@codegnan.com','support@codegnan.com',
            'krishna@mvits.com','info@codegnan.com']
#store the emailids with relevant user names
# get the above email_ids into the above users dictionary
users = {}
print(type(users))

users = dict.fromkeys(email_ids)
print(users)
users['saketh@codegnan.com'] =2345
print(users)

#All pyhton built-in datatypes are built-in functions
#(int,float,str,list,tuple,set,dict,bool)


email_ids =['saketh@codegnan.com', 'support@codegnan.com', 'krishna@mvits.com',
            'info@codegnan.com', 'rani@codegnan.com', 'swathi@codegnan.com', 'ramu@codegnan.com','santosh@deliotte.com']
users = {}
print(type(users))
print(users)
for i in range(len(email_ids)):
    #print(i,email_ids[i])
    users[i+1] = email_ids[i]
print(users)
'''
email_ids =['saketh@codegnan.com', 'support@codegnan.com', 'krishna@mvits.com',
            'info@codegnan.com', 'rani@codegnan.com', 'swathi@codegnan.com', 'ramu@codegnan.com','santosh@deliotte.com']
#enumerate -->it provides  by default a counter object(you can store in desired collection)
data = dict(enumerate(email_ids))
print(data)

#python -->object
#Functions --> First class obects because one function can be called as an argument,input and can pass to another function
#why set is unordered - it does not have index because its work is to take unique order.
#list ordered because it has indexing.

