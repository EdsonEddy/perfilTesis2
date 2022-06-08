tam=100000
p=[0]*tam
def criba():
    r=int(tam**(0.5))+1
    for i in range(2,r):
        if p[i]==0:
            for j in range(i+i,tam,i):
                p[j]=1
criba()
casos=int(input())
for i in range(casos):
    n=int(input())
    pd=n
    pi=n
    if p[n]==0:
        print('0')
    else:
        for j in range(1,n):
            pd=n-j
            pi=n+j

            if p[pd]==0 or p[pi]==0:
                print(j)
                break