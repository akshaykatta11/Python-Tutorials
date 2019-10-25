# Selection Sort

class Selection:
    def __init__(self, list):
        self.list = list

    def sorting(self):
        print("\nIteration: ")
        for i in range(len(self.list)):
            min = i
            for j in range(i, len(self.list)):
                if self.list[j] < self.list[min]:
                    min = j
            self.list[i], self.list[min] = self.list[min], self.list[i]
            # Print every Iteration as in how it looks!
            print(self.list)

        return self.list

number = int(input("Enter size of List: "))
list1 = []
for i in range(number):
    print("Enter", (i+1), "element: ", end="")
    list1.append(int(input()))

print("List Before Sorting: ", end="")
for i in list1:
    print(i, end=" ")

s1 = Selection(list1)

list1 = s1.sorting()

print("List After Sorting: ", end="")
for i in list1:
    print(i, end=" ")
