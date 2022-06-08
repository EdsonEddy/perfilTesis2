#Problema A
n=int(input())
#Entrada

for i in range(1,n+1):
    a, b = map(int, input().split())
    if(a>b):
        min=b
    else:
        min=a
    mcd=1
    for i in range (min, 1,-1):
        if(a%i==0 and b%i==0):
            mcd=i
            break
    print (mcd)