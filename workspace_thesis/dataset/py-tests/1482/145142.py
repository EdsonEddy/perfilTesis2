while True:
    x=int(input())
    i=1
    f=1
    if x>0:
        while i<=x:
            if i%2!=0:
                f=f*i
                f=f*(-1)
                print(f)
            else:
                f=f*i
                f=f*(-1)
                print(f)
            i=i+1
   
