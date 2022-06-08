P=0
while(P!=" "):
    P=int(input())

    U=int(bin(P)[2:])

    U=str(int(U))

    CadenaInvertida=U[::-1]

    V=int(str(CadenaInvertida))

    print(int(str(V),2))