class Person:
    university_name = "Vignan University" #Class Attriubute
    student_count = 0

    def __init__(self, name, age, Edu_BG, Gender, Department):
        self.name = name
        self.age = age
        self.Edu_BG = Edu_BG
        self.Gender = Gender
        self.Department =Department

    def display_info(self):
        #Method to be overridden
        pass


    #---------------Student------------------

class Student(Person):
    def __init__(self, name, age, student_id, course, year_, Edu_BG, Gender, Department):
        super().__init__(name, age, Edu_BG, Gender, Department)

        self.__student_id = student_id
        self.course = course
        self.year_ = year_
        
        Student.student_count += 1

    def display_info(self):
        print("\n-----------------Student Details-----------------------")
        print("University:", Person.university_name)
        print("Name      :", self.name)
        print("Age       :", self.age)
        print("Student ID:", self.__student_id)
        print("Course    :", self.course)
        print("Year      :", self.year_)
        print("Education :", self.Edu_BG)
        print("Gender    :", self.Gender)
        print("Department:", self.Department)

    def get_student_id(self):
        return self.__student_id

    @classmethod
    def total_students(cls):
        print("Total Students :" ,cls.student_count)

   #------------------Faculty----------------------------
class Faculty(Person):
    faculty_count = 0
    def __init__(self, name, age, faculty_id, Department, Edu_BG, Gender):
        super().__init__(name, age, Edu_BG, Gender, Department)

        self.__faculty_id = faculty_id

        Faculty.faculty_count += 1
    def display_info(self):
        print("\n-----------------Faculty Details-----------------------")
        print("University:", Person.university_name)
        print("Name      :", self.name)
        print("Age       :", self.age)
        print("Faculty ID:", self.__faculty_id)
        print("Education :", self.Edu_BG)
        print("Gender    :", self.Gender)
        print("Department:", self.Department)

    @staticmethod
    def university_policy():
        print("\nUniversity Policy:")
        print("Vignan University follows strict academic policies.")

    @classmethod
    def total_faculty(cls):
        print("Total Faculty Members :",cls.faculty_count)

  #------------------------BusDriver-----------------------
class Driver(Person):
    driver_count = 0

    def __init__(self, name, age, Edu_BG, driver_id, Department, Gender, Bus_Number, Bus_Route, license_id): 
        super().__init__(name, age, Edu_BG, Gender, Department)

        self.__driver_id = driver_id
        self.__Bus_Route = Bus_Route
        self.__Bus_Number = Bus_Number
        self.__license_id = license_id

        Driver.driver_count += 1

    def display_info(self):
        print("\n------ Driver Details ------")
        print("University     :", self.university_name)
        print("Name           :", self.name)
        print("Age            :", self.age)
        print("Driver ID      :", self.__driver_id)
        print("Education      :", self.Edu_BG)
        print("Gender         :", self.Gender)
        print("Department     :", self.Department)
        print("Bus Route      :", self.__Bus_Route)
        print("Bus Number     :", self.__Bus_Number)
        print("License ID :", self.__license_id)

    def get_driver_id(self):
        return self.__driver_id

    @classmethod
    def total_drivers(cls):
        print("Total Drivers :", cls.driver_count)

        #------------------------Non Teaching Staff---------------------------------
class Staff(Person):
    staff_count = 0
    def __init__(self, name, age, staff_id, Department, Edu_BG, Gender):
        super().__init__(name, age, Edu_BG, Gender, Department)

        self.__staff_id = staff_id

        Staff.staff_count += 1
    def display_info(self):
        print("\n-----------------Staff Details-----------------------")
        print("University:", Person.university_name)
        print("Name      :", self.name)
        print("Age       :", self.age)
        print("Staff ID  :", self.__staff_id)
        print("Education :", self.Edu_BG)
        print("Gender    :", self.Gender)
        print("Department:", self.Department)

    @staticmethod
    def university_policy():
        print("\nUniversity Policy:")
        print("Vignan University follows strict academic policies.")

    @classmethod
    def total_staff(cls):
        print("Total Staff Members :",cls.staff_count)

    #------------------------Workers--------------------------------
