# Using the "|" Operator
# The "|" symbol (pipe) is defined as the union operator. It performs the A∪B operation and returns a set of items in A,
# B or both. Set doesn't allow duplicate items.

s1={1,2,3,4,5}
s2={4,5,6,7,8}
s3 = s1|s2
print (s3)
# Output:
# {1, 2, 3, 4, 5, 6, 7, 8}

# Using the union() Method
# The set class has union() method that performs the same operation as | operator.
#  It returns a set object that holds all items in both sets, discarding duplicates.
s1={1,2,3,4,5}
s2={4,5,6,7,8}
s3 = s1.union(s2)
print (s3)


# Using the update() Method
# The update() method also joins the two sets, as the union() method. However it doen't return a new set object.
# Instead, the elements of second set are added in first, duplicates not allowed.
s1={1,2,3,4,5}
s2={4,5,6,7,8}
s1.update(s2)
print (s1)
# Output:
# {1, 2, 3, 4, 5, 6, 7, 8}


# Using the unpacking Operator
# In Python, the "*" symbol is used as unpacking operator. 
# The unpacking operator internally assign each element in a collection to a separate variable.
s1={1,2,3,4,5}
s2={4,5,6,7,8}
s3 = {*s1, *s2}
print (s3)
# Output:
# {1, 2, 3, 4, 5, 6, 7, 8}
