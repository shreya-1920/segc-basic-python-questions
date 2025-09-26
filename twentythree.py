#area in perimeter of triangle
import math
def perimeter(a,b,c):
    return a+b+c

def area(a,b,c):
    s=(a+b+c)/2
    return math.sqrt(s*(s-a)*(s-b)*(s-c))
a=float(input("enter a"))
b=float(input("enter b"))
c=float(input("enter c"))
print(perimeter(a,b,c))
print(area(a,b,c))
    
