n=int(input())
while n!=0:
    x=n
    i=1
    p=0
    im=0
    while x>0:
        d=x%10
        x=x//10
        if i%2==0:
            p=p+d
        else:
            im=im+d
        i=i+1
    if p==im:
         print('SI')
    else:
        print('NO')
    n=int(input())
