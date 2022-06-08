while True:
    import math
    n=int(input())
    par=0
    cd=0
    imp=0
    p=n
    while p!=0:
        di=p//1%10
        cd=cd+1
        p=p//10
    while n!=0:
        d=n//1%10
        if(cd%2==1):
            imp=imp+d
        else:
            if(cd%2==0):
                par=par+d
        cd=cd-1
        n=n//10
    if(par!=imp):
        print("NO")
    else:
        if(par==imp):
            print("SI")
