a=input().split()
b=""
x=0
y=0
for c in a:
    if c in b:
        continue
    else:
        b=b+c
for c in b:
    d=a.count(c)
    print (c,d)