n,k=map(int,input().split())
o=n
d=0
i=0
j=0
while n>0:
    d=n%10
    n=n//10
    i=i+1
d=0
for j in range(i+1-k):
    d=o%10
    o=o//10
print(i,d)
