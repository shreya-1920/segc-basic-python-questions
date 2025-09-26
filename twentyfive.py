#sum using array and function
def find_largest(arr):
    largest=arr[0]
    for num in arr:
        if num>largest:
            largest=num
            return largest
      
    
arr=[25,11,7,75,56]
result=find_largest(arr)
print(result)
