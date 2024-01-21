# Suppose we want to separate each letter in a string and put all non-vowel letters in a list object. 
# We can do it by a for loop as shown below −
chars=[]
for ch in 'TutorialsPoint':
   if ch not in 'aeiou':
      chars.append(ch)
print (chars)
# Output:
# ['T', 't', 'r', 'l', 's', 'P', 'n', 't']


# We can easily get the same result by a list comprehension technique
chars = [char for char in 'TutorialsPoint' if char not in 'aeiou']
print (chars)
# Output:
# ['T', 't', 'r', 'l', 's', 'P', 'n', 't']

#Another Example
squares = [x*x for x in range(1,11)]
print (squares)
# Output:
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


# Nested Loops in List Comprehension
# In the following example, all combinations of items from two lists in the form of a tuple are added in a third list object.
list1=[1,2,3]
list2=[4,5,6]
CombLst=[(x,y) for x in list1 for y in list2]
print (CombLst)
# Output:
[(1, 4), (1, 5), (1, 6), (2, 4), (2, 5), (2, 6), (3, 4), (3, 5), (3, 6)]


# Condition in List Comprehension
list1=[x for x in range(1,21) if x%2==0]
print (list1)
# Output:
# [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

