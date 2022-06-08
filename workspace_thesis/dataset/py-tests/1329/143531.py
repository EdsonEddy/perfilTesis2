n,i,j = map(int,input().split(" "))
cad = input()
v = cad.split(" ")
v = list(map(int, v))
aux = []
for x in range(i, j+1):
    aux.append(v[x])
aux.sort()
cd = 0
for x in range(n):
    if(x >= i and x <= j):
        print(aux[cd], end = "")
        cd+=1
    else:
        print(v[x], end = "")
    if(x != n-1):
        print(" ",end = "")
print("")