import sys
for casos in sys.stdin:
    a1,b1,c1=map(int,casos.split())
    a2,b2,c2=map(int,input().split())
    if (a1+a2)==5 and (b1+b2)==5 and (c1+c2)==5 :
        print('Esta es la llave')
    else:
        print('Intenta con otra')