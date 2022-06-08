elem=int(input())
lista=list(input().split(" "))
final=[]
for i in range(elem-1,-1,-1):
    final.append(lista[i])
if final == lista:
    print("SI")
else:
    print("NO")