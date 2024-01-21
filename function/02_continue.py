# The continue statement is just the opposite to that of break. It skips the remaining statements in the current loop
# and starts the next iteration.

for letter in 'Python': # First Example
   if letter == 'h':
      continue
   print ('Current Letter :', letter)
var = 10 # Second Example
while var > 0:
   var = var -1
   if var == 5:
      continue
   print ('Current variable value :', var)
print ("Good bye!")