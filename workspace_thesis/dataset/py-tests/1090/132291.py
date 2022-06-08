n=int(input())
s=0
for i in range (1,n+1):
    t=n-i
    if(t%3==0):
        s=s+t
print(s)
