n = int(input())
for i in range(n):
    x,y = map(int,input().split(" "))
    mcd = 1
    if x<y:
        t = int(x/2)
    elif x%y==0:
        t = x
    else:
        t = int(y/2)
    for j in range(2,t+1,1):
        if x%j==0 and y%j==0:
            mcd = j
        else:
            pass
    print(mcd)