n=int(input())
vec=input().split()
if n%2==0:
    m=(n/2)-1
else:
    m = (n // 2)
s1,s2=0,0
for i in range(m+1):
    s1+=int(vec[i])
for i in range(m+1,n,1):
    s2+=int(vec[i])
print(abs(s2-s1))