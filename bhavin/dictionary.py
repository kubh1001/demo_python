from typing import ValuesView


# abc = {"name":"bhavin","age":"30"}
# abc["name"]= "nihar"

# # print (abc)

# abc["height"] = "6.5"
# print (abc)

# print (abc.keys()) 

# print (abc.values())
# print (abc.items())


# name = {"fruit":("mango","banana","apple","graps")}
# print(name["fruit"])



bio = {
        "name":["bhavin","nihar",[3,5,7,98],{"age":28,"education":"graduate"}],
        "city":"abad",
        "extra":
        {"age":28,"education":"graduate"},
     
        }

# [3,5,7,98]
# bio["name"][2]
# print(bio["name"],["age"])
# print(bio["city"])
# print (bio["age"])








animals           = ['python','gopher']
more_animals      = animals
print(animals == more_animals)
print(animals is more_animals)
even_more_animals = ['python','gopher']
print(animals == even_more_animals)
print(animals is even_more_animals) 
print (animals is)