#           Polymorphism

#operator overloading
#operator overloading is an Example of polymorphism whose meaning is to use an operator on different form without changing its basic meaning.

# For example
#use operator with class object             //method , operator or object
#1. predefined
#2. user defined


class customer:
    def __init__(self,s,c):
        self.sale = s
        self.comm = c
    def __add__(self,t):
        temp = customer(0,0)
        temp.sale=self.sale +t.sale
        temp.com = self.comm +t.comm
        return temp
    def display(self):
        print("sale=",self.sale)
        print("comm=",self.com)

cust1 =customer(10000,500)
cust2 = customer(20000,1000)
cust3 = customer(0,0)

cust3 = cust1 + cust2
cust3.display()



# code with harry ---> 
# at first compilor found instant variable


class A:
    classvar1 = "I am a class variavle in class A"
    def __init__(self):
        self.var1 = "I am inside class A's constructor"
        self.classvar1 = "instance var in class A "
class B(A):
    classvar1 = "I am in class B"

a=A()
b=B()
print(b.classvar1)      #first compilor go class B if there have no then go to the refered super class. In this case compilor first found the instance variable B --> A, then found class variable B --> A .


# Override concept 


class A:
    classvar1 = "I am a class variavle in class A"
    def __init__(self):
        self.var1 = "I am inside class A's constructor"
        self.classvar1 = "instance var in class A "
        self.special = "Special"    #i need to print it rather ther this constractor was overrided
class B(A):
    classvar1 = "I am in class B"
    def __init__(self):    # This constractor override the super class's constractor
        super().__init__()
        self.var1 = "I am inside class A's constructor"
        self.classvar1 = "instance var in class A "   # if i comment it then output will "I am in class B" super class's constractor was overrided


a=A()
b=B()
print(b.special,b.var1,b.classvar1)   
