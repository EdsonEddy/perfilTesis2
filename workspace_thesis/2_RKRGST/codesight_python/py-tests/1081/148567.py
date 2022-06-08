tam=100000
p=[0]*tam
def criba():
    r=int(tam**0.5)+1
    for i in range(2,r):
        if p[i]==0:
            for j in range(i+i,tam,i):
                p[j]=1
criba()
casos=int(input())
for i in range(casos):
    n=int(input())
    pd=0
    for j in  range(n,tam):
        if p[j]==0:
            pd=j
            break
    pi=0
    for j in range(n,1,-1):
        if p[j]==0:
            pi=j
            break
    if(n-pi)<(pd-n):
        print(n-pi)
    else:
        print(pd-n)
