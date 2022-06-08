for casos in range(int(input())) :
    n=int(input())
    sw=0;
    d1=n%10
    n=n//10
    while(n>0):
        d2=n%10
        if d2 <= d1 :
            print("NO!")
            break
        n=n//10
        d1=d2
    else :
        print('SI!')
