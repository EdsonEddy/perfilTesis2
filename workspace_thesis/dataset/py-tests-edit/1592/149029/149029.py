from statistics import mode
a=int(input())
b =input().split()
s=mode(b)
t=0
for i in range(a):
    if s!=b[i]:
        t+=1
print(t)
