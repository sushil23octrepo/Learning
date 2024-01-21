# Converting a String to a List:
# Since both string and list objects are sequences, they are interconvertible. Hence,
# if we cast a string object to a list, modify the list either by insert(), 
# append() or remove() methods and convert the list back to a string, to get back the modified version.

# We have a string variable s1 with WORD as its value. With list() built-in function, 
# let us convert it to a l1 list object, and insert a character L at index 3. 
# The we use the join() method in str class to concatenate all the characters.

s1="WORD"
print ("original string:", s1)
l1=list(s1)

l1.insert(3,"L")

print (l1)

s1=''.join(l1)
print ("Modified string:", s1)

#Output:
# original string: WORD
# ['W', 'O', 'R', 'L', 'D']
# Modified string: WORLD


# Using the Array Module
# To modify a string, construct an array object. Python standard library includes array module.
# We can have an array of Unicode type from a string variable.
# Now, with the help of tounicode() method, get back the modified string

import array as ar

s1="WORD"
print ("original string:", s1)

sar=ar.array('u', s1)
sar.insert(3,"L")
s1=sar.tounicode()

print ("Modified string:", s1)

# It will produce the following output −
# original string: WORD
# Modified string: WORLD


