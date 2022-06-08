from sys import stdin
import math
n = int(input())
for i in range(n):
    tec = input()
    cad = input()
    v = [0 for i in range(260)]
    step = 0
    for j in range(len(tec)):
        v[ord(tec[j])]=j
    for j in range(len(cad)-1):
        aux = abs(v[ord(cad[j])]-v[ord(cad[j+1])])
        step = step +aux
    print(step)