#igualar el array
numero=int(input(""))#numero de elementos de array
win=list(map(int,input().split()))#Lista de numeroa
h=0
k=[]
p=[]

for f in win:
    if f not in k:
        k.append(f)
        p.append(win.count(f))
g=p.index(max(p))
for f in range(len(p)):
    if f!=g:
        h=h+p[f]
print(h)