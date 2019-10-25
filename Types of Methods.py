# Instance Method = Methods defined with "self" parameter. (works with instance variable)
# Class Method = Methods defined with "cls" parameter and @classmethod Decorators. (works with class variable)
# Static Method = Methods defined without any parameter and @staticmethod Decorators. (works with nothing)

class Student:

    # Class Variable
    School = "MESCOE"

    # Constructor
    def __init__(self,m1,m2,m3):
        # Instance Variable
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    # Instance Method  --> with "self" parameter
    def avg(self):
        return (self.m1 + self.m2 + self.m3)/3

    # Class Method --> with "cls" parameter
    @classmethod
    def getSchool(cls):
        return cls.School

    # Static Method --> with no parameter
    @staticmethod
    def info():
        print("This is Student Class!")


s1 = Student(12, 45, 78)
s2 = Student(34, 87, 56)

print("Average Of S1:", s1.avg())
print("Average Of S2:", s2.avg())
print("School:", Student.getSchool())
Student.info()
