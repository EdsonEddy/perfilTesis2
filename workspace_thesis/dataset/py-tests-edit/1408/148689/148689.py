casos=int(input())
while casos > 0:
    casos-=1
    cad=str(input())
    a="ABC"*1000000
    b="BABC"*1000000
    c="CCAABB"*1000000
    ca=0
    cb=0
    cc=0
    j=0
    k=0
    w=0
    for q in cad:
            if q == a[j]:
                  ca=ca+1
            j+=1
    for z in cad:
            if z == b[k]:
                  cb=cb+1
            k+=1
    for s in cad:
            if s == c[w]:
                  cc=cc+1
            w+=1
    l=max(ca,cb)
    m=max(l,cc)
    print(m)
    if ca == m:
        print("Alvaro")
    if cb == m:
        print("Edwin")
    if cc== m:
        print("Gabriel")
