while True:
    try:
        n=int(input())
        while n > 0:
            n=n-1
            x=int(input())
            if x <=17 and x >=0:
                if x==0:
                    print(1)
                elif x==1:
                    print(0)
                else:
                    if x%2==0:
                        m=x//2
                        c=0
                        while m+1> 0:
                            c=int(8*10**(m-1)+c)
                            m=m-1
                        print (c)
                    else:
                        m = x // 2
                        c = 0
                        d = 4 * 10**m
                        while m + 1 > 0:
                            c = int(8 * 10 ** (m - 1) + c)
                            m = m - 1
                        u=d+c
                        print(u)
        break
    except ValueError:
        break