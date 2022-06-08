while 1>0:
    abc='abcdefghijklmnopqrstuvwxyz'
    n=str(input())
    n=sorted(n)
    l=n[len(n)-1]
    s=0
    k=chr(ord(l)+1)
    if k>'z':
        print('-1')
    else:
        for i in abc:
            if i not in n:
                s=1
                print(i)
                break
        if s==0:

            print('-1')
