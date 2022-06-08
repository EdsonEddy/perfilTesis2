
m=str(input())
n=str(input())
e=0
c=0
while e>=0:
         b=n.find(m,e)
         if b<0:
                   break
         c=c+1
         e=b+1
print(c)