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



#Built-in modules -->math,random,os, time,datetime

#We download modules -->pypi(Python Package Index)

#Build a QRCode Scanner using Python -->Linkedin URl
#pyqrcode,png
#pip install pyqrcode
#pip install pypng
import pyqrcode
import png
#create a QRcode by giving a link
link = "https://www.linkedin.com/in/jahnavi-devi-078999289/"
qr = pyqrcode.create(link)
#print(qr)
qr.png("myqr.png",scale=10)

#Persoanl Bussiness card  -- name,email,phone number,website
'''
