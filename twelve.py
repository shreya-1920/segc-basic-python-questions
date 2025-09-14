#gcd of a number
a=int(input("enter a"))
b=int(input("enter b"))
gcd=1
for i in range(1,min(a,b)+1):
    if a%i==0 and b%i==0:
        gcd=i
print("gcd of",a,"and",b,"is",gcd)