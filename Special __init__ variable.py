# Special __init__ Variable

class Computer:

    # Defining Constructor
    def __init__(self, cpu, ram):
        self.processor = cpu
        self.RAM = ram

    def config(self):
        print("Core: ", self.processor, "RAM: ", self.RAM)

# Object Creation
comp1 = Computer('i5', 8)
comp2 = Computer('AMD', 16)

# Method Calling
comp1.config()
comp2.config()
