salary=int(input("enter the salary:"))
if salary>=30000:
    bonus=salary*0.10
else:
    bonus=salary*0.15
total=salary+bonus    
print("bonus=",bonus)
print("total=",total)

        