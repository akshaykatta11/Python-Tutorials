# Operator Overloading = Every Operator in python has its class which calls its method in background.

class Stud:

    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):  # '+' Operator has this __add__() that is called in the background whenever we use it.
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Stud(m1, m2)  # Creating Object
        return s3  # Returning Object

    def __str__(self):
        # Converting these integer values to string using format.
        return "{} {}".format(self.m1, self.m2)

s1 = Stud(45, 67)
s2 = Stud(56, 89)

s3 = s1 + s2  # Overloading '+' Operator

print("S3_M1:", s3.m1, "S3_M2:", s3.m2)

a = 9
print("A:", a)  # Here the call to variable prints the value of that variable
#                 i.e in background it calls __str__() method.

# But when we print object of a Class it gives us the address of it
print(s3)   # <__main__.Stud object at 0x00E30E50>  Same method __str__() is called whenever we print something.

# So after Overloading __str__() method
print("After Overloading:", s3)
