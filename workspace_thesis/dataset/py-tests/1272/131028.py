import math
from sys import stdin,stdout
for n in stdin:
    n = int(n)
    comp = (1<<10) - 1
    flag = False
    for fghij in range(1234,98765):
        abcde = fghij * n
        if(abcde > 99999):
            break
        if(int(math.log10(fghij) + 1) == 4):
            val = 1
        else:
            val = 0
        x = int(fghij)
        y = int(abcde)
        while(x > 0):
            d = int(x % 10)
            x = int(x / 10)
            val = val | (1 << d)
        while(y > 0):
            d = int(y % 10)
            y = int(y / 10)
            val = val | (1 << d)
        if(val == comp):
            flag = True
            stdout.write(str(abcde)+" / "+str(fghij)+" "+str(n)+"\n")
    if(flag == False):
        stdout.write("No hay soluciones para"+" "+str(n)+"\n")
