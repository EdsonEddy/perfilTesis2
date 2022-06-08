from sys import*
n=int(stdin.readline())
for k in range(n):
    a=stdin.readline()
    mayu,minus,numero,simbolo=0,0,0,0
    for i in a:
        if i >="A" and i<="Z":
            mayu=1
        elif i>="a" and i<="z":
            minus=1
        elif i>="0" and i<="9":
            numero=1
        elif i=="@" or i=="_" or i==">" or i=="<" or i=="-" or i ==".":
            simbolo=1
    if(mayu+minus+numero+simbolo)==4:
        stdout.write("Dale no te jackiaran esta vez.\n")
    else:
        stdout.write("No va dar Botas.\n")

