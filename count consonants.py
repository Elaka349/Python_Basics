s="Python"
count=0
for ch in s:
    if ch not in "aeiouAEIOU" and ch.isalpha() :
        count+=1
print(count)    