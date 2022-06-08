def ordenAsen(v,n):
    for i in range(0,n-1):
        for j in range(i+1,n):
            if(int(v[i])>int(v[j])):
                aux=v[i]
                v[i]=v[j]
                v[j]=aux
    return
def ordenDesen(v,n):
    for i in range(0,n-1):
        for j in range(i+1,n):
            if(int(v[i])<int(v[j])):
                aux=v[i]
                v[i]=v[j]
                v[j]=aux
    return
while True:
    n=int(input())
    v1=input().split()
    v2=input().split()
    s=0
    
    ordenAsen(v1,n)
    ordenDesen(v2,n)
    for i in range(n):
        p=int(v1[i])*int(v2[i])
        s=s+p
    print(s)