'''
scenario to understand (*args and **kwargs)
Modules -->Some intersting cases -->Projects (Virtual Assistant ,Email autoamte
OOP --> Github (branch)

#Employee Details

def employees(*names,**settings):
    """Employee Details along with their Settings"""
    print("Employee Names")
    for employee in names:
        print('---------')
        print('-',employee)
    for key,value in settings.items():
        print("Key is",key)
        print("Value is",value)

employees('Rahul',"Akash","Saritha",
          department='Operations',
          experience_letters=True,
          Salary=True)
          
exmaple -2:
# Shopping cart

def products(*categories,**filters):
    """Product Details along with  their filters"""
    print("Product Names")
    for product in categories:
        print('-',product)
    for key,value in filters.items():
        print("Key is",key)
        print("Value is",value)
products("Mobile","headphones","powerbank",
         department ="Electronics", # differnt categories kavali  ante  we can keep in list or write with deffent name seperately
         rating =True,
         Price =True)
------------------------------------
Projects

Module --> A Module is a simple Python file(block of code) (reusable,organized code) 
key word -->import
[oka file lo unna code ni inko file lo use chese danni module antaru
ee moudle lo motham kinda uunavi anni untayi]

Employee Details/performance metrics (employee.py)
  --->employees function
  --->performance function
  --->Increment/Leardership/Learning function

OOP

Organization -->class

Encapsulation (hides),inheritance, Polymorphism   

Emplloyess -->Function (Methods)
Performance Metrics -->Function
Increement -->Function

Emp1,Emp2,Emp3, ....... -->objects

'''

#Employee Details

def employees(*names,**settings):
    """Employee Details along with their Settings"""
    print("Employee Names")
    for employee in names:
        print('---------')
        print('-',employee)
    for key,value in settings.items():
        print("Key is",key)
        print("Value is",value)


#if __name__=="__main__":

details={'Organization':'Codegan',
         'Year':2018,
         'branches':['Vijayawada','Hyderabad','Vizag']}
print(__name__) # it is called as Dunder methods -->Magic method  before--leading,after--trailing



'''



#Every  python file -->Module -->import keyword-->__name__
import sep10
print(dir(sep10)) # dir-->directory will return all available methods,attributes

'''
print(type(sep10.employees))
print(type(sep10.details))

sep10.employees("Sanjana",designation = "Trainee at Codegnan",
                location ="Vizag")
#print(sep10.details.keys())
print(sep10.details['Year'])
# 2 keys ni okasari call cheyadam avavdhu oka dani taruvatha okati call cheyali
print(sep10.details['Organization'])
sep10.details.update({'batches':['PFS','JFS','DA','AAA','DS'],
                      'employees':240})
print(sep10.details)
'''
#Every  python file -->Module -->import keyword-->__name__
import sep10
print(dir(sep10)) # dir-->directory will return all available methods,attributes


print(type(sep10.employees))
print(type(sep10.details))

sep10.employees("Sanjana",designation = "Trainee at Codegnan",
                location ="Vizag")
#print(sep10.details.keys())
print(sep10.details['Year'])
# 2 keys ni okasari call cheyadam avavdhu oka dani taruvatha okati call cheyali
print(sep10.details['Organization'])
sep10.details.update({'batches':['PFS','JFS','DA','AAA','DS'],
                      'employees':240})
print(sep10.details)


#from keyword

from sep10 import employees,details
details.update({'batches':['PFS','JFS','DA','AAA','DS'],
                      'employees':240,
                'Branch Numbers':3})
#print(details)
print(sep10.__doc__) # used to call doc string
# it returns  Doc  string from the given module




'''



