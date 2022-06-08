al=['A','B','C']*100
ed=['B','A','B','C']*100
ga=['C','C','A','A','B','B']*100
while True:
    N=int(input())
    n=input()
    cal=0
    ced=0
    cga=0
    r=0
    for i in range(N):
        if n[i]==ed[i] and n[i]==ga[i] and n[i]==al[i]:
            cal=cal+1
            ced=ced+1
            cga=cga+1
        elif n[i]==al[i]:
            cal=cal+1
            if n[i]==ga[i]:
                cga=cga+1
            if n[i]==ed[i]:
                ced=ced+1
        elif n[i]==ed[i]:
            ced=ced+1
            if n[i]==al[i]:
                cal=cal+1
            elif n[i]==ga[i]:
                cga=cga+1
        elif n[i]==ga[i]:
            cga=cga+1
            if n[i]==al[i]:
                cal=cal+1
            elif n[i]==ed[i]:
                ced=ced+1
    r=(max(cal,ced,cga))
    print(r)
    if cal==ced and ced==cga:
        print('Alvaro')
        print('Edwin')
        print('Gabriel')
    elif cal>ced and cal>cga:
        print("Alvaro")
    elif ced>cal and ced>cga:
        print("Edwin")
    elif cga>cal and cga>ced:
        print("Gabriel")


    elif (cal and ced)>cga:
        print("Alvaro")
        print('Edwin')
    elif (cal and cga)>ced:
        print('Alvaro')
        print('Gabriel')
    elif (ced and cal)>cga:
        print('Alvaro')
        print('Edwin')
    elif (ced and cga)>cal:
        print('Edwin')
        print('Gabriel')
    elif (cga and cal)>ced:
        print('Alvaro')
        print('Gabriel')
    elif (cga and ced)>cal:
        print('Edwin')
        print('Gabriel')