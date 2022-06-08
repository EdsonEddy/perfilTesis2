from collections import Counter
n=int(input())
fil=list(tuple(map(int,input().split())))
c = Counter(fil)
g=max(c, key=c.get)
c=0
for j in fil:
    if g!=j:
        c=c+1
print(c)