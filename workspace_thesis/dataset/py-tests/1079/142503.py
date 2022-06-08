while 1>0:
    a=input()
    if a=="end":
        break
    j=a.upper()
    c=["A","E","I","O","U"]
    h=["B", "D", "F", "G", "H", "J", "K", "L", "M", "N", "Ñ", "P", "Q", "R", "S","T", "V", "X", "Y", "Z"]
    d=0
    e="el gato dice miau"
    f=1
    x=0
    y=0
    i=1
    z="hola"
    for b in j:
        if b in c:
            d=1
            x=x+1
            if y<3:
                y=y*0
            z=b
        if b==e and b!="E" and b!="O":
            f=0
        e=b
        if b in h:
            y=y+1
            if x<3:
                x=x*0
    if x>2 or y>2:
        i=0
    if d+f+i==3:
        print("<%s> is acceptable." %a)
    else:
        print("<%s> is not acceptable." %a)