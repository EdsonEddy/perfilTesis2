a,b,c,d=map(int,input().split())
x=0
for e in range(1, a -1):
    x = x + 1
    x = c + d
    c = d
    d = x
y=x%b
print(y)