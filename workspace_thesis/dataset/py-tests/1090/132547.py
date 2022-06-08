m=int(input())
s=0
n=m
for i in range(m): 
    n=n-1
    if n%3==0:
        s=s+n
print(s)
