# Since set is not a sequence data type, its items cannot be accessed individually 
# as they do not have a positional index (as in list or tuple). Set items do not have a key either (as in dictionary) to access.
# You can only traverse the set items using a for loop.

langs = {"C", "C++", "Java", "Python"}
for lang in langs:
   print (lang)


langs = {"C", "C++", "Java", "Python"}
print ("PHP" in langs)
print ("Java" in langs)
# Output:
# False
# True

