from statistics import mode
a=int(input())
x =input().split()
b=mode(x)
c=0
for i in range(a):
    if b!=x[i]:
        c+=1
print(c)