class abc:
    def setvalue(self):
        self.__x = 10
    def set1(self):     # seter. for edit the value of object
        self.__x = 200
    def get1(self):     # geter. return the value out from the class
        return self.__x

obj = abc()
abj.setvalue()
print(obj.get1())
obj.set1()
print(obj.get1()) 