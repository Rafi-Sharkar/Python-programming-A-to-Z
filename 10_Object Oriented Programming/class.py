# class my_class:
#     x=5
    
# # p1= my_class()
# print(my_class().x)

# class Person:
#   def __init__(self, name, age):
#     self.n = name
#     self.age = age

# p1 = Person("John", 36)

# print(p1.n)
# print(p1.age)

# class Person:
#   def __init__(self, name, age):
#     self.n = name
#     self.a = age

#   def myfunc(self):
#     print("Hello my name is " + self.n)

# p1 = Person("John", 36)
# p1.myfunc()

class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.n = name
    mysillyobject.a = age
    print(mysillyobject.n)

  def myfunc(abc):
    print("Hello my name is " + abc.n)

p1 = Person("John", 36)
p1.myfunc()
