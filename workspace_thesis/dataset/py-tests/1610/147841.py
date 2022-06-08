n=''
n=input()
ta=len(n)
v=[0]*ta
v=n
s=0
y=[]
c=0
for i in range(len(v)):
    s = s+1
    if int(v[i])== 0:
        s=s-1
        y.append(s)
        c=1
        s = 0
    else:
        c=0
if c==0:
    y.append(str(s))
for i in range(len(y)):
    print(y[i],end="")