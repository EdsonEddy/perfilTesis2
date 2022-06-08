x=str(input())
a=str(input())
y=0
c=0
while y>=0:
         b=a.find(x,y)
         if b<0:
                   break
         c=c+1
         y=b+1
print(c)
