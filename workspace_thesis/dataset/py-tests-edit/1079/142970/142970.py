voc=['a','e','i','o','u']
while 1>0:
    xd=0
    c=''
    v=''
    n=str(input())
    if n=='end':
        break
    for i in n:
        if i in voc:
            s=True
            xd=xd+1
            v=v+i
            if v=='ee' or v=='oo':
                v=''
            c=''
            if v=='aa' or v=='ii' or v=='uu':
                s=False
                break
            if len(v)>=3:
                s=False
                break
        else:
            c=c+i
            v=''
            if len(c)>=2:
                if c[0]==c[1]:
                    s=False
                    break
            if len(c)>2:
                s=False
                break
    if s and xd>0:
        print('<',end='')
        print(n, end='')
        print('>', end=' ')
        print('is acceptable.')
    else:
        print('<', end='')
        print(n, end='')
        print('>', end=' ')
        print('is not acceptable.')