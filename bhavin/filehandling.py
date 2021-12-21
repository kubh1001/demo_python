f = open("test.txt","r")
# print (f.readlines())


for i in f.readlines():
    print (i[2])

print (f.readline()[2])