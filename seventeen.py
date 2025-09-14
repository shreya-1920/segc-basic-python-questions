#find vowels in string
n=input("enter string")
vowels="aeiouAEIOU"
found=[]
for ch in n:
    if ch in vowels:
        found.append(ch)
print(found)        

