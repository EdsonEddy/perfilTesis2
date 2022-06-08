while True:
    try:
        n=int(input())
        s=0
        c=1
        for i in range (0,200):
            s=s+2**i
            if n<=s:
                print(c)
                break
            c+=1
    except ValueError:
        break