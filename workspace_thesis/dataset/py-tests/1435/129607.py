a,b=map(int,input().split())
n=a
s=0
while a>0:
    d=a%10
    s=s+1
    a=a//10

k=n//(10**(s-b))
l=k%10
print(s,l)