# You can use the variables in formal argument list as keywords to pass value. Use of keyword arguments is optional. 
# But, you can force the function be given arguments by keyword only. 
# You should put an astreisk (*) before the keyword-only arguments list.

def intr(amt,*, rate):
   val = amt*rate/100
   return val

interest = intr(1000, rate=10)

# interest = intr(1000, 10) This will be error