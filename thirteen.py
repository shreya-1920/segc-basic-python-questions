#avg of no
n=int(input("enter how many numbers"))
total=0
for i in range(n):
    num=float(input(f"enter number{i+1}:"))
    total+=num

avg=total/n
print("average is:",avg)