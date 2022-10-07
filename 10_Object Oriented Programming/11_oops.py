#       Seter & Geter
# if i need to get privet variable go out  the class method. for this we use set or get method.

class abc:
    def setvalue(self):
        self.__x = 10
    def set1(self):     # seter. for edit the value of object
        self.__x = 200
    def get1(self):     # geter. return the value out from the class
        return self.__x

obj = abc()
obj.setvalue()
print(obj.get1())
obj.set1()
print(obj.get1()) 


#           Methods for class variable

#   getattr()  ---> to access the variable of class
#   setattr()  ---> to update the value of class variable
#   delattr()  ---> to remove the variable of class
#   hasattr()  ---> to check an variable is belongs to class

class abc1:
    x=10
print(getattr(abc1,"x"))
setattr(abc1,"x",200)
print(abc1.x)
delattr(abc1,"x")
# print(abc1.x)


