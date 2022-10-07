#               Hierarchical Inheritance
# In this inheritance, a super-class can be inherited into more than one sub-classes.

# all child class have only one super/ mother class

class student:
    def input_data(self):
        self.Rollno = int( input("Enter your roll no::"))
        self.name = input("Enter your name::")
        self.m1 = int( input("Enter mark1::"))
        self.m2 = int( input("Enter mark2 ::"))
        self.m3 = int( input("Enter mark3 ::"))
class btech(student):
    def result(self):
        self.__tm = self.m1 +self.m2 +self.m3
        self.__per = self.__tm*100/300
        print("Total marks=",self.__tm)
        print("Percentange=",self.__per)
class mca(student):
    def result(self):
        self.__tm = self.m1 +self.m2 +self.m3
        self.__per = self.__tm*100/300
        print("Total marks=",self.__tm)
        print("Percentange=",self.__per)

std1=btech()
std1.input_data()
std1.result()
std2=mca()
std2.input_data()
std2.result()


#           Hybrid Inheritance
# This type of inheritance, consists of multiple types of inheritance

class student:
    def show (self):
        print("Hello Student")
class cs(student):
    def msg1(self):
        print("cs student",)
class ec(student):
    def msg2(self):
        print("Ec student")
class college(ec,cs):
    def msg3(self):
        print("welcome")
    
std = college()
std.show()
std.msg1()
std.msg2()
std.msg3()