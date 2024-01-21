# The list class methods remove() and pop() both can remove an item from a list. 
# The difference between them is that remove() removes the object given as argument,
#  while pop() removes an item at the given index.

list1 = ["Rohan", "Physics", 21, 69.75]
print ("Original list: ", list1)

list1.remove("Physics")
print ("List after removing: ", list1)
#Output:
# Original list: ['Rohan', 'Physics', 21, 69.75]
# List after removing: ['Rohan', 21, 69.75]

list2 = [25.50, True, -55, 1+2j]
print ("Original list: ", list2)
list2.pop(2)
print ("List after popping: ", list2)
# Output
# Original list: [25.5, True, -55, (1+2j)]
# List after popping: [25.5, True, (1+2j)]

list3 = ["a", "b", "c", "d"]
print ("Original list: ", list3)
del list3[2]
print ("List after deleting: ", list3)
# Output:
# Original list: ['a', 'b', 'c', 'd']
# List after deleting: ['a', 'b', 'd']

# You can delete a series of consecutive items from a list with the slicing operator.
#  Take a look at the following example −
list4 = [25.50, True, -55, 1+2j]
print ("List before deleting: ", list4)
del list4[0:2]
print ("List after deleting: ", list4)

# Output:
# List before deleting: [25.5, True, -55, (1+2j)]
# List after deleting: [-55, (1+2j)]
