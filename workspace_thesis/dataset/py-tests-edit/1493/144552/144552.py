n=str(input())
n=n.lower()
a=str(input())
a=a.lower()
f=0
while f>=0:
    f=n.find(a,f)

    if f==-1:
        break
    print(f)
    f=f+1