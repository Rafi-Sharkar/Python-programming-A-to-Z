#                   static variable
# * When a variable is  define inside a class, but outside the method, it is called static variable or class variable.
# * Static variable can be called directly by the class but not through the instances.

class abc:
    a=10    # static or class variable
    def setvalue(self):
        self.b = 20     # instance variable
        c = 30          # local variable
        print(c)

print(abc.a)
obj = abc()         # for calling instance variable we have to make an object
obj.setvalue()      # when we called setvalue() c also print
print(obj.b)
print(obj.a)        # we can call class or static variable by the name of class or object both ways



#                     Static Method 
# * Static method are also called class method and it can't have self keyword as parameter.
# * Static method (class method) can access only static variable (class variable)
# * Static method can be called without creating an object it means we can call the static method with the reference of the class name. 


class abc1:
    def show():    # static or class method
        print("Hello abc1")
    def display(self):
        print("welcome")

abc1.show()     #static method called by its class
obj1 = abc1()
obj1.display()  #non-static method called by creating object and called that object

# abc1.display()       # will show error 
# obj1.show()          # will show error



# Example of static variable and method
# Program to count the no. of objects of a class.

class abc:
    countobj = 0
    def __init__(self):
        abc.countobj = abc.countobj +1

ob1 = abc()
ob2 = abc()
ob3 = abc()
ob4 = abc()
print("No. of object=",abc.countobj)

