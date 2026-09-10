'''
#Task - create a function with the usage of  *args & **args

def fn(*a,**b):
     .......
     ....... # any scenior based i do vote
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
