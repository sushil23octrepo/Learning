tup1 = ("Rohan", "Physics", 21, 69.75)
tup2 = (1, 2, 3, 4, 5)

# Output:
# Item at 0th index in tup1: Rohan
# Item at index 2 in tup2: 3


tup1 = ("a", "b", "c", "d")
tup2 = (25.50, True, -55, 1+2j)
tup4 = ("Rohan", "Physics", 21, 69.75)
tup3 = (1, 2, 3, 4, 5)

print ("Items from index 1 to last in tup1: ", tup1[1:])
print ("Items from index 0 to 1 in tup2: ", tup2[:2])
print ("Items from index 2 to last in tup3", tup3[2:-1])
print ("Items from index 0 to index last in tup4", tup4[:])

#Output:
# Items from index 1 to last in tup1: ('b', 'c', 'd')
# Items from index 0 to 1 in tup2: (25.5, True)
# Items from index 2 to last in tup3: (3, 4)
# Items from index 0 to index last in tup4: ('Rohan', 'Physics', 21, 69.75)
