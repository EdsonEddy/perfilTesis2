x,y = map(int, input().split())
if y>x:
    aux = x
    x = y
    y = aux
for i in range (x,y-1,-1):
    print(i)
