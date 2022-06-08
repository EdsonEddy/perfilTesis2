from statistics import mode
y=int(input())
x =input().split()
j=mode(x)
k=0
for i in range(y):
    if j!=x[i]:
        k+=1
print(k)
