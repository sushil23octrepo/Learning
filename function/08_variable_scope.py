marks = 50 # this is a global variable
def myfunction():
   marks = 70 # this is a local variable
   print (marks)
   
myfunction()
print (marks) #print global variable