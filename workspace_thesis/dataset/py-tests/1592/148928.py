from statistics import mode
y=int(input())
x =input().split()
m=mode(x)
a=0
for i in range(y):
    if m!=x[i]:
        a+=1
print(a)