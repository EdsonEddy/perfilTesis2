from sys import *
for casos in stdin:
    a,b=casos.split()
    ret = sum (1 for i in range (len (a)) if a [i] != b [i])
    print( ["feliz", "lentes"][ret > 1])