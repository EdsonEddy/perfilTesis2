while True:
    n=input()
    c=1
    if n=="end":
        exit()
    else:
        vocales=["a","e","i","o","u"]
        consonantes=["b","c","d","f","g","h","j","k","l","n","m","p","q","r","s","t","v","w","x","y","z"]
        c1=0
        c2=0
        c3=0
        error=0
        eer=0
        for i in n:
            if i in vocales:
                c1=1
            if i in consonantes:
                c2=c2+1
                c3=0
            if i in vocales:
                c3=c3+1
                c2=0
            if c<=len(n)-1:
                if i == n[c] and i!="o" and i !="e":
                    error=1
            if c3==3 or c2==3:
                eer=1
            c=c+1
        if c1==1 and eer!=1 and error !=1:
            print("<"+n+"> is acceptable.")
        else:
            print("<"+n+"> is not acceptable.")