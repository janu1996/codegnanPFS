**comparator thinking:**

**1.sorting rule**



**sort()--> ascending order**

**arr = \[1 4 2 9 5]**

**arr.sort()**

**output=\[1 2 3 4 5 9]**



**sorted:**

**arr = \[5 2 8 1]**

**result = sorted(arr)**

**print(result)**



**key**

**arr = \["apple","cat",,"human","dog"]**

**using length**

**print(sorted(arr,key=len))**



**2.multiple comparator thinking:**



**words =\["cat","apple","dog","ball"]**

**first sort by length if length is same sort**

**alphabetically using lambda**



**code:**

**words = \["cat", "apple", "dog", "ball", "ant", "bat"]**



**words.sort(key=lambda x: (len(x), x))**



**print(words)**



**dry run**

**words = \["cat","apple","dog","ball"]**

**first sort by length if length is same sort**

**alphabetically using lambda**

**words = \["cat","apple","dog","ball"]**

**words.sor(key=lambda x:(len(x),x))**

**(3,cat)**

**(5,apple)**

**(3,dog)**

**(4,ball)**

**\["cat,"dog",ball,apple]**



**sort students by**

**1)marks descending**

**2)name alphabetically**

**students =\[("ravi",85),("anil",90),("bharat",85),("kiran",90)]**

**three level comparator**

**students =\[("ravi",85),("anil",90),("bharat",85),("kiran",90)]**

**students.sort(key=lambda x:(-x\[1],x\[0]))**



**-x\[1]=marks in descending order**

**x\[0]-->sorting name in ascending order**



**sort by number of vowels**

**words=\["apple","sky","education","cat","rhythm"]**



**code:**

**words = \["apple", "sky", "education", "cat", "rhythm"]**



**words.sort(key=lambda x: sum(1 for ch in x if ch in "aeiou"))**



**print(words)**



**1.sort by number of vowels**

**words=\["apple","sky","education","cat","rhythm"]**



**code:**

**def count\_vowels(word):**

&#x20;   **count = 0**



&#x20;   **for i in word:**

&#x20;       **if i in "aeiou":**

&#x20;           **count += 1**



&#x20;   **return count**





**words = \["apple","sky","education","cat","rhythm"]**



**result = sorted(words, key=count\_vowels)**



**print(result)**



**output:**

**\['sky', 'rhythm', 'cat', 'apple', 'education']**



**-----------------**

**2.sort by last digit**

**numbers =\[123,45,78,89,91,34,62]**



**code:**

**numbers = \[123, 45, 78, 89, 91, 34, 62]**

**result = sorted(numbers, key=lambda x: x % 10)**

**print(result)**

**o/p:**

**\[91, 62, 123, 34, 45, 78, 89]**

**-----------------------**

**3.sort by frequency**

**numbers=\[4,1,2,2,3,3,3,1,4,4,4]**



**code:**

**numbers = \[4, 1, 2, 2, 3, 3, 3, 4, 4, 4]**



**frequency = {}**



**for i in numbers:**

&#x20;   **frequency\[i] = frequency.get(i, 0) + 1**



**result = sorted(numbers, key=lambda x: frequency\[x])**



**print(frequency)**

**print(result)**

**o/p:**

**{4: 4, 1: 1, 2: 2, 3: 3}**

**\[1, 2, 2, 3, 3, 3, 4, 4, 4, 4]**

**-----------------------**

**4.sort numbers by distance from target**

**given target 10, sort numbers by their distance from 10**



**numbers =\[15,3,8,20,12,7]**

**target=10**



**code:**

**numbers = \[15,3,8,20,12,7]**

**target=10**

**result =sorted(numbers,key=lambda x: abs(x-target))**

**print(result)**



**o/p:\[8, 12, 7, 15, 3, 20]**





**=======================**

**sorting:**

**1) comparison based sorting**

**directly comparing the values/elements**

1. **bubble sort**
2. **selection sort**
3. **insertion sort**
4. **merge sort**
5. **quick sort**
6. **heap sort**



**2)non-comparison**

**-->we don't do the direct soring on the elements**

**1.counting sort**

**2.bucket sort**

**3.radix sort**



**==================**

**1.bubble sort:**

**initial : 7 4 1 5 3**

**compare 7 and 4**

**since 7>4 : swap**

**4 7 1 5 3**

**compare 7 and 1**

**since 7>1 : swap**

**4 1 7 5 3**

**compare 7 and 5**

**since 7>5 :swap**

**4 1 5 7 3**

**compare 7 and 3**

**since 7>3 : swap**

**4 1 5 3 7**

**comparison 2:**

**compare 4 and 1**

**since 4>1 : swap**

**1 4 5 3 7**

**compare 4 and 5**

**5>4 so no swapping required**

**1 4 5 3 7**

**compare 5 and 3**

**since 5>3 : swap**

**1 4 3 5 7**

**comparison 3:**

**compare 1 and 4**

**1<4 so no swapping is required**

**1 4 3 5 7**

**compare 4 and 3**

**since 4>3**

**1 3 4 5 7**



&#x20;**Q.12 15 145 144 1 9 7 120 11 bubble sort**

**code:**

