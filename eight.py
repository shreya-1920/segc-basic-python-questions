#armstrong num or not
num=int(input("enter n"))
sum=0
temp=num

n=len(str(num))
while temp>0:
    digit=temp%10
    sum+=digit**n
    temp//=10

if num==sum:
    print("yes")
else:
    print("no")   