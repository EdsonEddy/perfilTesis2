a,b,c,d=map(int,input().split())

for i in range(a-1):
    c,d=d,c+d
print(c%b)