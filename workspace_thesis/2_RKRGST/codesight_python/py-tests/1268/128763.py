while True:
    c,p =map(int, input().split())
    if (p==0 and c==0):
        break
    else:
        if (p % 2==1):
            print ("-1")
        else:
            v=int(p/2 - c)
            g=int(c-v)
            if (v<0 or g<0):
                print ("-1")
            else:
                print (g,v)