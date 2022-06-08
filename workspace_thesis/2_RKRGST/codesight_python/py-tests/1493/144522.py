c=str(input().lower())
n=len(c)
s=str(input().lower())
a=0
g=0
while g!=-1:
    g=c.find(s,a,n)
    if g==-1:
        break
    print(g)
    a=g+1