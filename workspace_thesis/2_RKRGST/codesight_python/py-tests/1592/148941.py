from statistics import mode
b=int(input())
a=input().split()
m=mode(a)
c=0
for i in range(b):
    if m!=a[i]:
        c+=1
print(c)