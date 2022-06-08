from statistics import mode
n=int(input())
x =input().split()
m=mode(x)
c=0
for i in range(n):
    if m!=x[i]:
        c+=1
print(c)