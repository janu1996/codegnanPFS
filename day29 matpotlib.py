'''
Matplotlib
---------
Matplotlib library is an python library that proveds functionalities
to charts,graphs, bar and data visualization.

ex:-
import matplotlib.pyplot as plt
x = [1,2,3,4,5]
y = [10,20,15,30,5]

plt.plot(x,y)
plt.show()

ex1:-
import matplotlib.pyplot as plt
x = [1,2,3,4,5]
y = [10,20,15,30,5]

plt.plot(x,y)
plt.title('Simple Plot')
plt.show()

ex2:-
import matplotlib.pyplot as plt
x = [1,2,3,4,5]
y = [10,20,15,30,5]

plt.plot(x,y)
plt.title('Simple Plot')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.show()

1. Line plot
example : sales of  cars (line plot)
import matplotlib.pyplot as plt
x = [2026,2025,2024,2023,2022]
y = [120,150,135,95,70]

plt.plot(x,y)
plt.title('Car Sales')
plt.xlabel('Years')
plt.ylabel('Number of Cars ')
plt.show()

2.Bar chart
eg:-
import matplotlib.pyplot as plt
x = [2026,2025,2024,2023,2022]
y = [120,150,135,95,70]

plt.bar(x,y)
plt.title('Car Sales')
plt.xlabel('Years')
plt.ylabel('Number of Cars ')
plt.show()

eg1:-
import matplotlib.pyplot as plt
x = [2026,2025,2024,2023,2022]
y = [120,150,135,95,70]

plt.bar(x,y,color='red')
plt.title('Car Sales')
plt.xlabel('Years')
plt.ylabel('Number of Cars ')
plt.show()

eg3:-
import matplotlib.pyplot as plt
x = [2026,2025,2024,2023,2022]
y = [120,150,135,95,70]

plt.bar(x,y,color='red',edgecolor='black')
plt.title('Car Sales')
plt.xlabel('Years')
plt.ylabel('Number of Cars ')
plt.show()

ex4:-
import matplotlib.pyplot as plt
x = ['AUDI','BMW','VERNA','DESIRE','SWIFT','XZEN' ,'TAR']
y = [120,150,135,95,70,85,150]

plt.bar(x,y,color='Yellow',edgecolor='red')
plt.title('Car Sales')
plt.xlabel('Car Brands')
plt.ylabel('Number of Cars sold ')
plt.show()

3.Pie chart
eg:-
import matplotlib.pyplot as plt
subjects_ = ['Python','Java','C']
stu_ = [69,79,50]

plt.pie(stu_,labels = subjects_)
plt.title('Course')

plt.show()

eg1: to get which color which subject
import matplotlib.pyplot as plt
subjects_ = ['Python','Java','C']
stu_ = [69,79,50]

plt.pie(stu_,labels = subjects_)
plt.legend(subjects_)
plt.title('Course')

plt.show()

eg2:- to get percentage
import matplotlib.pyplot as plt
subjects_ = ['Python','Java','C']
stu_ = [69,79,50]

plt.pie(stu_,labels = subjects_,autopct='%1.1f%%')
plt.legend(subjects_)
plt.title('Course')

plt.show()

eg3:- add color
import matplotlib.pyplot as plt
subjects_ = ['Python','Java','C']
stu_ = [69,79,50]

plt.pie(stu_,labels = subjects_, colors=['red','yellow','purple'],autopct='%1.1f%%')
plt.legend(subjects_)
plt.title('Course')

plt.show()

4.Scatter plot :display only dots
eg:
import matplotlib.pyplot as plt
x = ['AUDI','BMW','VERNA','DESIRE','SWIFT','XZEN' ,'TAR']
y = [120,150,135,95,70,85,150]

plt.scatter(x,y,color='red')
plt.title('Car Sales')
plt.xlabel('Car Brands')
plt.ylabel('Number of Cars sold ')
plt.show()

all mix:
eg:
import matplotlib.pyplot as plt
x = ['AUDI','BMW','VERNA','DESIRE','SWIFT','XZEN' ,'TAR']
y = [120,150,135,95,70,85,150]

plt.plot(x,y,color='blue')
plt.title('Car Sales')
plt.xlabel('Car Brands')
plt.ylabel('Number of Cars sold ')
plt.show()


plt.scatter(x,y,color='red')
plt.title('Car Sales')
plt.xlabel('Car Brands')
plt.ylabel('Number of Cars sold ')
plt.show()

plt.bar(x,y,color='yellow',edgecolor='black')
plt.title('Car Sales')
plt.xlabel('Car Brands')
plt.ylabel('Number of Cars sold ')
plt.show()

plt.pie(y,labels = x,autopct='%1.1f%%')
plt.legend(x)
plt.title('Car Sales')
plt.show()

all3 in one:

import matplotlib.pyplot as plt
x = ['AUDI','BMW','VERNA','DESIRE','SWIFT','XZEN' ,'TAR']
y = [120,150,135,95,70,85,150]

plt.plot(x,y,color='blue')
plt.scatter(x,y,color='red')
plt.bar(x,y,color='yellow',edgecolor='black')
plt.title('Car Sales')
plt.xlabel('Car Brands')
plt.ylabel('Number of Cars sold ')
plt.show()

5.Histograh:

import matplotlib.pyplot as plt
y = [10,40,20,50]
plt.hist(y,bins=20)
plt.title('Car Sales')
plt.xlable('years')
plt.ylable('Number of cars')
plot.show()
 '''
import matplotlib.pyplot as plt
x = ['AUDI','BMW','VERNA','DESIRE','SWIFT','XZEN' ,'TAR']
y = [120,150,135,95,70,85,150]

plt.plot(x,y,color='blue')
plt.scatter(x,y,color='red')
plt.bar(x,y,color='yellow',edgecolor='black')
plt.title('Car Sales')
plt.xlabel('Car Brands')
plt.ylabel('Number of Cars sold ')
plt.show()
