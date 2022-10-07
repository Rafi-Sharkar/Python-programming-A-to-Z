#        Inheritance
class ABC:          # Declare the mother or super class ABC
    pass
class XYZ(ABC):     # XYZ is a sub or derived class of ABC
    pass            # I can easily go to ABC through XYZ


#           Types of Inheritance
#   1. Single Inheritance
#   2. Multilevel Inheritance
#   3. Multiple Inheritance
#   4. Hierarchical Inheritance
#   5. Hybrid Inheritance


#           01_Single Inheritance
# In this inheritance a derived class inherits the single base class

class A:
    pass
class B(A):  #one super class has only one sub class 
    pass

# Exercise of single Inheritance

class employee:
    def input_data(self):
        self.__empno = int(input("Enter employee no::"))
        self.__name = input("Enter name ::")
        self._salary = int(input("Enter salary ::"))  #when we use __ before variable like __salary then the variable is privet for that class
class manager (employee):
    def calculation(self):
        self.__pf = self._salary*10/100
        self.__netsalary = self._salary - self.__pf
        print("PF=",self.__pf)
        print("Net salary=",self.__netsalary)

emp=manager()
emp.input_data()
emp.calculation()




