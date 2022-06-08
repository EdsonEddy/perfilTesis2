n=int(input())
for i in range(n):
    x=int(input())
    y=1
    s=0
    if 1<=x<=10**14:
        c=1
        while x>3 :
            s=0
            while x>0 :
                a = x % 10
                x =x//10
                s=s+a**2
            x=s
            c=c+1
            if c>100:
                x=0

        if x==1:
            print("Feliz")
        else:
            print("Triste")
