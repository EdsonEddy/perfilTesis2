casos = int(input())
for i in range(casos):
    palabras=int(input())
    cc=0
    x=0
    for a in range(palabras):
        n=input()
        if "porque" in n:
            x=1
            cc=cc
        elif "porque" not in n and x!=1:
            cc=cc+1
    print(cc)