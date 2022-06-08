for casos in range(int(input())) :
    n=int(input())
    x,y=map(int,input().split())
    print(str(x),end='')
    for i in range(n-1):
        x,y=y,x+y
        print('+'+str(x),end='')
    print()
