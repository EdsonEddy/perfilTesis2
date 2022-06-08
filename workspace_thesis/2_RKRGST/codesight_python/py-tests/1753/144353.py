s=tuple(input().split())
c=0
for j in s:
    a=j.lower()
    d=a[::-1]
    if d==a:
        c+=1
print(c)