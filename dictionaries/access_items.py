# A dictionary in Python is not a sequence, as the elements in dictionary are not indexed. 
# Still, you can use the square brackets "[ ]" operator to fetch the value associated 
# with a certain key in the dictionary object.
# Python raises a KeyError if the key given inside the square brackets is not present in the dictionary object.
capitals = {"Maharashtra":"Mumbai", "Gujarat":"Gandhinagar", "Telangana":"Hyderabad", "Karnataka":"Bengaluru"}
print ("Capital of Gujarat is : ", capitals['Gujarat'])
print ("Capital of Karnataka is : ", capitals['Karnataka'])
print ("Capital of Karnataka is: ", capitals.get('Telangana'))

# The get() method accepts an optional string argument. If it is given, and if the key is not found, 
# this string becomes the return value.
print ("Capital of Haryana is : ", capitals.get('Haryana', 'Not found'))