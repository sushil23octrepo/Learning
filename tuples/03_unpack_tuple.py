tup1 = (10,20,30)
x, y, z = tup1
print ("x: ", x, "y: ", "z: ",z)

#example 2
# If the number of variables is more or less than the length of tuple, Python raises a ValueError.
tup1 = (10,20,30)
x, y = tup1
x, y, p, q = tup1
# Output
# ValueError: not enough values to unpack (expected 4, got 3)

#for above case we can use *sybmol to unpack the rest.
tup1 = (10,20,30)
x, *y = tup1
print ("x: ",x ,"y: ", y)
# It will produce the following output −
# x: 10 y: [20, 30]

#example 3
tup1 = (10,20,30, 40, 50, 60)
x, *y, z = tup1
print ("x: ",x, "y: ", y, "z: ", z)
# Output
# x: 10 y: [20, 30, 40, 50] z: 60

#Example 4
tup1 = (10,20,30, 40, 50, 60)
*x, y, z = tup1
print ("x: ",x, "y: ", y, "z: ", z)
# Output
# x: [10, 20, 30, 40] y: 50 z: 60



