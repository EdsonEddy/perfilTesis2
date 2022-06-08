while True:
    b=int(input())
    B=int(bin(b)[2:])
    C=str(B)
    res=C[::-1]
    print(int(str(res),2 ))