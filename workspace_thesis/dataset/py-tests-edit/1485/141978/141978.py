import sys
for linea in sys.stdin:
    def id(num):
        c=int(str(num)[::-1])
        return (c)
    m=int(linea)
    x=0
    for i in range(m):
        numero = int(input())
        if(numero == id(numero)):
	        x+=1
    print(x)