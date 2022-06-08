while True:
    try:
        n=str(input())+"0"
        ca=""
        c=0
        for e in range(0,len(n)):
            if n[e] == "1":
                c+=1
            elif n[e] == "0":
                ca=ca+str(c)
                c=0
        print(ca)
    except ValueError:
        break