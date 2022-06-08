while True:
    a=int(input())
    if (a == -1):
        break
    else:
        i=0
        r=-1
        while (i <= a):
            r=r+2
            i=i+1
        print (r)