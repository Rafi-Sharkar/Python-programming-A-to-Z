#               Abstract class
# Abstract class is a declarator. For this we have to take "from abc import ABC, abstractmethod" and "class class_name(ABC):""
# Then take decorator "@abstractmethod"
# And define a empty function which method will must be use in its sub class like "class ractangle(shape)"
# If any sub class miss that abstract method then compiler throws error


from abc import ABC, abstractmethod

class shape (ABC):          # This is the abstract class for abstract method
    @abstractmethod         # decorator
    def area(self):         # This is the abstract method
        pass

class rectangle(shape):
    def area(self):
        self.l = int(input("Enter length :"))
        self.b = int(input("Enter breadth :"))
        self.ar = self.l* self.b
        print("Area of rect",self.ar)
class circle(shape):
    def area(self):
        self.r = float(input("Enter radius :"))
        self.ar = 3.1416*self.r**2
        print("Area of circle=",self.ar)



class square(shape):
    def area(self):
        self.side = int(input("Enter calue of side :"))
        self.ar = self.side * self.side
        print("Area of square=",self.ar)   

ob1 = rectangle()
ob1.area()
ob2 = circle()
ob2.area()
ob3 = square()
ob3.area()


