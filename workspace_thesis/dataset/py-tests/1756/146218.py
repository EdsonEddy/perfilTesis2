val=int(input())
while val>0:
    k=int(input())
    h=1
    k=k%6
    for i in range(k+1):
        h=h*2
        if h>=10:
            h=h%10+h//10
    print(h)
    val-=1
        