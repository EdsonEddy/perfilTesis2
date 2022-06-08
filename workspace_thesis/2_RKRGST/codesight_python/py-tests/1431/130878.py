n,m,a,b=map(int,input().split())
for i in range(n-2):
    a, b = b, a + b
print(b%m)