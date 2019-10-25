# Linear Search

class ABC:
    def __init__(self, list, num):
        self.list = list
        self.num = num

    def search(self):
        for i in range(len(self.list)):
            if(self.list[i] == self.num):
                globals()['pos'] = i
                return True
        return False

list1 = []
pos = -1
number = int(input("Enter Number of Elements in list: "))

for i in range(number):
    print("Enter", (i+1), "Element: ", end="")
    list1.append(int(input()))

search_key = int(input("Enter Element to Search: "))

a1 = ABC(list1, search_key)

if a1.search():
    print("Element Found at:", pos+1)
else:
    print("Element Not Found!")