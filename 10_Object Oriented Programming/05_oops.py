#               * Method Overriding
#               * super Function

class abc:
    a = 20
    def msg(self):
        print("Hello abc")
class xyz(abc):
    a = 30
    def msg(self):
        print("HEllo xyz")        #  msg method of xyz will override msg method of abc class
        super().msg()
        print(xyz.a)
        print(abc.a)
        print(super().a)

obj= xyz()
obj.msg()


class a:
    def __init__(self):
        print("Hello a")

class b(a):
    def __init__(self):
        print("Hello b")
        super().__init__()

obj1 = b()

    