# Classes and Objects

# Class creation
class Computer:

    # Method declaration and Definition
    def config(self):
        print("Core: i5, RAM: 8GB, Storage: 2TB")


# Object creation
comp = Computer()

# Calling Method --> Class_Name.method_name(object_name)
Computer.config(comp)

# Another Way of Calling Method using Object
comp.config()
