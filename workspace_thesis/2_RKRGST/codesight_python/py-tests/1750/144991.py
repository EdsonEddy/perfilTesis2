import unicodedata
from sys import stdin
for cad in stdin:
    cad=unicodedata.normalize("NFKD",cad).encode("ascii","ignore").decode("ascii")
    aux=cad
    t=""
    s=""
    sw=False
    n=len(cad)
    c=0
    f=cad[::-1]
    for i in range(1,n-1):
        q=f[i]
        ini=aux[c]
        t=t+ini
        s=s+q
        sv=s[::-1]
        c=c+1
        if(sv==t):
            sw=True
            break
    if(sw):
        print("si")
    else:
        print("no")