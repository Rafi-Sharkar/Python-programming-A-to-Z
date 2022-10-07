# Instance variable & class variable

            # Types of variavle


class abc:
    a=10        #class variable

    def fun(self,b):    # "self" keyword represents the instance of a class
                        # "b" inside fun paramiter is local variavle
        self.b=20       # "b" is instance variable






# Memory Repesentation of object

class University:
    collage = "GTC"
    def setvalue(self,r,n,c):
        self.rollno = r
        self.name = n
        self.course = c
    def display(self):
        print(self.rollno)
        print(self.name)
        print(self.course)

std1 = University()
std2 = University()

std1.setvalue(101, "Rafi", "CSE203")
std2.setvalue(603, "Tanjirul", "Tex204")
print(std1.collage)
print("This is for student 1")
std1.display()
print("This is for student 2")
std2.display()