class Worker(Person):
    worker_count = 0
    def __init__(self, name, age, worker_id, Department, Edu_BG, Gender):
        super().__init__(name, age, Edu_BG, Gender, Department)

        self.__worker_id = worker_id

        Worker.worker_count += 1
        
    def display_info(self):
        print("\n-----------------Worker Details-----------------------")
        print("University:", Person.university_name)
        print("Name      :", self.name)
        print("Age       :", self.age)
        print("Worker ID :", self.__worker_id)
        print("Education :", self.Edu_BG)
        print("Gender    :", self.Gender)
        print("Department:", self.Department)

   
    @classmethod
    def total_worker(cls):
        print("Total Workers:",cls.worker_count)
   


        #-----------------------Objects--------------------------

student1 = Student("Rahul Sharma",21,"22NM1A0561","Computer Science",2022,"Intermediate","Male","IT")
student2 = Student("Annanya Reddy",24,"22NM1A0574","Computer Science",2020,"Intermediate","Female","IT")
student3 = Student("Pallavi",18,"23NM1A0457","Electronics and Communications",2024,"Dipoloma","Female","IT")
student4 = Student("Ravi",19,"24VF0287","Artificial And Intellegence",2026,"Dipoloma","Male","IT")

faculty1 = Faculty("Dr. Ravi Kumar",45, "F001","AI & ML","PhD","Male")
faculty2 = Faculty("Dr. Meera Srinivas",50,"F002","CyberSecurity","PhD","Female")
faculty3 = Faculty("J. Priyanka",30,"F003","Python","M.Tech","Female")
faculty4 = Faculty("B.Krishna Chaitanya",36,"F004","Java Programming","PhD","Male")
faculty5 = Faculty("k.Ramani",45,"F005","Web Developer","M.Tech","Female")

driver1 = Driver("Vivek kumar",28,"SSC","DV001","Transport","Male","3341","Akkayapalam","DL123456")
driver2 = Driver("Sammera",27,"NIL","DV002","Transport","Female","3745","Carshed","DL789012")
driver3 = Driver("Naidu",50,"SSC","DV003","Transport","Male","2286","Madhurwada","DL869054")
driver4 = Driver("Kumar",45,"NIL","DV004","Transport","Male","2276","R&B","DL904567")
driver5 = Driver("Satish",29,"Inter","DV005","Transport","Male","9613","Seetammadara","DL871236")

staff1 = Staff("Kalyani",30,"S001","libraian","B.Tech","Female")
staff2 = Staff("Swathi",28,"S002","Lab Incharge","B.Tech","Female")
staff3 = Staff("Kishore",40,"S003","Transport Incharge","B.Tech","Male")
staff4 = Staff("Kiran",50,"S004","Training and Placement","Phd","Male")
staff5 = Staff("Vedhavathi",32,"S005","Exam Cell","M.Tech","Female")
staff6 = Staff("Prakash",48,"S006","Accounts","Bsc.Computers","Male")

worker1 = Worker("Parvathi",55,"W001","Cleaner","Nill","Female")
worker2 = Worker("Simhachalam",59,"W002","Electrian","Nill","Male")
worker3 = Worker("Kumari",45,"W003","Cleaner","Nill","Female")
worker4 = Worker("Siva",32,"W004","Plumber","Nill","Male")
worker5 = Worker("Rishi",52,"W005","Attender","Inter","Male")

    #----------------------Output----------------------------

student1.display_info()
student2.display_info()
student3.display_info()
student4.display_info()

print("\nStudent ID:",student1.get_student_id())

faculty1.display_info()
faculty2.display_info()
faculty3.display_info()
faculty4.display_info()
faculty5.display_info()

Faculty.university_policy()

driver1.display_info()
driver2.display_info()
driver3.display_info()
driver4.display_info()
driver5.display_info()

print("\nDriver ID:",driver1.get_driver_id())

staff1.display_info()
staff2.display_info()
staff3.display_info()
staff4.display_info()
staff5.display_info()
staff6.display_info()

Staff.university_policy()

worker1.display_info()
worker2.display_info()
worker3.display_info()
worker4.display_info()
worker5.display_info()

Student.total_students()
Faculty.total_faculty()
Driver.total_drivers()
Staff.total_staff()
Worker.total_worker()
