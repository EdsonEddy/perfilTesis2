from sys import *
for casos in stdin :
    lon,piezas=map(int,casos.split())
    if lon >= sum(range(1,piezas+1)):
        print ('posible')
    else :
        print ('imposible')