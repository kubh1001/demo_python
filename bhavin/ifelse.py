a = 20
y = 50

# if a>10 or y<20:
#     print(a+y)
# else:
#     print ("not print anything")
# if ((a+y)==70) and y ==40 or ((a+y)!=60):
#     print ("conditions are good")

# a = 20
# y = 50

# if ((a+y) >80):
#     print ("not looks real")
# elif a==30:
#     print ("still not loosk real")
# elif y==50:
#     print ("now looks good and real")
# else:
#     print("all the above conditions are not correct/")


"""writing a program related to voting that person is eligible or not"""

# x = int(input ("age of the candidate :"))
# y = "yes"
# z = "no"
# if x>=18:
#     print(y)
# else:
#     print (z)
""" on test paper its mention like

why have added int with the age?

age=int(input("Enter your age"))
if age >=18:
   print("Eligible for voting")
else:
   print("not eligible for voting")"""

# age=int(input("Enter your age"))
# if age >=18:
#    print("Eligible for voting")
# else:
#    print("not eligible for voting")


# x = input("name of the candidate")
# print (x)

# x = 5
# print (6%2 ==0)

# print (5%2)

# for number in range (1,100) :
#     print (number)

# x = int(input("enter a number :"))
# if (x%2==0):
#     print ("HELLO") 
# else:
#     ("Number is not multiple of 5")


""" Write a program to calculate the electricity bill (accept number of unit from user) 
according to the following criteria :
             Unit                                                     Price  
First 100 units                                               no charge
Next 100 units                                              Rs 5 per unit
After 200 units                                             Rs 10 per unit
(For example if input unit is 350 than total bill amount is Rs2000)"""




# x = int (input ("units consumed :"))

# if x<=100:
#     print ("electricity bill of the user",x*0)
# elif x>100 and x<=200 :
#     print (("electricity bill of the user --> ", x*5))
# elif x>200 :
#     print("electricity bill of the user",x*10)
# else:
#     print("not faling on any condition")


"""Write a program to check whether the last digit of a number( entered by user ) is 
divisible by 3 or not."""

# x = int(input("enter a number :"))
# y = (x%10)
# if y%3==0:
#     print ("Number is divisible by 3")
# else:
#     print("number is not devisible by 3")

x =float(input("pecentage of student :"))
if x>90:
    print("pass with A grade")
elif x>80 and x<=90 :
    print("pass with B grade")
elif x>=60 and x<=80 :
    print("pass with C grade")
elif x<60 :
    print("pass with D grade")
else:
    print("not faling on any condition")
