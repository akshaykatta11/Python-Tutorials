# Inner Class

# Outer Class
class Student:

    def __init__(self,name,prn):
        self.name = name
        self.prn = prn
        self.lap = self.Laptop()    # Creating Object of Inner Class inside Outer Class

    def show(self):
        print("Name:", self.name, "PRN:", self.prn)
        self.lap.show()     # Calling Inner Class Method

    # Inner Class
    class Laptop:

        def __init__(self):
            self.brand = "Legion"
            self.cpu = 'i5'
            self.ram = 8

        def show(self):
            print("Brand:", self.brand, "Processor:", self.cpu, "RAM:", self.ram)


s1 = Student("Akshay", 21)

s1.show()
Lap1 = Student.Laptop()     # Creating Object of Inner Class outside Outer Class.
