n=1
c=0
cc=0
temp=0
while n!=0:
    t=float(input())
    if(t==0):
        break
    if(t<0):
        c=c+1
    if t>temp:
        temp=t
    cc=cc+1
td=c/cc
td=int(td*100)
temp=int(temp)
print(td)
print(temp)