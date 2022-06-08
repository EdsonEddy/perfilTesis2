def pal(x):
    r=""
    for letra in x:
        r=letra+r
    if r==x:
        return 1
    else:
        return 0

x=input()
i=0
s=0
b=x.lower().split()
for i in b:
    s=s+pal(i)
print(s)
    
