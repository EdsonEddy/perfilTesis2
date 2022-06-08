import sys
for casos in sys.stdin:
    h1,m1,h2,m2=map(int,casos.split())
    if h2 == 0 :
        h2 = 24
    uno=h1*60+m1
    dos=h2*60+m2
    tiempo=dos-uno
    print(tiempo//60,tiempo%60)
