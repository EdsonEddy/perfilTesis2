while True:
    a,b,c,d = map(float,input().split())
    if b!=0 and d!=0:
        x = a/b
        y = c/d
        if x == y:
            print('=')
        else:
            print('!=')
    elif a==0 and b==0 and c==0 and d==0:
        break