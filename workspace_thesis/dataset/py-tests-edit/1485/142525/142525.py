import sys
for x in sys.stdin:
    n=int(x)
    cont = 0
    for i in range(1,n+1):
        k=input()
        invert=k[::-1]
        if(k==invert):
            cont=cont+1
    print(cont)