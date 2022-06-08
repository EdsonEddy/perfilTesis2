n=int(input())
s=0
x=n
while(n>0):
    d=n%10
    s=s*10+d
    n=n//10
if(x==s):
    print ("S")
else:
    print ("N")