# Bubble Sort

class Sorting:
    def __init__(self, list):
        self.list = list

    def sort(self):
        for i in range(len(self.list)-1):
            for j in range(i+1, len(self.list)):
                if self.list[i] > self.list[j]:
                    self.list[i], self.list[j] = self.list[j], self.list[i]
        return self.list

list1 = []
number = int(input("Enter Size of List: "))
for i in range(number):
    print("Enter", (i+1), "element:", end="")
    list1.append(int(input()))

print("\nList before Sorting: ", end="")
for i in list1:
    print(i, end=" ")

s1 = Sorting(list1)
list1 = s1.sort()

print("\nList After Sorting: ", end="")
for i in list1:
    print(i, end=" ")
