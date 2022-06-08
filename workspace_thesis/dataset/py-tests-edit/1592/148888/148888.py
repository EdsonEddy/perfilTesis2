from statistics import mode
n=int(input())
x =input().split()
m=mode(x)
p=0
for i in range(n):
    if m!=x[i]:
        p+=1
print(p)
