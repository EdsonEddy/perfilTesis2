from statistics import mode
a=int(input())
b=input().split()
c=mode(b)
d=0
for i in range(a):
    if c!=b[i]:
        d+=1
print(d)