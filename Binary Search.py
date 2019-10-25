# Binary Search

class ABC:

    def __init__(self, list, num):
        self.list = list
        self.num = num

    def search(self):
        l = 0
        u = len(self.list) - 1

        while l<=u:
            mid = (l + u) // 2
            if(self.list[mid] == self.num):
                globals()['pos'] = mid
                return True
            else:
                if self.list[mid] < self.num:
                    l = mid+1
                else:
                    u = mid-1
        return False

list1 = []
pos = -1
number = int(input("Enter Number of Elements you want: "))
for i in range(number):
    print("Enter", (i+1), "element:", end="")
    list1.append(int(input()))

print("List is:", end="")
for i in list1:
    print(i,end=" ")

search_key = int(input("\nEnter Element to search: "))

a1 = ABC(list1, search_key)

if a1.search():
    print("Element Found at:", pos+1)
else:
    print("Element Not Found!")
