from statistics import mode
q=int(input())
w=input().split()
l=mode(w)
v=0
for b in range(q):
    if l!=w[b]:
        v+=1
print(v)