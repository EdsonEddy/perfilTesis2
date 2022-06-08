while(True):
    cad = input()
    if(cad == "#"):
        break
    for i in range(len(cad)):
        if(cad[i] == ' '):
            print("%20", end = "")
        elif(cad[i] == '!'):
            print("%21", end = "")
        elif(cad[i] == '$'):
            print("%24", end = "")
        elif(cad[i] == '%'):
            print("%25", end = "")
        elif(cad[i] == '('):
            print("%28", end = "")
        elif(cad[i] == ')'):
            print("%29", end = "")
        elif(cad[i] == '*'):
            print("%2a", end = "")
        else:
            print(cad[i], end = "")

    print("")
