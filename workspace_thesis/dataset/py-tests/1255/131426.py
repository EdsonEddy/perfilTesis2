while True:
    h1,m1,h2,m2=map(int,input().split())
    if h2==00:
        h2=24
    if m2<m1:
        h2=h2-1
        m2=m2+60
    op1=h2-h1
    op2=m2-m1
    print(op1,op2)