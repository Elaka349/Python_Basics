arr=[70,30,20,60,10]
largest=float('-inf')
smallest=float('-inf')
for num in arr:
    if num > largest:
        second=largest  
        largest=num
    elif num>second and num!=largest:
        second=num
print("second number=",second)                  
