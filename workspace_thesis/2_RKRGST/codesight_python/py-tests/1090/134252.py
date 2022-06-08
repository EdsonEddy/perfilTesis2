n=int(input())
s = 0
for i in range (1,n):
    d=i%3
    if (d==0):
        s=s+i

print(s)