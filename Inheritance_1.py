# Inheritance: Single Level and MultiLevel Inheritance

# Parent Class or Super Class
class A:

    def feature1(self):
        print("Feature 1 Working")

    def feature2(self):
        print("Feature 2 Working")

# Child Class or Subclass
class B(A):     # Single Level Inheritance

    def feature3(self):
        print("Feature 3 Working")

    def feature4(self):
        print("Feature 4 Working")

class C(B):     # MultiLevel Inheritance

    def feature5(self):
        print("Feature 5 Working")

# Class A object can access only 2 of its Features
a1 = A()
a1.feature1()
a1.feature2()

# Class B object can access all features of class A and its own
b1 = B()
b1.feature1()
b1.feature2()
b1.feature3()
b1.feature4()

# Class C object can access features of class A, Class B and its own
c1 = C()
c1.feature1()
c1.feature2()
c1.feature3()
c1.feature4()
c1.feature5()
