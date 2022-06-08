while True:
    n=int(input())
    lib=int(n/240)
    n1=int(n%240)
    chel=int(n1/12)
    pen=int(n1%12)
    print("("+str(lib)+", "+str(chel)+", "+str(pen)+")")