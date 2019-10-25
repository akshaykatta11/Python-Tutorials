# File Handling
# In files, We have two modes 1) Character Mode & 2) Binary Mode

# Opening and Reading the file

file1 = open("Hello.txt", 'r')      # 'r' = open file for reading purpose.

print("To print Single line from the data:", file1.readline())
print("To read whole data:", file1.read())

file1.close()