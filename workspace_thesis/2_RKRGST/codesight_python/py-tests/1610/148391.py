n=''
n=input()
m=len(n)
l=[0]*m
l=n
s=0
k=[]
c=0
for i in range(len(l)):
    s = s+1
    if int(l[i])== 0:
        s=s-1
        k.append(s)
        c=1
        s = 0
    else:
        c=0
if c==0:
    k.append(str(s))
for i in range(len(k)):
    print(k[i],end="")