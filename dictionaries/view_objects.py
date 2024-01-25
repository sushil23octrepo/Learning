# items() Method
# The items() method returns a dict_items view object. It contains a list of tuples, each tuple made up of respective key, 
# value pairs.
numbers = {10:"Ten", 20:"Twenty", 30:"Thirty",40:"Forty"}
obj = numbers.items()
print ('type of obj: ', type(obj))
print (obj)
print ("update numbers dictionary")
numbers.update({50:"Fifty"})
print ("View automatically updated")
print (obj)

# Output:
# type of obj: <class 'dict_items'>
# dict_items([(10, 'Ten'), (20, 'Twenty'), (30, 'Thirty'), (40, 'Forty')])
# update numbers dictionary
# View automatically updated
# dict_items([(10, 'Ten'), (20, 'Twenty'), (30, 'Thirty'), (40, 'Forty'), (50, 'Fifty')])


numbers = {10:"Ten", 20:"Twenty", 30:"Thirty",40:"Forty"}
obj = numbers.keys()
print ('type of obj: ', type(obj))
print (obj)
print ("update numbers dictionary")
numbers.update({50:"Fifty"})
print ("View automatically updated")
print (obj)
# Output:
# type of obj: <class 'dict_keys'>
# dict_keys([10, 20, 30, 40])
# update numbers dictionary
# View automatically updated
# dict_keys([10, 20, 30, 40, 50])

# values() Method
# The values() method returns a view of all the values present in the dictionary. 
# The object is of dict_value type, which gets automatically updated.
numbers = {10:"Ten", 20:"Twenty", 30:"Thirty",40:"Forty"}
obj = numbers.values()
print ('type of obj: ', type(obj))
print (obj)
print ("update numbers dictionary")
numbers.update({50:"Fifty"})
print ("View automatically updated")
print (obj)
# Output:
# type of obj: <class 'dict_values'>
# dict_values(['Ten', 'Twenty', 'Thirty', 'Forty'])
# update numbers dictionary
# View automatically updated
# dict_values(['Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty'])