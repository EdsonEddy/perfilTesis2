import sys

for line in sys.stdin:
    a,b=[int(x)for x in line.split()]

    if  b > int((a+1)/2):
        b = b - int((a+1)/2)
        print(2*b)
    else:
        print(b*2-1)
