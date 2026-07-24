'''
date &time
-----------

from datetime import datetime
current_ = datetime.now()
print(current_)
print(current_.strftime('%Y'))
print(current_.strftime('%m'))
print(current_.strftime('%d'))
print(current_.strftime('%H:%M:%S'))

method-2 to get date:

from datetime import datetime , date
current_ = datetime.now().today()
today = date.today()
now = datetime.now()

print(today)
print(now)

print(current_.strftime("%d/%m/%Y %H:%M:%S"))
print(current_.strftime("%d/%m/%Y %I:%M:%S %p"))

---------------------------------------------

%d --> day in the month
%m --> month in the year
%Y --> Year
%H --> hour
%M --> minute
%S --> second
%I --> 12 hour clock
%p --> AM or PM
=============================
calenders
---------
eg:
import  calendar

print(calendar.calendar(2026))
eg1:-
import  calendar

print(calendar.month(2026,7))
eg2:-
import  calendar

print(calendar.weekday(2026,7,24))

eg3:- leapyear

import  calendar
print(calendar.isleap(2026))

===================================
numpys and pandas
-----------------
-->mostly used for dataAnalysis.
-->it represents as graphs.

Data Analysis
-------------
--> Clean the data
--> transfer

what is Data Analysis?
----------------------
Data Analysis is the process of inspecting,cleaning,transform and modeling
data to discover useful insights, support decisions- making, and identify patterns.
It is widely used in industries such as finance, healthcare, marketing, and technology.

Types of Data Analysis
----------------------
1. Descriptive Analysis - Summarizing data
(e.g., average sales per month).
2. Diagnostic Analysis - Understanding causes
(e.g., why sales dropped).
3. Predictive Analysis - Forecasting future outcomes
(e.g., Predicting customer- churn)
4. Prescriptive analysis- Suggesting actions based on data
(e.g., best marketing strategies)


What is numpy
-------------
--> Numpy is a library in python which is known as numerical python
--> This Numpy have different diamentinal arrays such as 1D,2D,3D
--> to install go to cmd and use
pip install Numpy
--> To use the Numpy we have to import library as
import numpy as np
eg:-
import numpy as np
arr_1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr_1)

1D
eg:
import numpy as np
arr_1 = np.array([1,2,3,4])
print(arr_1)

2D
eg:-
import numpy as np
arr_1 = np.array([[1,2,3],[4,5,6]])
print(arr_1)

three dimensional(3D)
------------------
import numpy as np
arr_1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr_1)

------------------------------
Indexing in array
--> As we used indexing in the list or tuple, here the way it works
--> By cslling index position from array, we will get the value
--> And negative indexing also will work.
eg:-
import numpy as np
arr_1 = np.array([1,2,3,4])
print(arr_1[1])

eg1:- negative indexing
import numpy as np
arr_1 = np.array([1,2,3,4])
print(arr_1[-1])

Scling
------
import numpy as np
arr_1 = np.array([1,2,3,4])
print(arr_1[:2])

functionalities:
----------------
eg:-
import numpy as np
arr_1 = np.array([1,2,3,4])
print(arr_1.sum())
print(arr_1.mean())
print(arr_1.max())
print(arr_1.min())
============================
reshape
-------
eg:- 2D into 3D
import numpy as np
arr_1 = np.array([[1,2,3],[4,5,6]])
print(arr_1)
print(arr_1.reshape(3,2))

eg1:- 3D  ni change cheyali ante 4 values unadli 
import numpy as np
arr_1 = np.array([[1,2,3,4],[4,5,6,7],[7,8,9,10]])
print(arr_1)
print(arr_1.reshape(4,3))
===========================
Pandas
-------
-->Pandas is an powerful python library and this is built in the top of numpy
--> By using pandas data manipulation will be done...
--> Pamdas have Data Structures like series and dataframes
--> to install go to terminal pip install pandas
--> to use this we have import the library
like
import pandas as pd

eg:- Series
import pandas as pd

Data = pd.Series(
    [2000,4000,7000],
    index = ['Earphone','Charger','Mobile']
)
print(Data)

eg:- DataFrames

import pandas as pd
df = {
    "Product" : ['Laptop','Charger','Mobile'],
    "Brand": ['Mac','Realme','Iphone'],
    'price':[5700,1500,2500],
    "stock":[5,15,9],
    "Sales":['Amazon','Offline','Flipcart']
    }
data = pd.DataFrame(df)
print(data)

'''
import pandas as pd

df = {
    "Product" : ['Laptop','Charger','Mobile'],
    "Brand": ['Mac','Realme','Iphone'],
    'price':[5700,1500,2500],
    "stock":[5,15,9],
    "Sales":['Amazon','Offline','Flipcart']
    }
data = pd.DataFrame(df)
print(data)
