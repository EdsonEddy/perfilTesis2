n=input()
m=input()
x=len(m)
y=m.find(n)
y=y+1
c=0
while (y!=0):
    m=m[y:x]
    c=c+1
    y=m.find(n)
    y=y+1
print(c)