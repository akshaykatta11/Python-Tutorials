# Opening and Writing in the file.

file1 = open("Mydata.txt", 'w')

file1.write("Hie from Akshay!\n")

file1.close()

# Copying the data of a file and appending it in other file.
f1 = open("Hello.txt", 'r')
f2 = open("Mydata.txt", 'a')

for i in f1:
    f2.write(i)

f2.close()
f1.close()
