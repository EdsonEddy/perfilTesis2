while 1>0:
    precio,total=map(int,input().split())
    con=0
    con2 = 0
    if precio==total:
        con=con+1
        print(con)
    else:
        s=0
        while s!=total:
                s=s+((2**con2)*precio)
                con2=con2+1
                con=con+1
        print(con)