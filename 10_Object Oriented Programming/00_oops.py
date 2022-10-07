#Creating Empty Class
class classname:
    pass

#Defining Method Inside A Class
class classname:
    def method (self):
        pass

#Creating Object of a class
objectname = classname()

#Accessing Member Of Class
class message:      #Class declaration
    def msg1(self):     #Defining method inside class
        print("hi")
    def msg2(self):     #Defining method inside class
        print("Bye")

mobj = message()        #creating object through class
mobj.msg1()         #calling the method for this object
mobj.msg2()         #calling the method for this object