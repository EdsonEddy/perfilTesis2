from statistics import mode
A1=int(input())
B1=input().split()
j=mode(B1)
P=0
for i in range(A1):
    if j!=B1[i]:
        P+=1
print(P)