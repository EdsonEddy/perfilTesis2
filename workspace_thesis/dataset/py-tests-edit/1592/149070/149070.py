from statistics import mode
m=int(input())
a =input().split()
b=mode(a)
w=0
for i in range(m):
    if b!=a[i]:
        w+=1
print(w)