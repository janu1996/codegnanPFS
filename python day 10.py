'''
1.prime num(single)
num = int(input("Enter a number:"))
count = 0
for j in range(1,num+1):
    if num % j == 0:
        count += 1
if count == 2:
    print(f"{num} is a prime")
else:
    print(f"{num} is  not a prime")

2.generating prime num
limit_ = 10
for j in range(2,limit_+1):
    count = 0
    for i in range(1,j+1):
        if j % i == 0:
            count += 1
           
    if count == 2:
        print(f"{j} is a prime")

3. patterns
right angle traingle
end use cheste side by side vastadhi
2nd for loop mi end cheyadaniki manam print use chesam so that it will go to next iteration  
*
* *
* * *
* * * *
* * * * *
print like this
num = 5
for j in range(1,num+1):
    for i in range(1,j+1):
        print("*", end = " ")
    print()

4. same as  above but by using numbers
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
num = 5
for j in range(1,num+1):#  used to print next numbers 
    for i in range(1,j+1):
        print(j, end = " ")
    print()
reverse
num = 4

for j in range(num,0,-1):
    for i in range(1,j+1):
        
        print(j ,end = " ")
    print()
5.
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5

num = 5
for j in range(1,num+1):
    for i in range(1,j+1):
        print(i, end = " ")
    print()
reverse
num = 4

for j in range(num,0,-1):
    for i in range(1,j+1):
        
        print(i ,end = " ")
    print()


6.
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15

num = 5
count = 0
for j in range(1,num+1):
    for i in range(1,j+1):
        count += 1
        print(count ,end = " ")
    print()
7. reverse of 6th question
num = 4
count = 0
for j in range(num,0,-1):
    for i in range(1,j+1):
        count += 1
        print(count ,end = " ")
    print()
# to print right side use space into num

8.amstrong
 length of given number ni andulo lo unna each number ki aa length ni multiply chesi add cheste given number ravali
 153 = 1^3 + 5^3 + 3^3 = 153

am_str = int(input("Enter a number:"))
length_= len(str(am_str))
all_sum = 0
for j in str(am_str):
    all_sum += int(j) ** length_
if all_sum == am_str:
    print(f"{am_str} is a amstrong")
else:
    print(f"{am_str} is  not a amstrong")

9. pyramid
  *
* * *
num = 10
for j in range(num):
    print(" " *(num - j -1),end = " ") # defines position
    print("*" * (2 * j + 1))


'''

