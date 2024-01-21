# In Python, a string is an ordered sequence of Unicode characters.
# Each character in the string has a unique index in the sequence. 
# The index starts with 0. First character in the string has its positional index 0. 
# The index keeps incrementing towards the end of string

# >>> var="HELLO PYTHON"
# >>> var[0]
# 'H'
# >>> var[7]
# 'Y'
# >>> var[11]
# 'N'
# >>> var[12]
# Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
# IndexError: string index out of range



# One of the unique features of Python sequence types (and therefore a string object) it has a negative indexing scheme also. 
# In the example above, a positive indexing scheme is used where the index increments from left to right. 
# In case of negative indexing, the character at the end has -1 index and the index decrements from right to left, 
# as a result the first character H has -12 index.

# >>> var[-1]
# 'N'
# >>> var[-5]
# 'Y'
# >>> var[-12]
# 'H'
# >>> var[-13]
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# IndexError: string index out of range



# In Python, string is an immutable object. The object is immutable if it cannot be modified in-place, 
# once stored in a certain memory location. You can retrieve any character from the string with the help of its index,
#  but you cannot replace it with another character. 

var="HELLO PYTHON"
var[7]="y"
print (var)

# It will produce the following output −
# TypeError: 'str' object does not support item assignment


# Python defines ":" as string slicing operator. It returns a substring from the original string. Its general usage is −
# substr=var[x:y]

var="HELLO PYTHON"

print ("var:",var)
print ("var[3:8]:", var[3:8])

# It will produce the following output −
# var: HELLO PYTHON
# var[3:8]: LO PY


#Another example:
var="HELLO PYTHON"
print ("var:",var)
print ("var[3:8]:", var[3:8])
print ("var[-9:-4]:", var[-9:-4])

# It will produce the following output −
# var: HELLO PYTHON
# var[3:8]: LO PY
# var[-9:-4]: LO PY


# Both the operands for Python's Slice operator are optional. The first operand defaults to zero, 
# which means if we do not give the first operand, the slice starts of character at 0th index, i.e.
# the first character. It slices the leftmost substring up to "y-1" characters.
var="HELLO PYTHON"
print ("var:",var)
print ("var[0:5]:", var[0:5])
print ("var[:5]:", var[:5])

# It will produce the following output −
# var: HELLO PYTHON
# var[0:5]: HELLO
# var[:5]: HELLO

# Similarly, y operand is also optional. By default, it is "-1", 
# which means the string will be sliced from the xth position up to the end of string.
var="HELLO PYTHON"
print ("var:",var)
print ("var[6:12]:", var[6:12])
print ("var[6:]:", var[6:])

# Output:
# var: HELLO PYTHON
# var[6:12]: PYTHON
# var[6:]: PYTHON

# Naturally, if both the operands are not used, the slice will be equal to the original string.
#  That's because "x" is 0, and "y" is the last index+1 (or -1) by default.
var="HELLO PYTHON"
print ("var:",var)
print ("var[0:12]:", var[0:12])
print ("var[:]:", var[:])

# It will produce the following output −
# var: HELLO PYTHON
# var[0:12]: HELLO PYTHON
# var[:]: HELLO PYTHON

