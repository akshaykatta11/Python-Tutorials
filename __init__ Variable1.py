# Using Special __init__ Method A.K.A Constructor

class Profile:

    def __init__(self):
        self.name = "Akshay"
        self.age = 22

    def update(self):
        self.name = input("Enter Name: ")
        self.age = int(input("Enter Age: "))

emp1 = Profile()
emp2 = Profile()

emp2.update()

if (emp1.age == emp2.age) and (emp1.name == emp2.name):
    print("They have Same Age!")
else:
    print("They have Different Name and Age!")

print("Name:", emp1.name, "& Age: ", emp1.age)
print("Name:", emp2.name, "& Age: ", emp2.age)

