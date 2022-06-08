Alvaro = ['A','B','C']*100 
Edwin = ['B','A','B','C']*100 
Gabriel = ['C','C','A','A','B','B']*100 
while True:
    N = int(input())
    n = input()
    pa = 0
    pe = 0
    pg = 0
    r = 0
    for i in range(N):
        if (n[i]==Edwin[i] and n[i]==Gabriel[i] and n[i]==Alvaro[i]):
            pa = pa + 1
            pe = pe + 1
            pg = pg + 1
        elif (n[i]==Alvaro[i]):
            pa = pa + 1
            if (n[i]==Gabriel[i]):
                pg = pg + 1
            if (n[i]==Edwin[i]):
                pe = pe + 1
        elif (n[i]==Edwin[i]):
            pe = pe + 1
            if (n[i]==Alvaro[i]):
                pa = pa + 1
            elif (n[i]==Gabriel[i]):
                pg = pg + 1
        elif (n[i]==Gabriel[i]):
            pg = pg + 1
            if (n[i]==Alvaro[i]):
                pa = pa + 1
            elif (n[i]==Edwin[i]):
                pe = pe + 1
    r=(max(pa,pe,pg))
    print(r)
    if (pa==pe and pe==pg):
        print('Alvaro')
        print('Edwin')
        print('Gabriel')
    elif (pa>pe and pa>pg):
        print("Alvaro")
    elif (pe>pa and pe>pg):
        print("Edwin")
    elif (pg>pa and pg>pe):
        print("Gabriel")
    elif ((pa and pe)>pg):
        print("Alvaro")
        print('Edwin')
    elif ((pa and pg)>pe):
        print('Alvaro')
        print('Gabriel')
    elif ((pe and pa)>pg):
        print('Alvaro')
        print('Edwin')
    elif ((pe and pg)>pa):
        print('Edwin')
        print('Gabriel')
    elif ((pg and pa)>pe):
        print('Alvaro')
        print('Gabriel')
    elif ((pg and pe)>pa):
        print('Edwin')
        print('Gabriel')