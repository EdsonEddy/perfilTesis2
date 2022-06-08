import sys
for BIN in sys.stdin:
    BIN=int(BIN)
    b=bin(BIN)
    c=list(b)
    c.remove("b")
    C="".join(c)
    C=C.lstrip("0")
    alej=C[::-1]
    print(int(str(alej),2 ))