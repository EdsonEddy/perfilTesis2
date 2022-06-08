from statistics import mode
a=int(input())
b=input().split()
c=mode(b)
x=0
for i in range(a):
    if c!=b[i]:
        x=x+1
print(x)