while True:
    pa = input()
    vo = ["A","E","I","O","U","Y","a","e","i","o","u","y"]
    sv = "."
    sd = list()
    for letra in pa:
        if letra not in vo:
            sd.extend(sv+letra.lower())
    a = sd
    sw = ""
    for letra in a:
        sw += letra
    print (sw)