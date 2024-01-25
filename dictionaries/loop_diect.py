numbers = {10:"Ten", 20:"Twenty", 30:"Thirty",40:"Forty"}
for x in numbers:
   print (x)
# Output:
# 10
# 20
# 30
# 40
   
numbers = {10:"Ten", 20:"Twenty", 30:"Thirty",40:"Forty"}
for x in numbers:
   print (x,":",numbers[x])
# Output:
# 10 : Ten
# 20 : Twenty
# 30 : Thirty
# 40 : Forty

numbers = {10:"Ten", 20:"Twenty", 30:"Thirty",40:"Forty"}
for x in numbers.items():
   print (x)
# Output:
# (10, 'Ten')
# (20, 'Twenty')
# (30, 'Thirty')
# (40, 'Forty')


numbers = {10:"Ten", 20:"Twenty", 30:"Thirty",40:"Forty"}
for x,y in numbers.items():
   print (x,":", y)
# Output:
# 10 : Ten
# 20 : Twenty
# 30 : Thirty
# 40 : Forty
   
numbers = {10:"Ten", 20:"Twenty", 30:"Thirty",40:"Forty"}
for x in numbers.keys():
   print (x, ":", numbers[x])
# Output:
# 10 : Ten
# 20 : Twenty
# 30 : Thirty
# 40 : Forty
   
numbers = {10:"Ten", 20:"Twenty", 30:"Thirty",40:"Forty"}
l = len(numbers)
for x in range(l):
   print (list(numbers.keys())[x], ":", list(numbers.values())[x])
# Output:
# 10 : Ten
# 20 : Twenty
# 30 : Thirty
# 40 : Forty