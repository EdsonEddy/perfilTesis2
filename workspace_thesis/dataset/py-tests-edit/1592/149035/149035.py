from statistics import mode
a=int(input())
h =input().split()
c=mode(h)
g=0
for i in range(a):
    if c!=h[i]:
        g+=1
print(g)
