def verificar(x):
    for i in range(len(c)):
        if x==c[i]:
            return False
    return True
def unir(x,y):
    for i in range(x):
        if verificar(a[i]):
            c.append(a[i])
    for i in range(y):
        if verificar(b[i]):
            c.append(b[i])       
    return

n,nn=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=[]
unir(n,nn)
c.sort()
for i in range(len(c)):
    print(c[i])