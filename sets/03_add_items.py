lang1 = {"C", "C++", "Java", "Python"}
lang1.add("Golang")
print (lang1)
# Output:
# {'Python', 'C', 'Golang', 'C++', 'Java'}

#Example
lang1 = {"C", "C++", "Java", "Python"}
lang2 = {"PHP", "C#", "Perl"}
lang1.update(lang2)
print (lang1)
# Output:
# {'Python', 'Java', 'C', 'C#', 'PHP', 'Perl', 'C++'}

#Example 2
lang1 = {"C", "C++", "Java", "Python"}
lang2 = {"PHP", "C#", "Perl"}
lang3 = lang1.union(lang2)
print (lang3)
# Output:
# {'C#', 'Java', 'Perl', 'C++', 'PHP', 'Python', 'C'}

#Example 3:
# If a sequence object is given as argument to union() method, 
# Python automatically converts it to a set first and then performs union.
lang1 = {"C", "C++", "Java", "Python"}
lang2 = ["PHP", "C#", "Perl"]
lang3 = lang1.union(lang2)
print (lang3)
# Output:
# {'PHP', 'C#', 'Python', 'C', 'Java', 'C++', 'Perl'}
