a = input()
s = ''
a1 = "0000000"
a2 = "000000"
a3 = "00000"
a4 = "0000"
a5 = "000"
a6 = "00"
a7 = "0"
for x in a:
    i = ord(x)
    i = bin(i)
    u = i.lstrip("0b")
    conta = len(u)
    if(conta == 1):
        i = str(i)
        s = s + a1 + u
    elif(conta == 2):
        i = str(i)
        s = s + a2 + u
    elif(conta == 3):
        i = str(i)
        s = s + a3 + u
    elif(conta == 4):
        i = str(i)
        s = s + a4 + u
    elif(conta == 5):
        i = str(i)
        s = s + a5 + u
    elif(conta == 6):
        i = str(i)
        s = s + a6 + u
    elif(conta == 7):
        i = str(i)
        s = s + a7 + u
    else:
        s = s + u
print(s)