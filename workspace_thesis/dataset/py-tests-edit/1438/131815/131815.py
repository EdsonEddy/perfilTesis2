import math
n,a,b = map(int, input().split(" "))
cd = int(math.log10(n)) + 1
r = n
x = 0
y = 0
nuevo = 0
while(r != 0):
    if(cd == b):
        y = (r % 10)
    elif(cd == a):
        x = (r % 10)
    nuevo = nuevo*10 + (r%10)
    r//=10
    cd-=1
if(x == 0):
    x=y
if(y == 0):
    y=x 
cd = 1
while(nuevo != 0):
    if(cd == b):
        r = r*10 + (x)
    elif(cd == a):
        r = r*10 + (y)
    else:
        r = r*10 + (nuevo % 10)
    nuevo//=10
    cd+=1
print(r)