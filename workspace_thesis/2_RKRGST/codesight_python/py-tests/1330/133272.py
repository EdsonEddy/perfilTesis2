a,b=map(str,input().split())
b=int(b)
x=0
y=""
z=a[::-1]
g=z[:b]
h=g[::-1]
for c in a:
    x=x+1
if x>b:
    b=b
else:
    b=b%x
f=x-b
e=a[:f]
if(b==0):
    print(a)
else:
    if(x==1):
         print(h)
    else:
         print(h+e)