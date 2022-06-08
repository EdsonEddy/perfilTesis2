import sys
for x in sys.stdin:
    n = int(x)
    f = 1
    for i in range(n):
        if(i%2==0):
            print(-f)
        else:
            print(f)
        f=f*(i+2) 
