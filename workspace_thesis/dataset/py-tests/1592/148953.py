from statistics import mode
l=int(input())
p =input().split()
k=mode(p)
c=0
for i in range(l):
    if k!=p[i]:
        c+=1
print(c)