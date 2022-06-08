s=str(input())
r=""
c=0
for a in s:
    if c>0 and c%7==0:
        r+=a
    if a=="u" and c%2==0:
        r+=a
    c+=1
print(r)