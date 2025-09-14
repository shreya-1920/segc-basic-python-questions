#compound and simple interest of  a number
P=float(input("enter p"))
R=float(input("enter r"))
T=float(input("enter t"))
SI=(P*R*T)/100
CI=P*((1+R/100)**T)-P

print(SI)
print(CI)