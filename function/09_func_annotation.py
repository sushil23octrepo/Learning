def myfunction(a: int, b: int):
   c = a+b
   return c

def myfunction1(a: int, b: int) -> int:
   c = a+b
   return c


def myfunction3(a: "physics", b:"Maths" = 20) -> int:
   c = a+b
   return c

print (myfunction3(10))