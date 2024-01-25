numbers = {10:"Ten", 20:"Twenty", 30:"Thirty",40:"Forty"}
print ("numbers dictionary before delete operation: \n", numbers)
del numbers[20]
print ("numbers dictionary before delete operation: \n", numbers)
# Output:
# numbers dictionary before delete operation:
#  {10: 'Ten', 20: 'Twenty', 30: 'Thirty', 40: 'Forty'}
# numbers dictionary before delete operation:
#  {10: 'Ten', 30: 'Thirty', 40: 'Forty'}

#The del keyword with the dict object itself removes it from memory.
numbers = {10:"Ten", 20:"Twenty", 30:"Thirty",40:"Forty"}
print ("numbers dictionary before delete operation: \n", numbers)
del numbers
print ("numbers dictionary before delete operation: \n", numbers)

# Output:
# numbers dictionary before delete operation:
#  {10: 'Ten', 20: 'Twenty', 30: 'Thirty', 40: 'Forty'}
# Traceback (most recent call last):
#  File "C:\Users\mlath\examples\main.py", line 5, in <module>
#   print ("numbers dictionary before delete operation: \n", numbers)
#                                                            ^^^^^^^
# NameError: name 'numbers' is not defined

#using pop method:
#The pop() method returns the value of the specified key after removing the key-value pair.
#syntax: val = dict.pop(key)

# Using popitem() Method
# The popitem() method in dict() class doesn't take any argument. 
# It pops out the last inserted key-value pair, and returns the same as a tuple
# Syntax: val = dict.popitem()