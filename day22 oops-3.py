'''
Inheritance
-------------
-->Inheritance is an oop concept where one class (child/derrived) acquired
the properties and methods of another class (parent/base)

syntax:
class parent:
    pass
class chinld(parent):
    pass

types
------
1.single inheritance
--------------------
A child class inherits from one parent is single inheritance
(one way traffic)

eg:-
class animal:
    def sound(self):
        print('Animals make sounds')
class dog(animal):
    def barks(self):
        print('Dog barks')
d = dog()
d.sound()
d.barks()

eg1:-
class father:
    def land(self):
        print('5 ar of land')
class son(father):
    def flat(self):
        print('3BHK flat')
s = son()
s.land()
s.flat()

2.multiple inheritence
----------------------
A Child class inherits more than one parent is called multiple inheritence

eg:
class father:
    def skills(self):
        print('Driving')
class mother:
    def talent(self):
        print('cooking')
class son(father,mother):
    def mine(self):
        print('coding')
all_ = son()
all_.skills()
all_.talent()
all_.mine()

eg1:
class father:
    def skills(self):
        print('Driving')
class mother:
    def talent(self):
        print('cooking')
class sister:
    def learn(self):
        print('python')
class son(father,mother,sister):
    def mine(self):
        print('coding')
all_ = son()
all_.skills()
all_.talent()
all_.learn()
all_.mine()

eg2:-
class father:
    def skills(self):
        print('Driving')
class mother:
    def talent(self):
        print('cooking')
class brother:
    def learn(self):
        print('math')
class daughter(father,mother,brother):
    def mine(self):
        print('writter')
all_ = daughter()
all_.skills()
all_.talent()
all_.learn()
all_.mine()

3. Multi-level
----------------
one child class becomes the parent for another class

eg:-
class grandfather:
    def house(self):
        print('Owns House')
class father(grandfather):
    def flat(self):
        print("New 3bhk flat")
class son(father):
    def car(self):
        print('Have a car')
fam = son()
fam.house()
fam.flat()
        
eg2:-
class grandfather:
    def house(self):
        print('Owns House')
class father(grandfather):
    def flat(self):
        print("New 3bhk flat")
class son(father):
    def car(self):
        print('Have a car')
fam = son()
fam.house()
fam.flat()
fam.car()        

4.Hierarical
--------------
--> Multiple childs inherits from the same parent
(single parent multiple childs)

eg:-
class mother:
    def gold(self):
        print('10 KG gold')
class pinky(mother):
    def show(self):
        print('Will get 5 kg gold')
class yuktha(mother):
    def show_2(self):
        print('will get remaining 5 kg gold')

child_1 = pinky()
child_2 = yuktha()

child_1.gold()
child_1.show()

child_2.gold()
child_2.show_2()

eg2:-
class father:
    def land(self):
        print('6 arc of land')
class charan(father):
    def show(self):
        print('will get 2 arc of land')
class chaitu (father):
    def show_2(self):
        print('will get remaining 2 arcs of land')
class krishna(father):
    def show_3(self):
        print('Last 2 arcs of land')
child_1 = charan()
child_2 = chaitu()
child_3 = krishna()

child_1.land()
child_1.show()

child_2.land()
child_2.show_2()

child_3.land()
child_3.show_3()

5.Hybrid inheritance
---------------------
--> This is the combination of two or more types of inheritance
example of multiple + multi-level

eg:-
class A:
    def methodA(self):
       print('Class A')
class B(A):
    def methodB(self):
        print('Class B')
class C(A):
    def methodC(self):
        print('Class C')
class D(B,C):
    def methodD(self):
        print('Class D')

so = D()    # anni call cheyakunda d okati call chesam 
so.methodA()
so.methodB()
so.methodC()
so.methodD()

----------------------
super()
------
--> this super() function is used to access the parent class methods or
constructor in the child class...

paricular parent class mnunchi inheritance access chesi vere danilo use cheyachu
eg:- for methods
class parent:
    def show(self):
        print('Parent method')
class child(parent):
    def show(self):
        super().show()
        print('child class')
chi_ = child()
chi_.show()

eg:- for constructor

class person:
    def __init__(self, name):
        self.name = name
class student(person):
    def __init__(self,name,roll):
        super().__init__(name)
        self.roll = roll
    def dispaly(self):
        print(self.name)
        print(self.roll)
an = student('Teja',101)
an.dispaly()

'''
class person:
    def __init__(self, name):
        self.name = name
class student(person):
    def __init__(self,name,roll):
        super().__init__(name)
        self.roll = roll
    def dispaly(self):
        print(self.name)
        print(self.roll)
an = student('Teja',101)
an.dispaly()
