n = int(input())
v = list(map(int, input().split()))
aux = [v[i] for i in range(len(v))]
##for i in range(len(v)):
##    aux.append(v[i])
aux.reverse()
if(aux == v):
    print("SI")
else:
    print("NO")

