# Constructor in Single Level and MultiLevel Inheritance

class A:
    def __init__(self):
        print("init of A")

    def feature1(self):
        print("Feature 1-A working")

class B(A):
    def __init__(self):
        super().__init__()
        print("init of B")

    def feature1(self):
        print("Feature 1-B working")


a1 = A()    # Calls constructor of its own class.
a2 = B()    # Calls constructor of its own class.

a3 = B()    # if super() is used then constructor of both the class will be called
