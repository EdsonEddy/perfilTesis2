while True:
    fn = int(input())
    vr = 0
    vr = fn*fn
    c = 0
    for x in range(fn):
        c+=1
        d = 0
        for f in range(fn):
            d += 1
            print (c,"/",d, sep="")