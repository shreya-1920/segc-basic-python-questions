#palindrome of a no
#reads backward and forward the same
num=input("enter a no")
if num==num[::-1]:
    print("yes")
else:
    print("no")