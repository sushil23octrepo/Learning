# The append() method adds the item at the end of an existing list.
list1 = ["a", "b", "c", "d"]
print ("Original list: ", list1)
list1.append('e')
print ("List after appending: ", list1)
# Output:
# Original list: ['a', 'b', 'c', 'd']
# List after appending: ['a', 'b', 'c', 'd', 'e']

# The insert() method inserts the item at a specified index in the list.
list1 = ["Rohan", "Physics", 21, 69.75]
print ("Original list ", list1)
list1.insert(2, 'Chemistry')
print ("List after appending: ", list1)
list1.insert(-1, 'Pass')
print ("List after appending: ", list1)