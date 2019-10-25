# Duck Typing = If there is a object that has a method than that's it we are not consent about which class objec Nit
#               that required method is, we are just consent that it should have that required method.
# Duck Typing is somewhat like Interface in Java.

class Pycharm:
    def execute(self):
        print("Compiling")
        print("Running")

class Notepad:
    def execute(self):
        print("Only Typing")

class Software:
    def code(self, ide):
        ide.execute()

# Creating Objects of Pycharm and Notepad Class
ide1 = Pycharm()
ide2 = Notepad()

# Creating Object of Software Class
s1 = Software()

# Passing objects of Pycharm and Notepad Class to Software Class object as a parameter.
s1.code(ide1)
s1.code(ide2)


