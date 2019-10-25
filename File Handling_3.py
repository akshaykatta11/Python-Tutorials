# Creating a New copy of a binary mode file i.e "Image File"
# Binary mode has two formats: 1) rb = Read Binary. 2) wb = Write Binary.

f1 = open("Akshay_Photo.jpg", 'rb')
f2 = open("Copied_Akshay_Photo.jpg", 'wb')

for i in f1:
    f2.write(i)

f2.close()
f1.close()
