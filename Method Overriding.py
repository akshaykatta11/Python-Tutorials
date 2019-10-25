# Method Overriding = Creating Methods with same name and same no. of parameters but in different class and not in same.
# Checks in own class first and if not found then goes to parent class.
class A:

    def show(self):
        print("From A Show")

class B(A):
    pass

class C(A):

    def show(self):
        print("From C Show")


a1 = B()        # Creating object of B
a1.show()       # Output: From A Show

a2 = C()        # Creating object of C
a2.show()       # Output: From C Show
