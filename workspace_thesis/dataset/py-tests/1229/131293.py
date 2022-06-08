a,b=map(str,input().split())
if a>b:
    print('{} > {}'.format(a,b))
elif b>a:
    print('{} < {}'.format(a,b))
else:
    print('{} = {}'.format(a,b))