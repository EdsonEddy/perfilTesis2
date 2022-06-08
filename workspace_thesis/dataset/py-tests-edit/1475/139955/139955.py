s = input()
l = s.split(" ")
N = int(l[0])
i = int(l[1])
j= int(l[2])
cad = input()
f = cad.split(" ")
g = []
for x in range(i,j+1):
    g.append(f[x])
g.reverse()
cd=0
for k in range(N):
    if k>=i and k<=j:
        print(g[cd])
        cd+=1
    else:
        print(f[k])