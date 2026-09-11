'''
#Task - create a function with the usage of  *args & **args

def fn(*a,**b):
     .......
     ....... # any scenior based 
fn(*c,**d)

'''
def fn(*a, **b):
    print("Student Subjects:")
    for subject in a:
        print(subject)

    print("\nStudent Details:")
    for key, value in b.items():
        print(key, ":", value)


c = ("Python", "SQL", "HTML")
d = {
    "Name": "Radha",
    "Age": 22,
    "Department": "CSE"
}

fn(*c, **d)

#code 2:

#task
#Creat a function withe usage of *args & **Kwargs with real time secenrio

def student_marks(*args, **kwargs):
    """Here takes student name marks and college and bank detals"""
    for student in args:
        print("Name:", student[0])
        print("Python:", student[1])
        print("SQL:", student[2])
        print("Java:", student[3])
        print()

    print("College:", kwargs["college"])
    print("Branch:", kwargs["branch"])


student_marks(
    ("Lavanya", 85, 90, 80),
    ("Likhitha", 90, 88, 85),
    college="Amrutha College",
    branch="Computer Science"
)


