# x= input("type your number :")

# for i in x :
#     print (i)
#     if (x is str):
#         break

# x = input("enter the no")
# for i in x :
#     print (i)
#     if x==str:
 #         break


# try:
#     x = int(input("enter the numbber :"))
#     print (x)
# except:
#     print ("this is not a integer..")

# x = int(input("enter any number :"))
# for i in x:
#     if type(x)==str:
#         break
#     print (i)

# num=int(input("Enter any number"))
# f=1
# for i in range(1,num+1):
#     f=f*i
# print("Factorial is",f)

# num=int(input("Enter any number"))
# s=0
# while(num):
#    r=num%10
#    s=s+r
#    num=num//10
# print("Sum of digits is",s)

# x = int(input("emter the number  :"))
# s=0
# for i in x:
#     print (i)

# num=(input("Enter any number"))
# while(num):
#     if num==str:
#         break

# def abc (*kwargs):
#     total = x+y
#     multiply =  (x*y)
#     print (total)
#     print (multiply)
# abc (x = 5, y = 7))

# f = open ("test.txt","r")
# print (f.read(2))

# f = open ("test.txt","w")
# f.write ("this is a updated verson")
# f.close

# f = open("test.txt","w")
# f.write ("I have updated the sheet with old content/Hope this is a good thing/If you feel not to update then replave with older one")
# f.close





# x = (input("enter your latter : "))

# while x == str:
#     break
# print (x)

while True:
    data = input("Please enter a loud message (must be all caps): ")
    if data is range (1,1000):
        print("Sorry, your response was not loud enough.")
        continue
    else:
        #we're happy with the value given.
        #we're ready to exit the loop.
        break
