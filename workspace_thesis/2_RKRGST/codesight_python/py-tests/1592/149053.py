from statistics import mode
a=int(input())
b =input().split()
j=mode(b)
L=0
for i in range(a):
    if j!=b[i]:
        L+=1
print(L)
