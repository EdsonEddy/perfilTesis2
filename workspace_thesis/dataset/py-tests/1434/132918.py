n=int(input())
c=n
x=0
while n>0:
    x=x*10+n%10
    n=n//10
if x==c:
    print("S")
else:
    print("N")
    
