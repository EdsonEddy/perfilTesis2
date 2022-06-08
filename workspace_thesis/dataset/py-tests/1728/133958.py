n=int(input())
r=n
s=0
while n!=0:
    r=r%10
    n=n/10
    if r%2==0:
        s=r+s
    r=n
print(8)

m=int(input())
y=m
d=0
while m!=0:
    y=y%10
    m=m/10
    if y%2==0:
        d=y+d
    y=m
print(2)