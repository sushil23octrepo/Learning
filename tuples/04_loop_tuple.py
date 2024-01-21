tup1 = (25, 12, 10, -21, 10, 100)
for num in tup1:
   print (num, end = ' ')

# Output
# 25 12 10 -21 10 100

#Example 2
tup1 = (25, 12, 10, -21, 10, 100)
indices = range(len(tup1))
for i in indices:
   print ("tup1[{}]: ".format(i), tup1[i])

# Output:
# tup1[0]: 25
# tup1 [1]: 12
# tup1 [2]: 10
# tup1 [3]: -21
# tup1 [4]: 10
# tup1 [5]: 100