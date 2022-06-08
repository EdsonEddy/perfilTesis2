a,b = map(int,input().split())
p = 0
div = 0
for i in range (a+1,b):
    div = 0
    for j in range (1,i+1):
        d = 0
        d = int(i%j)
        if d == 0:
            div = div + 1
    if div == 2:
        p=p+1
if a == b:
    for j in range (1,b+1):
        d = 0
        d = int(b%j)
        if d == 0:
            div = div + 1
    if div == 2:
        p=p+1
    
print (p)
