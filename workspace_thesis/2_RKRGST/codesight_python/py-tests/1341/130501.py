while True:
    m=int(input())
    a,b=0,1
    for i in range(m):
         a,b=b,a+b
    print(a)