a=int(input())
b=int(input())
c=0
l=0
while a>0:
    x=a%10
    a=a//10
    if x%2==0:
        l=l+x*10**c
        c=c+1
print(l)
l=0
c=0
while b>0:
    x=b%10
    b=b//10
    if x%2==0:
        l=l+x*10**c
print(l)