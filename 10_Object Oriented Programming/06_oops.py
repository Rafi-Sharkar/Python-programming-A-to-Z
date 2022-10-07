#               Multilevel Inheritance
# In this type of inheritance, a class can inherit from a child class
# One super-class and her child.then child has her sub-class,then sub-class has her sub-class and so on.


# Excercise of Multilevel Inheritance
class company:
    def input_data(self):
        self.__empno = int(input("Enter employee id ::"))
        self.__name = input("Enter name ::")
        self._salary = int(input("Enter salary ::"))
class allowance(company):
    def calculation(self):
        self._hra = self._salary*10/100
        self._da = self._salary * 5/100
        print("Hra=",self._hra)
        print("Da=",self._da)
class employee(allowance):
    def display(self):
        self.__gross = self._salary + self._hra +self._da
        print("Gross salary=", self.__gross)
emp = employee()
emp. input_data()
emp.calculation()
emp.display()



#               Multiple Inheritance
# In this type of inheritance, a class can inherit from more than one super-class
# two super-class and one child class

class student:
    def input_data(self):
        self.m1 = int(input('Enter marks1 :'))
        self.m2 = int(input('Enter marks2 :'))
        self.m3 = int(input('Enter marks3 :'))

class sports:
    def input_score(self):
        self._score1 = int(input("Enter score1 :"))
        self._score2 = int(input("Enter score2 :"))

class collage(student,sports):
    def result(self):
        self.__tm = self.m1 +self.m2 +self.m3
        self.__ts = self._score1 +self._score2
        print("Total marks=",self.__tm)
        print("Total score=",self.__ts)

std = collage()
std.input_data()
std.input_score()
std.result()



#       super() Function in multiple inheritance

class abc:
    def show (self):
        print("Hello abc")
class xyz:
    def show (self):
        print("Hello xyz")
class pqr(abc,xyz):         # First parameter will first exicute
    def show (self):
        super().show()
        print("Hello pqr")

obj2= pqr()
obj2.show()