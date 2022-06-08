casos = int(input())
for x in range(casos):
    n=int(input())
    if n==1:
        print("Feliz")
    else:
        while n >1:
            s=0
            while n > 0:
                d = n%10
                s=s+d*d
                n=n//10
            if s==1:
                print("Feliz")
            elif s!=1 and len(str(s))==1:
                print("Triste")
                break
            n=s