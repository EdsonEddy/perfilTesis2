while(True):
    cad = input()
    if cad=="end":
        break
    n = len(cad)
    aux = cad
    cad = cad +"***"
    flag = False
    vo = 0
    con = 0
    for i in range(n):
        if cad[i] == "a" or cad[i] == "e" or cad[i] == "i" or cad[i] == "o" or cad[i] == "u":
            flag = True
            vo = vo+1
            con = 0
        else:
            con = con+1
            vo = 0
        if con == 3 or vo == 3:
            flag = False
            break
        if (cad[i] !="e" and cad[i] != "o") and cad[i] == cad[i+1]:
            flag = False
            break
    if flag == True:
        print("<"+aux+"> is acceptable.")
    else:
        print("<"+aux+"> is not acceptable.")