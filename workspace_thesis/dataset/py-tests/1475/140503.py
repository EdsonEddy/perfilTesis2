n,i,j=map(int, input().split())
cad=input()
v=cad.split(" ")
aux=[ ]
for x in range(i, j+1):
    aux.append(v[x])
aux.reverse()
cd=0
for k in range(n):
    if k>=i and k<=j:
        print(aux[cd])
        cd+=1
    else:
        print(v[k])
