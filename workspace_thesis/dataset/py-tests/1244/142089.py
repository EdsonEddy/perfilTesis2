from math import pi
from sys import stdin

for x in stdin:
    n = int(x)
    for i in range(n):
        des = input().split()
        cad = des[0]
        a = 0
        if cad == 'rectangle':
            b, h = float(des[1]), float(des[2])
            a = b * h
        if cad == 'circle':
            r = float(des[1])
            a = pi * (r ** 2)
        print('{:.2f}'.format(a))