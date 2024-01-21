lang1 = {"C", "C++", "Java", "Python"}
print ("Set before removing: ", lang1)
lang1.remove("Java")
print ("Set after removing: ", lang1)
lang1.remove("PHP")
# Output:
# Set before removing: {'C', 'C++', 'Python', 'Java'}
# Set after removing: {'C', 'C++', 'Python'}
# lang1.remove("PHP")
# KeyError: 'PHP'

# discard() Method:
# The discard() method in set class is similar to remove() method.
#  The only difference is, it doesn't raise error even if the object to be removed is not already present in the set collection.
lang1 = {"C", "C++", "Java", "Python"}
print ("Set before discarding C++: ", lang1)
lang1.discard("C++")
print ("Set after discarding C++: ", lang1)
print ("Set before discarding PHP: ", lang1)
lang1.discard("PHP")
print ("Set after discarding PHP: ", lang1)
# Output:
# Set before discarding C++: {'Java', 'C++', 'Python', 'C'}
# Set after discarding C++: {'Java', 'Python', 'C'}
# Set before discarding PHP: {'Java', 'Python', 'C'}
# Set after discarding PHP: {'Java', 'Python', 'C'}

#The pop() method in set class removes an arbitrary item from the set collection. 
# The removed item is returned by the method. Popping from an empty set results in KeyError.
# The pop() method returns the object removed from set.
lang1 = {"C", "C++"}
print ("Set before popping: ", lang1)
obj = lang1.pop()
print ("object popped: ", obj)
print ("Set after popping: ", lang1)
obj = lang1.pop()
obj = lang1.pop()
# Output:
# Set before popping: {'C++', 'C'}
# object popped: C++
# Set after popping: {'C'}
# Traceback (most recent call last):
# obj = lang1.pop()
#          ^^^^^^^^^^^
# KeyError: 'pop from an empty set'


# difference_update() Method:
# The difference_update() method in set class updates the set by removing items that are common between itself 
# and another set given as argument.
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
print ("s1 before running difference_update: ", s1)
s1.difference_update(s2)
print ("s1 after running difference_update: ", s1)
# Output:
# s1 before running difference_update: {1, 2, 3, 4, 5}
# s1 after running difference_update: {1, 2, 3}

# intersection_update:
# The intersection_update() method removes uncommon items and keeps only those items which are common to itself and obj.
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
print ("s1: ", s1, "s2: ", s2)
s1.intersection_update(s2)
print ("a1 after intersection: ", s1)
# Output:
# s1: {1, 2, 3, 4, 5} s2: {4, 5, 6, 7, 8}
# s1 after intersection: {4, 5}

# symmetric_difference_update() method:
# The symmetric difference between two sets is the collection of all the uncommon items,
# rejecting the common elements. The symmetric_difference_update() method updates a set with symmetric difference between 
# itself and the set given as argument.

s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
print ("s1: ", s1, "s2: ", s2)
s1.symmetric_difference_update(s2)
print ("s1 after running symmetric difference ", s1)
# Output:
# s1: {1, 2, 3, 4, 5} s2: {4, 5, 6, 7, 8}
# s1 after running symmetric difference {1, 2, 3, 6, 7, 8}
