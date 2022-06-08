while 1>0:
    num= input().split()
    vars=num[1:]
    varInvert=vars[::-1]
    #print(varInvert)

    gg=" ".join(varInvert)
    """for i in varInvert:
        print(i,end=" ")
       """
    print(gg)