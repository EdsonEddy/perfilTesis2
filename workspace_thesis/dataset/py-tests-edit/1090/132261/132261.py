n=int(input())
i=1
s=0
while i<n:
    x=i%3
    if x==0:
        s=s+i
    i=i+1
print(s)