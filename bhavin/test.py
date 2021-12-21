# s = 'foo'
# t = 'bar'
# print("barf" in ("barf of the day"))

# abc = "bhavin"

# print ("bhavin" in ("abc"))


# print(ord("a"))

# abc = ("a","b","c","d","e","f","g","h",)

# print (abc[-1:-6:-2])

s = 'foobar'


print (s[:])
print(s[::-1][::-1])

print(s[::-1][::-1] is s)

print(s[::-1][::-1] == s)

"""want to understand why this above mentioned one is not true where as the below one is comming as true"""
print(s[:] is s)
# print (s[0] + 
# s[-1])
# print (s[::-1][::-5])
# s[::-1][-1] + s[len(s)-1]
# print (s[len(s)-1])
# print (len(s))
# print(s[len(s)-1])

# print (s[5])
# abc = ("a","b","c","d","e","f","g","h",)
# print (abc[::1])


"""s[::-1] reverses s, but creates a reference to a new object. An additional [::-1] slice reverses it again,
 so it is equal to the original s. But it is not the same object:"""


x = {"name":"bhavin","fruit":"apple"}
print (x.keys())