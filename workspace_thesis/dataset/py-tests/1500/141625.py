n=int (input())
v=list(map(int,input().split())) #coloco en una lista los datos 1 2 3 21 45
aux=[v[i] for i in range (len(v))]

## for i in range (len(v)):
#       aux.append(v[i])

aux.reverse()

if(aux==v):
    print("SI")
else:
    print("NO")
    