n=int(input())
a=""
while n!=0:
    a=a+" "+input()
    n-=1
c=a.split()
ne=len(c)
for x in range(0, ne):
    print(c[x])