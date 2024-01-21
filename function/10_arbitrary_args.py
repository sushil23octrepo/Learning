#The args variable prefixed with "*" stores all the values passed to it. Here, args becomes a tuple.
#We can run a loop over its items to add the numbers.
def add(*args):
   s=0
   for x in args:
      s=s+x
   return s
result = add(10,20,30,40)
print (result)

result = add(1,2,3)
print (result)


#Following call to avg() function passes first value to the required argument first,
#and the remaining values to a tuple named rest
def avg(first, *rest):
   second=max(rest)
   return (first+second)/2
   
result=avg(40,30,50,25)
print (result)


# The following code is an example of a function with arbitrary keyword arguments. 
# The addr() function has an argument **kwargs which is able to accept any number of address elements like name, 
# city, phno, pin, etc. Inside the function kwargs dictionary of kw:value pairs is traversed using items() method.
def addr(**kwargs):
   for k,v in kwargs.items():
      print ("{}:{}".format(k,v))

print ("pass two keyword args")
addr(Name="John", City="Mumbai")
print ("pass four keyword args")

# pass four keyword args
addr(Name="Raam", City="Mumbai", ph_no="9123134567", PIN="400001")

# Output:
# pass two keyword args
# Name:John
# City:Mumbai
# pass four keyword args
# Name:Raam
# City:Mumbai
# ph_no:9123134567
# PIN:400001