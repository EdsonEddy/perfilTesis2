n = int(input())
for i in range (0,n,1):
    x, y= map(int, input().split (" "))
    if x>y:
        mi=y
    else:
        mi=x
    for j in range (mi,0,-1):
        if x%j==0 and y%j==0:
            print(j)
            break
