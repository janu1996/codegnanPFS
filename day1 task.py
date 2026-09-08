'''
Question 1: Student Marks Manager

marks = []

# Accept three marks
for i in range(3):
    mark = int(input("Enter mark: "))
    marks.append(mark)

print("\nOriginal marks:", marks)

# Insert 90 at the beginning
marks.insert(0, 90)
print("After inserting 90:", marks)

# Add 75 and 85
marks.extend([75, 85])
print("After extending with 75 and 85:", marks)

# Check and remove 75
if 75 in marks:
    marks.remove(75)
    print("75 was removed.")

# Remove the final mark
removed_mark = marks.pop()
print("Removed final mark:", removed_mark)

# Final result
print("Final marks:", marks)
print("Number of marks:", len(marks))

-----------------------
Question 2: Number List Analyser

numbers = [20, 10, 30, 20, 40, 20]

# Sort in ascending order
numbers.sort()
print("Ascending order:", numbers)

# Reverse to descending order
numbers.reverse()
print("Descending order:", numbers)

# Ask user for a number
search = int(input("\nEnter a number to search: "))

# Check whether number exists
if search in numbers:
    print("Number found!")
    print("Count:", numbers.count(search))
    print("First index:", numbers.index(search))
else:
    print("Number not found.")

# Numerical summary
print("\nSmallest value:", min(numbers))
print("Largest value:", max(numbers))
print("Total:", sum(numbers))

-------------------------------
Question 3: Even and Odd Number Separator

numbers = [10, 15, 20, 25, 30, 35]

even = []
odd = []

# Separate even and odd numbers
for number in numbers:
    if number % 2 == 0:
        even.append(number)
    else:
        odd.append(number)

print("Original list:", numbers)
print("Even numbers:", even)
print("Odd numbers:", odd)

# Slicing
print("\nFirst three values:", numbers[:3])
print("Last three values:", numbers[-3:])

# Create backup
backup = numbers.copy()

# Clear original list
numbers.clear()

print("\nAfter clearing:")
print("Original list:", numbers)
print("Backup list:", backup)

----------------------------
Question 4: Unique Name Manager

names = ["Asha", "Rahul", "Asha", "John", "Rahul"]

# Convert list to set
unique_names = set(names)

print("Original names:", names)
print("Unique names:", unique_names)

# Add Meera
unique_names.add("Meera")

# Add Arun and Priya
unique_names.update(["Arun", "Priya"])

# Check and remove John
if "John" in unique_names:
    unique_names.remove("John")
    print("\nJohn was removed.")

# Try to remove David safely
unique_names.discard("David")

# Display every unique name
print("\nFinal unique names:")

for name in unique_names:
    print(name)

-------------------------------
Question 5: Course Student Comparison

python_students = {"Asha", "Rahul", "John", "Meera"}
da_students = {"Rahul", "Meera", "Arun"}

# Union
all_students = python_students.union(da_students)

# Intersection
both_courses = python_students.intersection(da_students)

# Students only in Python
only_python = python_students.difference(da_students)

# Students in only one course
only_one = python_students.symmetric_difference(da_students)

# Relationship checks
da_subset = da_students.issubset(python_students)
python_superset = python_students.issuperset(da_students)
disjoint = python_students.isdisjoint(da_students)

# Display results
print("Students in both courses:")
for student in all_students:
    print(student)

print("\nStudents learning both Python and DA:")
for student in both_courses:
    print(student)

print("\nStudents only in Python:")
for student in only_python:
    print(student)

print("\nStudents learning only one course:")
for student in only_one:
    print(student)

print("\nIs DA a subset of Python?", da_subset)
print("Is Python a superset of DA?", python_superset)
print("Are the two sets disjoint?", disjoint)

---------------------------------------



'''
