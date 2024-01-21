T1 = (10,20,30,40)
T2 = ('one', 'two', 'three', 'four')
T3 = T1+T2
print ("Joined Tuple:", T3)

# Output:
# Joined Tuple: (10, 20, 30, 40, 'one', 'two', 'three', 'four')

#above result can be obtain from following example:
T1 = (10,20,30,40)
T2 = ('one', 'two', 'three', 'four')
L1 = list(T1)
L2 = list(T2)
L1.extend(L2)
T1 = tuple(L1)
print ("Joined Tuple:", T1)