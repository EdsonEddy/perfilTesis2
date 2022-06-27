t = input()
for q in range(int(t)):
    Nfibo=int(input())
    if Nfibo==0:
        print("0")
    elif Nfibo==1:
        print("1")
    else:
        a=0
        b=1
        cont=1
        while Nfibo != b:
            c=b
            b=b+a
            a=c
            cont+=1
            if Nfibo == b:
                print(cont)
            elif b > Nfibo:
                print("0")
                break
