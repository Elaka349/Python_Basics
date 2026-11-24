arr=[10,5,2,8,2]
smallest=float('inf')
largest=float('inf')
for num in arr:
    if num < smallest:
        second=smallest
        smallest=num
    elif num<smallest and num!=smallest:
        second=num
print("second smallest=",second)    
