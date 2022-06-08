from statistics import mode
y=int(input())
x =input().split()
w=mode(x)
z=0
for i in range(y):
    if w!=x[i]:
        z+=1
print(z)