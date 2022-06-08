n=int(input())
for i in range(n):
    x=str(input())
    s=''
    for j in x:
        if j=='2' or j=='3' or j=='5' or j=='7':
            s=s+j
    if s=='':
        print('-1')
    else:
        print(s)