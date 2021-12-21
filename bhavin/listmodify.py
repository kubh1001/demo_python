"""to find out the length of the list"""

# list1 = ("tiogo","verna","swift","altroz")
# print(len(list1))

"""to get the index no value from the list

you can add more then 1 list as well here and get the no"""

# list2 = ("tata","hyundai","suzuki")

# print(list1[2],list2[1])

"""Slicing - that will use for tuple, string an list and using to get the required value"""

"""example with tuple data type"""
# car = ("hyundai","tiago","altroz","verna","I10","i20","nexon","amaze")
# print(car[1:6:3])

# print(car[:16:3])

# print(car[1::3])

# print(car[::3])


"""example with list data type"""


# car =["hyundai","tiago","altroz","verna","I10","i20","nexon","amaze"]
# print(car[1:6:3])

# print(car[:16:3])

# print(car[1::3])

# print(car[::3])

"""example with 2 different list"""


# name = ["bhavin", "nihar","satis","rohan","vijay",5,6,7,8,9]

# print(car[::2], name[1:10:4])

"""LIST method

1 - append - to append the vlaue (this will add teh value at the end)
2 - insert  - this will also will add the value but on a specific place"""


car =["hyundai","tiago","altroz","verna","I10","i20","nexon","amaze"]
# car.append("bmw")
# print(car)

car.insert(3,"jaguar")

# print (car)
name = ["bhavin", "nihar","satis","rohan","vijay",5,6,7,8,9]
# name.append("prity")
name.insert(4,"swity")
print (car, name)


car.extend(name)

print (car)

list2 = ("tata","hyundai","suzuki")



car.index("tiago")
print(car.index("tiago"))