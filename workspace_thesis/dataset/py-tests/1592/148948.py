from statistics import mode
n=int(input())
a =input().split()
m=mode(a)
c=0
for i in range(n):
    if m!=a[i]:
        c+=1
print(c)