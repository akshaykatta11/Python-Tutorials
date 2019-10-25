# Instance Variables = Defining a variable inside init() method.
# Class/Static Variables = Defining a variable inside a class but outside init() method.

class Car:

    # Class/Static Variables
    wheels = 4

    def __init__(self):
        # Instance Variables
        self.mil = 10
        self.com = "BMW"

c1 = Car()
c2 = Car()

Car.wheels = 6

print("Company:", c1.com, "Milege:", c1.mil, "Wheels:", c1.wheels)
print("Company:", c2.com, "Milege:", c2.mil, "Wheels:", c2.wheels)

print("Wheels:", Car.wheels)
