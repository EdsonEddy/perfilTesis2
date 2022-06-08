def cadena(x):
    num = {0: "", 1: "unu", 2: "du", 3: "tri", 4: "kvar", 5: "Kvin", 6: "ses", 7: "Sep", 8: "OK", 9: "Nau", 10: "dek"}
    if int(n) < 11:
        return(num[int(n)])
    elif int(n) < 20:
        cad = "dek" + " " + num[int(n[1])]
    else:
        cad = num[int(n[0])] + "dek" + " " + num[int(n[1])]

    if int(n[1]) == 0 and int(n) != 10:
        return cad[0:len(cad) - 1]

    else:
        return cad


while True:
    n=input()
    print(cadena(n))
    