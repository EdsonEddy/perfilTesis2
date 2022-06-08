while 1>0:
    s=''
    sw=False
    n=list(map(str,input().split()))
    for i in range(len(n),0,-1):

        if sw:
            s=s+n[i]+' '
        sw=True

    s=(s[:len(s)-1])
    print(s)