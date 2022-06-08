n=int(input())
v=input().split()

a=n//2+1
s=0;c=0
for i in range(0,a):
    s=s+int(v[i])
for j in range(n-1,a-1,-1):
    c=c+int(v[j])
a=max(s,c)-min(s,c)
print(a)