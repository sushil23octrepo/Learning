def add(x,y):
   z=x+y
   print ("x={} y={} x+y={}".format(x,y,z))

add(10,15)

#position only arguments
# It is possible to define a function in which one or more arguments can not accept their value with keywords.
# Such arguments may be called positional-only arguments.

# We make both the arguments of intr() function as positional-only by putting "/" at the end.
def intr(amt, rate, /):
   val = amt*rate/100
   return val

# If we try to use the arguments as keywords, Python raises following error message −
# TypeError: intr() got some positional-only arguments passed as keyword arguments: 'amt, rate'

interest = intr(amt=1000, rate=10)


# In this function, x is a required positional-only argument, y is a regular positional argument (you can use it as keyword 
# if you want), and z is a keyword-only argument.
def myfunction(x, /, y, *, z):
   print (x, y, z)

# The following function calls are valid −
# myfunction(10, y=20, z=30)
# myfunction(10, 20, z=30)

# # However, these calls raise errors −
# myfunction(x=10, y=20, z=30)
# TypeError: myfunction() got some positional-only arguments passed as keyword arguments: 'x'

# myfunction(10, 20, 30)
# TypeError: myfunction() takes 2 positional arguments but 3 were given