**numbers = \[12, 15, 145, 144, 1, 9, 7, 120, 11]**



**n = len(numbers)**



**for i in range(n):**

&#x20;   **for j in range(0, n - i - 1):**

&#x20;       **if numbers\[j] > numbers\[j + 1]:**

&#x20;           **numbers\[j], numbers\[j + 1] = numbers\[j + 1], numbers\[j]**



**print(numbers)**

**o/p:**

**\[1, 7, 9, 11, 12, 15, 120, 144, 145]**



**algorithm:**

**for every pass:**

**compare neighbouring elements**

**swap if left >right**

**repeat until array is sorted.**



**code: method 2**

**def bubble\_sort(arr):**

&#x20;   **n = len(arr)**



&#x20;   **for i in range(n - 1):**

&#x20;       **for j in range(n - i - 1):**

&#x20;           **if arr\[j] > arr\[j + 1]:**

&#x20;               **arr\[j], arr\[j + 1] = arr\[j + 1], arr\[j]**



&#x20;   **return arr**





**numbers = \[12, 15, 145, 144, 1, 9, 7, 120, 11]**



**result = bubble\_sort(numbers)**



**print(result)**

**---------------------**

**2.selection sort:**

**algorithm:**

**1. Start from index 0**

**2. Assume current element is the minimum**

**3. Store its index in min\_index**

**4. Compare it with all remaining elements**

**5. If a smaller element is found:**

&#x20;     **update min\_index**

**6. After finding the smallest element,**

&#x20;     **swap arr\[i] with arr\[min\_index]**

**7. Repeat for the remaining unsorted elements**

**8. Stop when the array is sorted**



**Q.12 15 145 144 1 9 7 120 11 selection sort**



**code:**



**arr = \[12, 15, 145, 144, 1, 9, 7, 120, 11]**



**n = len(arr)**



**for i in range(n - 1):**

&#x20;   **min\_index = i**



&#x20;   **for j in range(i + 1, n):**

&#x20;       **if arr\[j] < arr\[min\_index]:**

&#x20;           **min\_index = j**



&#x20;   **arr\[i], arr\[min\_index] = arr\[min\_index], arr\[i]**



**print(arr)**



**o/p:**

**\[1, 7, 9, 11, 12, 15, 120, 144, 145]**



==============================================

**3.Insertion sort**

**algorithm:**

**start from index 1**

**store the current element in key**

**set j =i-1**

**compare arr\[j] with key**

**if arr\[j]>key:**

&#x09;**shift arr\[j] to right**

**decrease j**

**repeat until correct position found**

**insert key at arr\[j+1]**

**code:**

**def insertion\_sort(arr):**

&#x20;   **for i in range(1, len(arr)):**

&#x20;       **key = arr\[i]**

&#x20;       **j = i - 1**



&#x20;       **while j >= 0 and arr\[j] > key:**

&#x20;           **arr\[j + 1] = arr\[j]**

&#x20;           **j -= 1**



&#x20;       **arr\[j + 1] = key**



&#x20;   **return arr**





**arr = \[5, 3, 4, 1, 2]**



**print(insertion\_sort(arr))**

**o/p:**

**\[1,2,3,4,5]**

**-----------------------------**

**4.merge sort**



**code:**

**def merge\_sort(arr):**

&#x20;   **if len(arr) > 1:**

&#x20;       **mid = len(arr) // 2**



&#x20;       **left = arr\[:mid]**

&#x20;       **right = arr\[mid:]**



&#x20;       **merge\_sort(left)**

&#x20;       **merge\_sort(right)**



&#x20;       **i = 0**

&#x20;       **j = 0**

&#x20;       **k = 0**



&#x20;       **# Compare elements from left and right**

&#x20;       **while i < len(left) and j < len(right):**

&#x20;           **if left\[i] < right\[j]:**

&#x20;               **arr\[k] = left\[i]**

&#x20;               **i += 1**

&#x20;           **else:**

&#x20;               **arr\[k] = right\[j]**

&#x20;               **j += 1**

&#x20;           **k += 1**



&#x20;       **# Copy remaining elements from left**

&#x20;       **while i < len(left):**

&#x20;           **arr\[k] = left\[i]**

&#x20;           **i += 1**

&#x20;           **k += 1**



&#x20;       **# Copy remaining elements from right**

&#x20;       **while j < len(right):**

&#x20;           **arr\[k] = right\[j]**

&#x20;           **j += 1**

&#x20;           **k += 1**





**arr = \[5, 3, 4, 1, 2]**



**merge\_sort(arr)**



**print(arr)**



**o/p: \[1 2 3 4 5]**



**algo:**

def  merge_sort(arr):
    if len(arr)>1:
        mid =len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    mergesort(left)
    mergesort(right)
    i=0
    j=0
    k=0
    while i <len(left) and j<len(right):
        if left[i]<right[j]:
            arr[k]=left[i]
            i+=1
        else:
            arr[k]=right[j]
        j+=1
        k+=1
        while i<len(left)
        arr[k]=left[i]
        i+=1
        k+=1
        while j<len(right):
            arr[k]=right[j]
            j+=1\
            k+=1
            arr=[5,3,4,1,2]

