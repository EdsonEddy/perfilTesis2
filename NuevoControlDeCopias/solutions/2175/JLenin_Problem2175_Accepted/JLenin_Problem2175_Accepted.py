for _ in range(int(input())):
    n=int(input())
    i,x,y=1,0,1
    if n==0:print(0);continue
    while True:
        x,y=y,x+y
        if x==n:print(i);break
        i+=1
